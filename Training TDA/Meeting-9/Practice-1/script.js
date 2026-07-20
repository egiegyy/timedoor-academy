// Variable ini dipakai untuk mengumpulkan semua teks output
let outputText = "";

// Loop pertama membuat platform dari nomor 1 sampai 3
for (let platform = 1; platform <= 3; platform++) {
  let platformText = `Platform created ${platform}`;

  // Tampilkan platform ke console
  console.log(platformText);
  outputText += platformText + "<br>";

  // Nested loop membuat carrot 1 sampai 2 di setiap platform
  for (let carrot = 1; carrot <= 2; carrot++) {
    let carrotText = `--- Carrot ${carrot}`;

    // Tampilkan carrot ke console
    console.log(carrotText);
    outputText += carrotText + "<br>";
  }

  // Baris kosong agar output di console lebih mudah dibaca
  console.log("");
  outputText += "<br>";
}

// Menampilkan hasil loop ke halaman web
const output = document.getElementById("output");
output.innerHTML = outputText;
