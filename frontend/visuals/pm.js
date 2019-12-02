for(const y of [2013,2018]) {
  get(`/analise?minData=${y}-12-26&maxData=${y+1}&estacaoCodigo=5`, function() {
    if(ok(this.status)) {
      const data = JSON.parse(this.response);

      const times = data.map(e => e.Data_e_hora);
      const pm10 = data.map(e => round(e.PM_10,4) || null);
      const pm2_5 = data.map(e => round(e.PM_2_5,4) || null);

      // Get length excluding `null`s
      const pm10_size = pm10.reduce((acc,cur)=> cur !== null ? acc += 1 : acc);
      const pm2_5_size = pm2_5.reduce((acc,cur)=> cur !== null ? acc += 1 : acc);

      // Get average
      const pm10_avg = pm10.reduce((acc,cur)=> acc += cur) / pm10_size;
      const pm2_5_avg = pm2_5.reduce((acc,cur)=> acc += cur) / pm2_5_size;

      document.getElementById(`avg-pm10-${y}-val`).textContent = round(pm10_avg,4);
      document.getElementById(`avg-pm2_5-${y}-val`).textContent = round(pm2_5_avg,4);

      const pm_chart = new ApexCharts(document.getElementById(`chart-${y}-pm`), {
        chart: { type: "area", toolbar: preventZoomConfig, height: 250,
        animations: { enabled: false }},
        tooltip: { x: {
          show: true,
          format: "HH:mm – dd/MM/yyyy",
        }},
        dataLabels: { enabled: false },
        colors: ["#ca3cff","#00ffc5"],
        fill: gradientConfig,
        stroke: { curve: "straight" },
        series: [{
          name: "PM<sub>2.5</sub>",
          data: [...pm2_5]
        },{
          name: "PM<sub>10</sub>",
          data: [...pm10]
        }],
        xaxis: {
          type: "datetime",
          categories: [ ...times ]
        },
        yaxis: {
          max: 90,
          min: 0,
          minWidth: 80,
          labels: { formatter: (value) => `${value} µg/m³` }
        }
      });
      pm_chart.render();
    }
  });
}