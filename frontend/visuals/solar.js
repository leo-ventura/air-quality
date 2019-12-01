const $chart_solar = document.getElementById("chart-solar");
const $chart_lux = document.getElementById("chart-lux");
get("/analise?minData=2012-03-20&maxData=2012-03-23&estacaoCodigo=4", function() {
  if(ok(this.status)) {
    const data = JSON.parse(this.response);

    const times = data.map(e => e.Data_e_hora);
    const sol = data.map(e => round(e.RadiacaoSolar,4) || null);

    // Solar efficacy, it's a constant
    const LumEff = 93;
    const lux = data.map(e => round(e.RadiacaoSolar*LumEff/1000,4) || null);

    const sol_chart = new ApexCharts($chart_solar, {
      chart: { type: "area", toolbar: preventZoomConfig, height: 250,
      animations: { enabled: false }},
      tooltip: { x: {
        show: true,
        format: "HH:mm – dd/MM/yyyy",
      }},
      dataLabels: { enabled: false },
      colors: ["#f7b801"],
      fill: gradientConfig,
      series: [{
        name: "Irradiância solar",
        data: [...sol]
      }],
      xaxis: {
        type: "datetime",
        categories: [ ...times ]
      },
      yaxis: { labels: { formatter: (value) => `${value} W/m²` } }
    });
    sol_chart.render();

    const lux_chart = new ApexCharts($chart_lux, {
      chart: { type: "area", toolbar: preventZoomConfig, height: 250,
      animations: { enabled: false }},
      tooltip: { x: {
        show: true,
        format: "HH:mm – dd/MM/yyyy",
      }},
      dataLabels: { enabled: false },
      colors: ["#ffd151"],
      fill: gradientConfig,
      series: [{
        name: "Iluminância Solar",
        data: [...lux]
      }],
      xaxis: {
        type: "datetime",
        categories: [ ...times ]
      },
      yaxis: { labels: { formatter: (value) => `${value} klx` } }
    });
    lux_chart.render();
  }
});