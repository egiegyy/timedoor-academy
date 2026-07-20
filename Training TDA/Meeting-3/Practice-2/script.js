// Nilai awal setiap variable
let a = 17;
let b = 20;
let c = 3;
let d = 1000;
let e = 4;

// Mengubah nilai menggunakan assignment operator
a += 3;
b -= 5;
c *= 4;
d /= 10;
e %= 3;

// Menampilkan hasil ke console
console.log("a setelah += 3:", a);
console.log("b setelah -= 5:", b);
console.log("c setelah *= 4:", c);
console.log("d setelah /= 10:", d);
console.log("e setelah %= 3:", e);

// Menampilkan hasil ke halaman web
const output = document.getElementById("output");
output.textContent = `Hasil: a=${a}, b=${b}, c=${c}, d=${d}, e=${e}`;
