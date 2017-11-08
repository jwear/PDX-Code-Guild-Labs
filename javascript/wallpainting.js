
function calculate(width, height, per_gallon_cost, num_coat) {
  var area_needed = (width * height) * num_coat
  var gallons_needed = Math.ceil(area_needed / 400)
  var full_cost = gallons_needed * per_gallon_cost
  console.log("You will need to buy " + gallons_needed + " gallons of paint. It will cost $" + full_cost + " you to paint the wall.")
}

calculate(20, 20, 5, 2)
