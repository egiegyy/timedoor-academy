// Function untuk mengubah centimeter ke meter
function cmToMeter(cm) {
  return cm / 100;
}

// Function untuk mengubah centimeter ke kilometer
function cmToKilometer(cm) {
  return cm / 100000;
}

// Function untuk mengubah centimeter ke millimeter
function cmToMillimeter(cm) {
  return cm * 10;
}

// Menyimpan nilai centimeter yang akan dikonversi
let centimeter = 100;

// Memanggil function dan menyimpan hasilnya
let meter = cmToMeter(centimeter);
let kilometer = cmToKilometer(centimeter);
let millimeter = cmToMillimeter(centimeter);

// Menampilkan hasil ke console
console.log(`${centimeter} cm is ${meter} meter`);
console.log(`${centimeter} cm is ${kilometer} kilometer`);
console.log(`${centimeter} cm is ${millimeter} millimeter`);

// Menampilkan hasil ke halaman web
const output = document.getElementById("output");
output.innerHTML = `
  <p>${centimeter} cm is ${meter} meter</p>
  <p>${centimeter} cm is ${kilometer} kilometer</p>
  <p>${centimeter} cm is ${millimeter} millimeter</p>
`;
