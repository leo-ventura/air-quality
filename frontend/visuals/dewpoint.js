const $chart_dewpoint = document.getElementById("chart-dewpoint");
const $chart_relhum = document.getElementById("chart-relhum");
get("/analise?estacaoCodigo=1", function() {
  if(ok(this.status)) {
    const data = JSON.parse(this.response).slice(-50);

    const times = data.map(e => e.Data_e_hora);

    const dewpoints = data.map(v => {
      if(!v.Temperatura || !v.UmidadeRelativaDoAr) return null;
      // Arden Buck equation approximation
      const mag = v.Temperatura - (100 - v.UmidadeRelativaDoAr) / 5;
      return round(mag,4);
    }).filter(e => !!e);
    const temperatures = data.map(e => round(e.Temperatura,4));
    const pressure = data.map(e => round(e.Pressao,4));
    
    const dew_chart = new ApexCharts($chart_dewpoint, {
      chart: {
        type: "area",
        toolbar: preventZoomConfig,
        height: 250,
        id: "dew-temp",
        group: "dew"
      },
      tooltip: { x: {
        show: true,
        format: "HH:mm – dd/MM/yyyy",
      }},
      dataLabels: { enabled: false },
      fill: gradientConfig,
      series: [{
        name: "Ponto de orvalho",
        data: [...dewpoints]
      },{
        name: "Temperatura",
        data: [...temperatures]
      }],
      xaxis: {
        type: "datetime",
        categories: [ ...times ]
      },
      yaxis: [{
        labels: {
          formatter: (value) => `${value} °C`,
          minWidth: 80
        }
      }]
    });
    dew_chart.render();

    const relhum = data.map(e => round(e.UmidadeRelativaDoAr,4));

    const relhum_chart = new ApexCharts($chart_relhum, {
      chart: {
        type: "area",
        toolbar: preventZoomConfig,
        height: 250,
        id: "dew-relhum",
        group: "dew"
      },
      tooltip: { x: {
        show: true,
        format: "HH:mm – dd/MM/yyyy",
      }},
      dataLabels: { enabled: false },
      colors: [ "#faa300", "#22Aed1" ],
      fill: gradientConfig,
      series: [{
        name: "Pressão",
        data: [...pressure]
      },{
        name: "Umidade relativa",
        data: [...relhum]
      }],
      xaxis: {
        type: "datetime",
        categories: [ ...times ]
      },
      yaxis: [{
        max: 1015,
        min: 1005,
        labels: {
          formatter: (value) => `${value} mbar`
        },
        minWidth: 80
      },{
        max: 100,
        min: 0,
        show: false,
        labels: {
          formatter: (value) => `${value}%`
        }
      }]
    });
    relhum_chart.render();
  }
});