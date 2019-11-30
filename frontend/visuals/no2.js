const $chart_nitrogen = document.getElementById("chart-nitrogen");
get("/qualidadeDoAr?siglaLocalEstacao=SP&poluente=NO2", function() {
  if(ok(this.status)) {
    const data = JSON.parse(this.response).slice(-50);
    // Sort descending a clone of data array, and get the first (max) value
    const max = JSON.parse(JSON.stringify(data))
      .sort((a, b) => b.IQAR - a.IQAR)[0];

    // Add data to text
    document.getElementById("max-no2-val").textContent = max.IQAR;
    document.getElementById("max-no2-date").textContent = prettifyDate(max.Data);

    plotIQAR(
      data,
      $chart_nitrogen,
      "Data",
      "IQAR",
      "IQAR NO<sub>2</sub>",
      ["#e2711d"]
    );
  }
});