import turtle  # Panggil library turtle

t = turtle.Pen()  # Buat objek pena/turtle
t.speed(10)  # Mengatur kecepatan gerakan (1 = paling lambat, 10 = cepat)
t.shape("turtle")  # Ubah bentuk penanda jadi kura-kura
t.pencolor("blue")  # Atur warna garis jadi biru

t.forward(50)  # Garis 1: Maju 50 piksel
t.left(90)  # Belok kiri 90 derajat

t.forward(50)  # Garis 2: Maju 50 piksel
t.left(90)  # Belok kiri 90 derajat

t.forward(50)  # Garis 3: Maju 50 piksel
t.left(90)  # Belok kiri 90 derajat

t.forward(50)  # Garis 4: Maju 50 piksel
t.left(90)  # Belok kiri (kembali ke arah awal)