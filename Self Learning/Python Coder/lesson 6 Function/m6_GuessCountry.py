def check_guess():
    global score  # Izinkan ubah nilai score di luar fungsi
    still_guessing = True  # Status user masih menebak
    attempt = 0  # Hitungan jumlah percobaan (max 3)

    while still_guessing and attempt < 3:  # Loop sampai benar atau max 3x coba
        guess = input("Guess :")  # Ambil input tebakan
        if guess.lower() == answer.lower():  # Cek jawaban (abaikan huruf besar/kecil)
            print("Correct Answer!")  # Pesan jika benar
            score += 1  # Tambah 1 poin
            still_guessing = False  # Hentikan loop
        else:
            if attempt < 2:  # Jika belum percobaan terakhir
                print("Wrong Answer!")  # Pesan jika salah
            attempt += 1  # Tambah hitungan percobaan


score = 0  # Inisialisasi skor awal
print("Guess the Country!")

print("By Size, what is the largest country in the world?")
answer = "Russia"  # Kunci jawaban 1
check_guess()  # Jalankan pengecekan

print("Which country has a unicorn as its national animal?")
answer = "Scotland"  # Kunci jawaban 2
check_guess()  # Jalankan pengecekan

print("In which country would you find the currency Baht?")
answer = "Thailand"  # Kunci jawaban 3
check_guess()  # Jalankan pengecekan

print("Your final score:", score)  # Cetak total skor akhir

