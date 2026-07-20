// Array berisi kumpulan angka
let numbers = [10, 25, 99, 500, 1111, 72, 88];

// Function untuk mencari angka target di dalam array
function findNumber(arrayData, targetNumber) {
  // Loop mengecek setiap index array satu per satu
  for (let i = 0; i < arrayData.length; i++) {
    // Strict equality === memastikan nilai dan tipe data sama
    if (arrayData[i] === targetNumber) {
      return i;
    }
  }

  // Jika angka tidak ditemukan, function mengembalikan -1
  return -1;
}

// Memanggil function untuk mencari angka 1111
let foundIndex = findNumber(numbers, 1111);

// Menampilkan hasil ke console
console.log(`1111 is located at index ${foundIndex}`);

// Menampilkan hasil ke halaman web
const output = document.getElementById("output");
output.textContent = `1111 is located at index ${foundIndex}`;
