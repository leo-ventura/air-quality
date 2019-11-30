const preventZoomConfig = {
  tools: {
    zoom: false,
    zoomin: false,
    zoomout: false,
    pan: false,
    reset: false
  }
};

const gradientConfig = {
  type: "gradient",
  gradient: {
    shadeIntensity: 1,
    opacityFrom: 0.7,
    opacityTo: 0.9,
    stops: [0, 100, 100]
  }
};

function get(url,callback) {
  if(!NET) return;
  const request = new XMLHttpRequest();
  request.open("GET", API+url, true);
  request.onload = callback;
  request.send();
}

function xss(str) {
  return (str+"")
    .split("&").join("&amp;")
    .split(">").join("&gt;")
    .split("<").join("&lt;");
}

function ok(status) {
  return status >= 200 && status < 400;
}

function round(num,dec=2) {
  const val = 10**dec;
  return ~~(num*val)/val;
}

function prettifyDate(str) {
  const d = new Date(str);
  const buf = [];
  buf.push(`${d.getDate()}`.padStart(2,0));
  buf.push(`${d.getMonth()+1}`.padStart(2,0));
  buf.push(d.getFullYear());
  return buf.join("/");
}

function prettifyTime(str) {
  const d = new Date(str);
  const buf = [];
  buf.push(d.getHours());
  buf.push(d.getMinutes());
  return buf.join(":");
}

function plotIQAR(data,element,x,y,series_name,colors) {
  const times = data.map(e => e[x]);
  const values = data.map(e => e[y]);

  const labelstyle = {
    text: "\u200C",
    borderWidth: 0,
    style: { padding: { left: 0, right: 0, top: 0, bottom: 0 } }
  };

  // apexcharts.com/docs/
  const chart = new ApexCharts(element, {
    chart: { type: "area", toolbar: preventZoomConfig },
    tooltip: { x: {
      show: true,
      format: "HH:mm – dd/MM/yyyy",
    }},
    colors: colors,
    dataLabels: { enabled: false },
    fill: gradientConfig,
    series: [{
      name: series_name,
      data: [...values]
    }],
    xaxis: {
      type: "datetime",
      categories: [ ...times ]
    },
    yaxis: {
      min: 0,
      max: 300,
      labels: { formatter: (value) => `${value} / 300` }
    },
    annotations: {
      yaxis: [{
        y: 51,
        y2: 100,
        borderColor: "#e5e5e5",
        fillColor: "#e5e5e5",
        label: labelstyle
      },{
        y: 101,
        y2: 199,
        borderColor: "#c2c2c2",
        fillColor: "#c2c2c2",
        label: labelstyle
      },{
        y: 200,
        y2: 299,
        borderColor: "#777",
        fillColor: '#777',
        label: labelstyle
      }]
    }
  });
  chart.render();
}