// Function menerima parameter name, country, dan career
function greeting(name, country, career) {
  // Membuat pesan pendek dan pesan lengkap
  let shortMessage = `Hello ${name}`;
  let fullMessage = `Hello, my name is ${name} from ${country} and I want to be a ${career}`;

  // Menampilkan pesan menggunakan alert
  alert(shortMessage);
  alert(fullMessage);

  // Menampilkan pesan ke console
  console.log(shortMessage);
  console.log(fullMessage);

  // document.write akan mengganti isi halaman dengan teks baru
  document.write(`<h1>${shortMessage}</h1><p>${fullMessage}</p>`);
}

// Pesan awal saat halaman dibuka
console.log("Klik salah satu tombol nama untuk menjalankan function greeting.");
