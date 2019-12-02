// Create the map
const map = L.map("map").setView([-22.8879,-43.4711], 10);

// Set up the OSM layer
L.tileLayer(
  //"http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png",
  "https://cartodb-basemaps-{s}.global.ssl.fastly.net/light_all/{z}/{x}/{y}.png",
  //"https://cartodb-basemaps-{s}.global.ssl.fastly.net/light_nolabels/{z}/{x}/{y}.png",
  {
    maxZoom: 18,
    minZoom: 10,
    attribution: `&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>, &copy; <a href="https://carto.com/attributions">CARTO</a>`,
 }
).addTo(map);

// Get station data
get("/estacoes", function() {
  if(ok(this.status)) {
    const data = JSON.parse(this.response);
    plotStationsToMap(data);
  }
});

const tags = [];
// Get tag data
get("/tags", function() {
  if(ok(this.status)) {
    const res = JSON.parse(this.response);
    res.forEach(t => {
      tags.push({
        name: t.Tag,
        zone: t.Zona_id
      });
    });

    // Then, get zone data
    get("/zonas", function() {
      if(ok(this.status)) {
        const data = JSON.parse(this.response);
        plotZonesToMap(data);
      }
    });
  }
});

const stations = {};
function plotStationsToMap(data) {
  data.forEach(e => {
    const center = [e.Latitude, e.Longitude];
    const circle = L.marker(center, 1000).addTo(map)
      .bindPopup(`<b>${xss(e.SiglaLocal)}</b><br>${xss(e.NomeEstacao)}`);
    stations[e.Codigo] = {
      name: e.NomeEstacao,
      acronym: e.SiglaLocal
    };
  });
}

const zones = {};
function plotZonesToMap(data) {
  data.reverse().forEach(e => {
    const center = [e.Latitude, e.Longitude];

    const buf = [];
    tags.forEach(t => {
      if(+t.zone === +e.Zona_id)
        buf.push(`Tag: ${t.name}`);
    });

    L.circle(center, {radius: e.Raio}).addTo(map)
      .bindPopup(`<b>${xss(e.Nome)}</b><br>${
        buf.join("<br>")
      }`);
    zones[e.Zona_id] = {
      name: e.Nome,
      coord: center,
      radius: e.Raio
    };
  });
}