// 1. Menampilkan nama 20 kali menggunakan for loop
for (let i = 1; i <= 20; i++) {
  console.log(`${i}. Regina Alya Analanai`);
}

// 2. Menampilkan angka 1 sampai 20
for (let number = 1; number <= 20; number++) {
  console.log("Angka:", number);
}

// 3. Menampilkan kelipatan 5 sampai 100
for (let multiple = 5; multiple <= 100; multiple += 5) {
  console.log("Kelipatan 5:", multiple);
}

// Menampilkan informasi ke halaman web
const output = document.getElementById("output");
output.textContent = "Buka console browser untuk melihat hasil for loop.";
