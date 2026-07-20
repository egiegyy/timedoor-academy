// Task 1: Menyimpan shopping list ke array
let shoppingList = [
  "Wheat bread",
  "Pasta",
  "Tomato sauce",
  "Lowfat yogurt",
  "Butter"
];

// Mengambil item pertama ke variable importantToBuy
let importantToBuy = shoppingList[0];

// Mengganti Lowfat yogurt menjadi Soy Milk
shoppingList[3] = "Soy Milk";

// Menggunakan length untuk menghitung jumlah item
let shoppingListLength = shoppingList.length;

// Task 2: Membuat array holidayPlans
let holidayPlans = ["Paris", "Tokyo", "Sidney", "New York"];

// Menambahkan Bali dan Hokkaido ke holidayPlans
holidayPlans.push("Bali", "Hokkaido");

// Menampilkan semua hasil ke console
console.log("Important to buy:", importantToBuy);
console.log("Shopping list setelah diubah:", shoppingList);
console.log("Jumlah shopping list:", shoppingListLength);
console.log("Holiday plans:", holidayPlans);

// Menampilkan hasil singkat ke halaman web
const output = document.getElementById("output");
output.innerHTML = `
  <p>Important to buy: ${importantToBuy}</p>
  <p>Jumlah shopping list: ${shoppingListLength}</p>
  <p>Holiday plans: ${holidayPlans.join(", ")}</p>
`;
