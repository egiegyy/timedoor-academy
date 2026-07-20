// Variable untuk menyimpan nama depan
let firstName = "Regina";

// Variable untuk menyimpan nama belakang
let lastName = "Alya Analanai";

// Function declaration bernama greeting
function greeting() {
  // Kode di dalam function hanya berjalan jika function dipanggil
  console.log(`My name is ${firstName} ${lastName}`);
}

// Memanggil function pertama kali
greeting();

// Memanggil function kedua kali
greeting();

// function will not run if we do not call it
console.log("Jika function tidak dipanggil, isi function tidak akan dieksekusi.");

// Menampilkan penjelasan ke halaman web
const output = document.getElementById("output");
output.innerHTML = `
  <p>My name is ${firstName} ${lastName}</p>
  <p>Function sudah dipanggil 2 kali. Cek console untuk melihat output lengkap.</p>
`;

