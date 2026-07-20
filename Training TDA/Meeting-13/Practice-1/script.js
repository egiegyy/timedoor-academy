// declaration can run before this line
console.log("Declaration before created:", multiplyDeclaration(5, 2));

// Function declaration
function multiplyDeclaration(a, b) {
  return a * b;
}

// Function expression tidak bisa dipanggil sebelum dibuat
// Baris di bawah sengaja dikomentari agar program tidak error:
// console.log(multiplyExpression(5, 2));

// Function expression disimpan ke dalam variable
const multiplyExpression = function (a, b) {
  return a * b;
};

// Function expression aman dipanggil setelah dibuat
console.log("Expression after created:", multiplyExpression(5, 2));

// short hoisting note
console.log("Hoisting: function declaration bisa dipanggil sebelum dibuat.");
console.log("Function expression: sebaiknya dipanggil setelah variable function dibuat.");

// Menampilkan penjelasan ke halaman web
const output = document.getElementById("output");
output.innerHTML = `
  <p>Function declaration bisa dipanggil sebelum dibuat karena hoisting.</p>
  <p>Function expression sebaiknya dipanggil setelah dibuat karena disimpan di variable.</p>
  <p>Cek console untuk melihat hasilnya.</p>
`;

