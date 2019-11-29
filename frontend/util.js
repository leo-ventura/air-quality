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
  buf.push(d.getDate());
  buf.push(d.getMonth()+1);
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

function plot(data,element,x,y,series_name,formatter) {
  const times = data.map(e => e[x]);
  const values = data.map(e => e[y]);

  // apexcharts.com/docs/
  const chart = new ApexCharts(element, {
    chart: { type: "area", toolbar: preventZoomConfig },
    tooltip: { x: {
      show: true,
      format: "HH:mm – dd/MM/yyyy",
    }},
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
    yaxis: { labels: { formatter: formatter } }
  });
  chart.render();
}