while True:  # Mulai perulangan tanpa henti (loop berulang terus)
    print("Body mass index (BMI)")  # Cetak judul program
    weight = float(input("How much do you weight in Kilograms?"))  # Input berat badan (kg) ke float
    height = float(input("How tall are you in meters ?"))  # Input tinggi badan (m) ke float
    BMI = weight / (height * height)  # Hitung rumus BMI (berat / tinggi^2)

    if BMI < 18.5:  # Jika BMI di bawah 18.5
        print("Less Weight")  # Cetak: Berat badan kurang
    elif 18.5 < BMI < 24.9:  # Jika BMI antara 18.5 sampai 24.9
        print("Normal Weight")  # Cetak: Berat badan normal
    elif 25 < BMI < 29.9:  # Jika BMI antara 25 sampai 29.9
        print("Over Weight")  # Cetak: Kelebihan berat badan
    else:  # Jika BMI 30 ke atas (atau berada di selisih interval)
        print("Obesity")  # Cetak: Obesitas

    print("Your BMI = " + str(BMI))  # Tampilkan nilai BMI yang didapat
    ans = input("Do you want to input again? y/n -->")  # Tanya user apakah ingin mengulang

    if ans == "n":  # Jika user mengetik 'n'
        break  # Hentikan dan keluar dari perulangan