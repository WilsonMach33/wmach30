// Set the dimensions of the SVG element and the margins of the chart
var width = 500,
    height = 300,
    margin = { top: 20, right: 20, bottom: 30, left: 50 };

// Define the birth data
var births = [
  { month: "January", births: 23000 },
  { month: "February", births: 22000 },
  { month: "March", births: 24000 },
  { month: "April", births: 22500 },
  { month: "May", births: 23500 },
  { month: "June", births: 24500 }
];

// Create the SVG element and append a group element to hold the chart
var svg = d3.select("#chart")
  .attr("width", width)
  .attr("height", height);

var chart = svg.append("g")
  .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

// Define the x-scale as an ordinal scale with the months as domain values
var x = d3.scaleBand()
  .domain(births.map(function(d) { return d.month; }))
  .range([0, width - margin.left - margin.right])
  .padding(0.1);

// Define the y-scale as a linear scale with the maximum births value as the domain
var y = d3.scaleLinear()
  .domain([0, d3.max(births, function(d) { return d.births; })])
  .range([height - margin.top - margin.bottom, 0])
  .nice();

// Add the x-axis to the chart
chart.append("g")
  .attr("class", "x axis")
  .attr("transform", "translate(0," + (height - margin.top - margin.bottom) + ")")
  .call(d3.axisBottom(x))
  
  .selectAll("text")
    .attr("y", 10)
    .attr("x", -5)
    .style("text-anchor", "middle")
  

// Add the y-axis to the chart
chart.append("g")
  .attr("class", "y axis")
  .call(d3.axisLeft(y).ticks(5))
  .append("text")
    .attr("transform", "rotate(-90)")
    .attr("y", 6)
    .attr("dy", ".71em")
    .style("text-anchor", "end")
    .text("Number of Births");

// Draw horizontal lines for each y-axis tick
chart.append("g")
  .attr("class", "grid")
  .call(d3.axisLeft(y)
    .tickSize(-width+75)
    .tickFormat("")
  )

// Draw vertical lines for each x-axis tick
chart.append("g")
  .attr("class", "grid")
  .attr("transform", "translate(0," + (height-50) + ")")
  .call(d3.axisBottom(x)
    .tickSize(-height+50)
    .tickFormat("")
  )

// Add the line to the chart
var line = d3.line()
  .x(function(d) { return x(d.month) + x.bandwidth() / 2; })
  .y(function(d) { return y(d.births); });

chart.append("path")
  .datum(births)
  .attr("class", "line")
  .attr("d", line);