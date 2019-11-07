//marking the drop down with all the values

const dataName = "samples.json";
var mdata;
d3.json(dataName).then(data => {
  var name_item = data.names;
  // need to call metadata then pass it into the chart, idk how
  console.log(name_item);
  var selectSub = document.getElementById("selDataset");

  var name = [];
  for (var i = 0; i < name_item.length; i++) {
    var item = document.createElement("option");
    item.value = name_item[i];
    item.text = name_item[i];
    selectSub.appendChild(item);
  }

  mdata = data.metadata;
  console.log(mdata);
  var dropd = d3.select("#selDataset");
  var selectID = dropd.property("value");
  console.log("This is selected: " + selectID);

  updatePage(selectID);
});
function updatePage(id) {
  console.log("IN UPDATE PAGE");
  let selectedData = mdata.filter(d => d.id == id)[0];
  let frequency = selectedData.wfreq;

// my gauge

  var gaugeData = [
    {
      domain: { x: [0, 1], y: [0, 1] },
      value: frequency,
      title: { text: "frequency of cleaning" },
      type: "indicator",
      mode: "gauge+number"
    }
  ];
  var layout = { width: 600, height: 500, margin: { t: 0, b: 0 } };

  Plotly.newPlot("gauge", gaugeData, layout);


  // document.getElementById(
  //     "sample-metadata"
  //   ).innerHTML = `<b>ID ${II.id} </b>
  //         <b>wash frequency</b>${II.wfreq}<br>`;

  // mdata.forEach(II => {
  //   //
  //   if (II.id == selectID) {
      

  //     // graph timeeeeeee

  //     var levis_array = Array.from({ length: 10 }, (v, k) => k).reverse();

      
  //   }
  // });
}