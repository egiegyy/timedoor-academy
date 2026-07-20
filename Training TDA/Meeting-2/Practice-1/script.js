// Variable untuk menyimpan nama depan
let firstName = "Regina Alya";

// Variable untuk menyimpan nama belakang
let lastName = "Analanai";

// Variable untuk menyimpan angka favorit
let favoriteNumber = 7;

// Menampilkan semua variable ke console
console.log("First Name:", firstName);
console.log("Last Name:", lastName);
console.log("Favorite Number:", favoriteNumber);

// Menampilkan ringkasan ke halaman web
const output = document.getElementById("output");
output.textContent = `${firstName} ${lastName} memiliki angka favorit ${favoriteNumber}.`;
