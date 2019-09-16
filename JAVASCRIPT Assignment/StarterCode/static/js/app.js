// from data.js
var tableData = data;
console.log(tableData);
my_table = d3.select("#ufo-table tbody")

// making my table

createTable=(tableData)=>{
}
tableData.forEach(row => {
  my_table.append('tr').html(`<td>${row.datetime}</td><td>${row.city}</td><td>${row.state}</td><td>${row.country}</td><td>${row.shape}</td><td>${row.durationMinutes}</td><td>${row.comments}</td>`)

});

  // making my filter,
  // what we do here is call the filtered data
var button = d3.select("#filter-btn");

button.on("click", function() {
  d3.selectAll("#ufo-table tbody tr").remove()
  var inputElement = d3.select("#datetime");
  var inputValue = inputElement.property("value");
  var filteredData = tableData.filter(my_ufo => my_ufo.datetime === inputValue)
  filteredData.forEach(row => {
  my_table.append('tr').html(`<td>${row.datetime}</td><td>${row.city}</td><td>${row.state}</td><td>${row.country}</td><td>${row.shape}</td><td>${row.durationMinutes}</td><td>${row.comments}</td>`)
    })
  })

