// Data film favorit Steve
let movieTitle = "Captain Marvel";
let movieRating = 6.8;
let movieYear = 2019;
let movieForAllAges = false;

// Data buku
let bookTitle = "The Quantum Universe";
let bookAuthors = "Brian Cox dan Jeff Forshaw";
let bookCategory = "science";

// Menampilkan data film ke console
console.log("Film Favorit Steve:");
console.log("Judul:", movieTitle);
console.log("Rating:", movieRating);
console.log("Tahun:", movieYear);
console.log("Untuk semua umur:", movieForAllAges);

// Menampilkan data buku ke console
console.log("Data Buku:");
console.log("Judul:", bookTitle);
console.log("Penulis:", bookAuthors);
console.log("Kategori:", bookCategory);

// Menampilkan informasi singkat ke halaman web
const output = document.getElementById("output");
output.innerHTML = `Film: ${movieTitle}<br>Buku: ${bookTitle}`;
