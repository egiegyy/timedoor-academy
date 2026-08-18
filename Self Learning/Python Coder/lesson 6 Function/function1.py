def calculate_average():  # Deklarasi fungsi calculate_average
    scores = [70, 85, 90, 65, 80]  # List berisi nilai-nilai ujian
    total = 0  # Inisialisasi variabel total nilai awal (0)
    for score in scores:  # Loop untuk tiap nilai di dalam list
        total += score  # Tambahkan setiap nilai ke variabel total
    average = total / len(scores)  # Hitung rata-rata (total / jumlah data)
    if average >= 70:  # Jika rata-rata 70 atau lebih
        status = "Pass"  # Set status lulus
    else:  # Jika rata-rata di bawah 70
        status = "Fail"  # Set status tidak lulus
    print("Average score: ", average)  # Cetak nilai rata-rata
    print("Pass status: ", status)  # Cetak status kelulusan

print("Exam Score Average Calculator")  # Cetak judul program
calculate_average()  # Panggil dan jalankan fungsi calculate_average