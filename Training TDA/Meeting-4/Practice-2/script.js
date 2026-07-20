// Array berisi daftar belanja
let shoppingList = [
  "Wheat bread",
  "Pasta",
  "Tomato sauce",
  "Lowfat yogurt",
  "Butter"
];

// Menampilkan shopping list ke console
console.log("Shopping List:", shoppingList);

// Menampilkan shopping list ke halaman web
const output = document.getElementById("output");
output.innerHTML = shoppingList.map((item) => `<li>${item}</li>`).join("");
