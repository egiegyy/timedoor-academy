// Batas bermain game per hari
let dailyLimit = 2;

// Data jam bermain game Steve selama beberapa hari
let gameHours = [1.5, 3, 2, 4, 1, 2.5, 5];

// total and over limit count
let totalHours = 0;
let overLimitCount = 0;

// Menghitung total jam dan mengecek hari yang melebihi batas
for (let i = 0; i < gameHours.length; i++) {
  totalHours += gameHours[i];

  if (gameHours[i] > dailyLimit) {
    overLimitCount++;
  }
}

// Menampilkan hasil ke console
console.log("Data jam bermain Steve:", gameHours);
console.log("Total jam bermain:", totalHours);
console.log("Jumlah melebihi batas 2 jam:", overLimitCount);

// Menampilkan hasil ke halaman web
const output = document.getElementById("output");
output.innerHTML = `
  <p>Total jam bermain game Steve: ${totalHours} jam</p>
  <p>Jumlah melebihi batas 2 jam: ${overLimitCount} kali</p>
`;

