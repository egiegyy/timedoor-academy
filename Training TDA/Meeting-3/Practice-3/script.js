// Data diri Cobee
let name = "Cobee";
let age = 15;
let dreamJob = "Programmer";

// Membuat kalimat menggunakan template literal
let sentence = `My name is ${name}, ${age} years old and I want to be ${dreamJob} in the future.`;

// Menampilkan output ke console
console.log(sentence);

// Menampilkan output ke halaman web
const output = document.getElementById("output");
output.textContent = sentence;
