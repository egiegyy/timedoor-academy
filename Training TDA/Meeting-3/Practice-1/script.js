// Harga top up setiap pembelian
let topUpPrice = 50;

// Jumlah pembelian
let purchaseCount = 3;

// Diskon setiap pembelian
let discountPerPurchase = 2;

// Menghitung total sebelum diskon
let totalBeforeDiscount = topUpPrice * purchaseCount;

// Menghitung total diskon
let totalDiscount = discountPerPurchase * purchaseCount;

// Menghitung total akhir
let totalTopUp = totalBeforeDiscount - totalDiscount;

// Expected result: 144
console.log("Total top up:", totalTopUp);

// Menampilkan hasil ke halaman web
const output = document.getElementById("output");
output.textContent = `Total top up adalah $${totalTopUp}.`;
