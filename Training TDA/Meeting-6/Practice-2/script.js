// Score player
let score = 120;

// check level
let level = score > 100 ? 2 : 1;

// Menampilkan hasil ke console
console.log("Score:", score);
console.log("Level:", level);

// Menampilkan hasil ke halaman web
const output = document.getElementById("output");
output.textContent = `Score ${score}, level player adalah ${level}.`;

