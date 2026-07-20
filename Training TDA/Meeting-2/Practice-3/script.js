// Membuat variable paragraph
let paragraph = "JavaScript is Fun";

// Menghitung jumlah karakter paragraph
let paragraphLen = paragraph.length;

// Mengubah paragraph menjadi huruf kecil
let paragraphLowercase = paragraph.toLowerCase();

// Membandingkan paragraph asli dengan paragraph lowercase
let isSame = paragraph === paragraphLowercase;

// Menampilkan hasil ke console
console.log("Paragraph:", paragraph);
console.log("Jumlah karakter:", paragraphLen);
console.log("Lowercase:", paragraphLowercase);
console.log("Apakah sama?:", isSame);

// Menampilkan hasil ke halaman web
const output = document.getElementById("output");
output.textContent = `Panjang paragraph adalah ${paragraphLen}. Hasil perbandingan: ${isSame}.`;
