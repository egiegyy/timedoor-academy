// 1. Cek angka positif atau negatif
let number = -8;

if (number > 0) {
  console.log("Angka positif");
} else if (number < 0) {
  console.log("Angka negatif");
} else {
  console.log("Angka nol");
}

// 2. Cek umur untuk membuat SIM
let age = 21;

if (age >= 17) {
  console.log("Boleh membuat SIM");
} else {
  console.log("Belum boleh membuat SIM");
}

// 3. Penilaian grade A-D
let score = 86;
let grade;

if (score >= 90) {
  grade = "A";
} else if (score >= 80) {
  grade = "B";
} else if (score >= 70) {
  grade = "C";
} else {
  grade = "D";
}
console.log("Grade:", grade);

// 4. Diskon member
let isMember = true;
let price = 100000;
let finalPrice;

if (isMember) {
  finalPrice = price - 20000;
} else {
  finalPrice = price;
}
console.log("Harga akhir:", finalPrice);

// 5. Pilih karakter Knight atau Wizard
let character = "Wizard";

if (character === "Knight") {
  console.log("Kamu memilih Knight dengan pedang kuat.");
} else if (character === "Wizard") {
  console.log("Kamu memilih Wizard dengan sihir hebat.");
} else {
  console.log("Karakter tidak tersedia.");
}

// Menampilkan hasil utama ke halaman web
const output = document.getElementById("output");
output.innerHTML = `
  <p>Number: ${number}</p>
  <p>Age: ${age}</p>
  <p>Grade: ${grade}</p>
  <p>Final Price: ${finalPrice}</p>
  <p>Character: ${character}</p>
`;
