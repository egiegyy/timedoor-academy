// Arrow function bernama sum untuk menjumlahkan dua parameter
const sum = (a, b) => {
  return a + b;
};

// Menampilkan hasil pemanggilan function ke console
console.log("sum(10, 20):", sum(10, 20));
console.log("sum(99, 1):", sum(99, 1));

// Menampilkan hasil ke halaman web
const output = document.getElementById("output");
output.innerHTML = `
  <p>sum(10, 20) = ${sum(10, 20)}</p>
  <p>sum(99, 1) = ${sum(99, 1)}</p>
`;
