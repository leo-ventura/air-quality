for(const y of [2017,2018]) {
  get(`/analise?minData=${y}-07&maxData=${y}-07-08&estacaoCodigo=6&minVelocidadeVento=0&minDirecaoVento=-1`, function() {
    if(ok(this.status)) {
      const data = JSON.parse(this.response);

      const times = data.map(e => e.Data_e_hora);
      const wind_dir = data.map(e => {
        return {
          dir: round(e.DirecaoVento,4),
          pwr: round(e.VelocidadeVento,4)
        }
      });
      const winds = new Array(8).fill(0);
      wind_dir.forEach(w => {
        const dir = Math.round(w.dir / 45);
        winds[dir] += w.pwr;
      });

      const wind_chart = new ApexCharts(document.getElementById(`chart-wind-${y}`), {
        chart: { type: "radar", toolbar: preventZoomConfig, height: 200, width: 200,
        animations: { enabled: false }},
        tooltip: { x: {
          show: true,
          format: "HH:mm – dd/MM/yyyy",
        }},
        dataLabels: { enabled: true },
        colors: [ y === 2017 ? "#ff3366" : "#20a4f3" ],
        series: [{
          name: "Velocidade acumulada do vento",
          data: [...(winds.map(w => round(w,4)))]
        }],
        labels: ["N", "NE", "E", "SE", "S", "SO", "O", "NO"],
        yaxis: { show: false,
          labels: { formatter: (value) => `${value} m/s` }
        }
      });
      wind_chart.render();
    }
  });
}