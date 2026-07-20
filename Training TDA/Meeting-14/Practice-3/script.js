// Array berisi daftar tamu undangan
let guests = ["Kimberly", "Olivia", "Sophia", "Catriona", "Michele"];

// Mengambil elemen HTML untuk menampilkan label undangan
const output = document.getElementById("output");

// Variable untuk menyimpan HTML label undangan
let invitationLabels = "";

// forEach menjalankan function untuk setiap item di dalam array guests
// Arrow function membuat penulisan function menjadi lebih singkat
guests.forEach((guest) => {
  let label = `To : ${guest}`;

  // Menampilkan label ke console
  console.log(label);

  // Menambahkan label ke tampilan HTML
  invitationLabels += `<div class="label">${label}</div>`;
});

// Menampilkan semua label undangan ke halaman web
output.innerHTML = invitationLabels;
