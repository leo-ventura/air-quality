const $chart_temperature = document.getElementById("chart-temperature");

const temperature_data = {};
// Get the max and min temperature reading
for(const par of ["max", "min"]) {
  get(`/${par}?tabela=Analise&coluna=Temperatura`, function() {
    if(ok(this.status)) {
      const data = JSON.parse(this.response);
      document.getElementById(`${par}-temp-val`).textContent = `${data[par]}`;
      temperature_data[par] = data[par];

      // Find analysis with that temperature value
      get(`/analise?temperatura=${data[par]}`, function() {
        if(this.status >= 200 && this.status < 400) {
          const data = JSON.parse(this.response)[0];

          // Prepare data
          const date = prettifyDate(data.Data_e_hora);
          const time = prettifyTime(data.Data_e_hora);
          const station = stations[data.EstacaoCodigo].name;

          // Add data to text
          document.getElementById(`${par}-temp-date`).textContent = date;
          document.getElementById(`${par}-temp-time`).textContent = time;
          document.getElementById(`${par}-temp-station`).textContent = station;
        }
      });

      // If `min` finished loading after `avg`
      if(par == "min" && "avg" in temperature_data)
        // Plot all the data
        plotTemperatureChart();
    }
  });
}
// Get average temperature
get("/avg?tabela=Analise&coluna=Temperatura", function() {
  if(ok(this.status)) {
    const data = JSON.parse(this.response);

    // Add fetched value to text
    document.getElementById("avg-temp-val").textContent = round(data.avg,4);

    // Save average value for plotting
    temperature_data.avg = data.avg;

    // If `avg` finished loading after `min`
    if("min" in temperature_data)
      // Plot all the data
      plotTemperatureChart();
  }
});

function plotTemperatureChart() {
  const temperature_chart = new ApexCharts($chart_temperature, {
    chart: { type: "rangeBar", toolbar: preventZoomConfig, height: 300 },
    states: { hover: { filter: { type: "none" } },
             active: { filter: { type: "none" } }
    },
    plotOptions: { bar: { horizontal: false } },
    fill: {
      type: "gradient",
      gradient: {
        type: "vertical",
        colorStops: [{
          offset: 0,
          color: "#fc466b" // red
        },{
          offset: 500,
          color: "#3f5efb" // blue
        }]
      }
    },
    dataLabels: {  enabled: false  },
    tooltip: {  enabled: false  },
    series: [{ data: [{
      x: "",
      y: [+temperature_data.min, +temperature_data.max]
    }]}],
    annotations: {
      yaxis: [{
        y: +temperature_data.avg,
        borderColor: "#1a1a1a", // black
        strokeDashArray: 0
      }]
    },
    yaxis: { labels: { formatter: (value) => `${value} °C` } }
  });
  temperature_chart.render();
}