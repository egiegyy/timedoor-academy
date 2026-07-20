// Function ini menjalankan calculator sederhana
function startCalculator() {
  // Meminta operator dari user
  let operator = prompt("Masukkan operator (+, -, *, /):");

  // Jika operator kosong atau tidak sesuai, tampilkan alert
  if (operator !== "+" && operator !== "-" && operator !== "*" && operator !== "/") {
    alert("no operator selected");
    console.log("no operator selected");
    return;
  }

  // Meminta angka pertama dan kedua dari user
  let firstInput = prompt("Masukkan angka pertama:");
  let secondInput = prompt("Masukkan angka kedua:");

  // Mengubah input string menjadi number
  let firstNumber = Number(firstInput);
  let secondNumber = Number(secondInput);

  // Validasi angka menggunakan isNaN
  if (isNaN(firstNumber) || isNaN(secondNumber)) {
    alert("Input harus berupa angka");
    console.log("Input tidak valid");
    return;
  }

  let result;

  // Menghitung hasil berdasarkan operator yang dipilih
  switch (operator) {
    case "+":
      result = firstNumber + secondNumber;
      break;
    case "-":
      result = firstNumber - secondNumber;
      break;
    case "*":
      result = firstNumber * secondNumber;
      break;
    case "/":
      result = firstNumber / secondNumber;
      break;
  }

  // Membuat teks hasil seperti contoh: 14 + 6 = 20
  let resultText = `${firstNumber} ${operator} ${secondNumber} = ${result}`;

  // Menampilkan hasil ke console, alert, dan halaman web
  console.log(resultText);
  alert(resultText);
  document.getElementById("output").textContent = resultText;
}

// Pesan awal saat halaman dibuka
console.log("Calculator siap digunakan. Klik tombol Start Calculator.");
