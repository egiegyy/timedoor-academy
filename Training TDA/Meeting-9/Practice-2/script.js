// Variable untuk menyimpan angka yang dicari
let expectedNumber = 5;

// random number variable
let randomNumber;

// Variable ini menyimpan riwayat angka random yang muncul
let randomHistory = [];

// Do-while akan berjalan minimal satu kali
// repeat until number is 5
do {
  randomNumber = Math.floor(Math.random() * 11);
  randomHistory.push(randomNumber);

  // Menampilkan setiap angka random ke console
  console.log("Random number:", randomNumber);
} while (randomNumber !== expectedNumber);

// Pesan ini muncul setelah angka 5 ditemukan
console.log("Angka 5 ditemukan. Program berhenti.");

// Menampilkan hasil ke halaman web
const output = document.getElementById("output");
output.innerHTML = `
  <p>Angka random: ${randomHistory.join(", ")}</p>
  <p>Angka 5 ditemukan. Program berhenti.</p>
`;

