const $chart_nitrogen = document.getElementById("chart-nitrogen");
get("/qualidadeDoAr?siglaLocalEstacao=SP&poluente=NO2", function() {
  if(ok(this.status)) {
    const data = JSON.parse(this.response);
    plot(
      data.slice(-50),
      $chart_nitrogen,
      "Data",
      "IQAR",
      "IQAR NO<sub>2</sub>",
      ["#e2711d"],
      (value) => `${value} / 300`
    );
  }
});