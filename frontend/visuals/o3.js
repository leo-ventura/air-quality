const $chart_ozone = document.getElementById("chart-ozone");
get("/qualidadeDoAr?siglaLocalEstacao=SP&poluente=O3", function() {
  if(ok(this.status)) {
    const data = JSON.parse(this.response);
    plot(
      data.slice(-50),
      $chart_ozone,
      "Data",
      "IQAR",
      "IQAR O<sub>3</sub>",
      ["#f7b801"],
      (value) => `${value} / 300`
    );
  }
});