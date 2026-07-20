// Membuat angka random dari 1 sampai 10
let firstNumber = Math.floor(Math.random() * 10) + 1;
let secondNumber = Math.floor(Math.random() * 10) + 1;

// Operator bisa diganti menjadi +, -, *, atau /
let operator = "+";
let result;

// Menghitung berdasarkan operator menggunakan switch statement
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
  default:
    result = "Operator tidak dikenal";
}

// Menampilkan challenge dan hasil ke console
console.log("Angka pertama:", firstNumber);
console.log("Angka kedua:", secondNumber);
console.log("Operator:", operator);
console.log("Hasil:", result);

// Menampilkan hasil ke halaman web
const output = document.getElementById("output");
output.textContent = `${firstNumber} ${operator} ${secondNumber} = ${result}`;
