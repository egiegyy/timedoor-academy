// food list
var spicyFoods = ["Seblak", "Spicy Ramen", "Hot Chicken", "Balado Rice"];
var sweetFoods = ["Ice Cream", "Donut", "Chocolate Cake", "Milkshake"];
var healthyFoods = ["Salad", "Fruit Bowl", "Oatmeal", "Grilled Chicken"];
var fastFoods = ["Burger", "Pizza", "Hotdog", "French Fries"];

// recommend food by category
function recommendFood(category) {
  var selectedFoods;

  // choose category
  if (category === "Spicy") {
    selectedFoods = spicyFoods;
  } else if (category === "Sweet") {
    selectedFoods = sweetFoods;
  } else if (category === "Healthy") {
    selectedFoods = healthyFoods;
  } else if (category === "Fast Food") {
    selectedFoods = fastFoods;
  } else {
    alert("Category not found");
    console.log("Category not found");
    return;
  }

  // random food
  var randomIndex = Math.floor(Math.random() * selectedFoods.length);
  var food = selectedFoods[randomIndex];
  var message = "Your food recommendation is: " + food;

  // print result
  alert(message);
  console.log(message);
  document.getElementById("output").innerHTML = message;
}

// ask category with prompt
function askFoodCategory() {
  var category = prompt("Choose category: Spicy, Sweet, Healthy, Fast Food");

  // check prompt input
  if (category === null || category === "") {
    alert("No category selected");
    console.log("No category selected");
  } else {
    recommendFood(category);
  }
}

// show prompt when page opens
askFoodCategory();
