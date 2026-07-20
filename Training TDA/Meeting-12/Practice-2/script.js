// Function square menghitung luas dan keliling persegi
function square(side) {
  // Rumus luas persegi: sisi x sisi
  let area = side * side;

  // Rumus keliling persegi: 4 x sisi
  let circumference = 4 * side;

  // Menampilkan hasil ke console
  console.log("Square");
  console.log("Area :", area);
  console.log("Circumference :", circumference);

  // Menampilkan hasil ke halaman web
  document.getElementById("output").innerHTML = `Area : ${area}<br>Circumference : ${circumference}`;
}

// Function rect menghitung luas dan keliling persegi panjang
function rect(width, height) {
  // Rumus luas persegi panjang: panjang x lebar
  let area = width * height;

  // Rumus keliling persegi panjang: 2 x (panjang + lebar)
  let circumference = 2 * (width + height);

  // Menampilkan hasil ke console
  console.log("Rectangle");
  console.log("Area :", area);
  console.log("Circumference :", circumference);

  // Menampilkan hasil ke halaman web
  document.getElementById("output").innerHTML = `Area : ${area}<br>Circumference : ${circumference}`;
}

// Pesan awal saat halaman dibuka
console.log("Klik tombol Square atau Rectangle untuk menghitung.");
