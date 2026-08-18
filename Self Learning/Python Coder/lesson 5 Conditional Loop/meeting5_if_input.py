temperature = float(input("Enter the current temperature (in degrees Celsius): "))  # Ambil input suhu dari user & ubah ke float (desimal)

if temperature < 0:  # Jika suhu di bawah 0°C
    print("The current temperature is extremely cold.")  # Cetak: Sangat dingin
elif temperature < 10:  # Jika suhu antara 0°C sampai 9.9°C
    print("The current temperature is quite cold.")  # Cetak: Cukup dingin
elif temperature < 25:  # Jika suhu antara 10°C sampai 24.9°C
    print("The current temperature is comfortable.")  # Cetak: Nyaman / Sejuk
else:  # Jika suhu 25°C ke atas
    print("The current temperature is quite hot.")  # Cetak: Cukup panas