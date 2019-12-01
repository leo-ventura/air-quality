const $chart_rain = document.getElementById("chart-rain");
get("/analise?minData=2018-12-25&maxData=2018-12-26&minChuva=0", function() {
  if(ok(this.status)) {
    const data = JSON.parse(this.response).slice(-50);

    let times = [];
    // Separate each analysis by station
    const rain_stations = [];
    data.forEach(e => {
      if(!rain_stations[e.EstacaoCodigo])
        rain_stations[e.EstacaoCodigo] = [];
      rain_stations[e.EstacaoCodigo].push(e);
      // Collect all times as well
      times.push(e.Data_e_hora);
    });
    // Get distinct times, and sort them ascending
    times = [...new Set(times)].sort();

    // Create array for all rain values
    const values = [];
    rain_stations.forEach(e => {
      values.push({
        name: stations[e[0].EstacaoCodigo].name,
        data: times.map(t => {
          const found = e.find(an => an.Data_e_hora === t)||{};
          const ret = found.Chuva;
          return ret || null;
        })
      });
    });

    const rain_chart = new ApexCharts($chart_rain, {
      chart: {
        type: "bar",
        stacked: true,
        toolbar: preventZoomConfig,
        animations: { enabled: false }
      },
      dataLabels: { enabled: false },
      stroke: { curve: "straight" },
      colors: [ "#ef476f", "#ffd166", "#26547c", "#06d6a0", "#253031", "#6874e8", "#f26df9"],
      series: values,
      xaxis: {
        type: "datetime",
        categories: [ ...times ]
      },
      yaxis: {
        labels: { formatter: (value) => `${value} mm` }
      }
    });
    rain_chart.render();
  }
});