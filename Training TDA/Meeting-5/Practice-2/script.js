// Koordinat player
let x = 0;
let y = 0;
let position;

// Menentukan posisi berdasarkan nilai x dan y
if (x > 0 && y > 0) {
  position = "top right";
} else if (x > 0 && y < 0) {
  position = "bottom right";
} else if (x < 0 && y > 0) {
  position = "top left";
} else if (x < 0 && y < 0) {
  position = "bottom left";
} else {
  position = "middle";
}

// Menampilkan posisi ke console
console.log("Koordinat x:", x);
console.log("Koordinat y:", y);
console.log("Posisi player:", position);

// Menampilkan posisi ke halaman web
const output = document.getElementById("output");
output.textContent = `Player berada di posisi ${position}.`;
