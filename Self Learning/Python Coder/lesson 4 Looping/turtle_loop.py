import turtle  # Impor modul turtle

t = turtle.Pen() # Buat objek pena/turtle
t.shape("turtle") # Ubah bentuk penanda jadi kura-kura
t.pencolor("blue") # Set warna garis jadi biru
t.speed(1) # Set kecepatan 1 lambat, 10 cepat

for x in range(4): # Ulangi 4 kali untuk membuat 4 sisi
    t.forward(100) # Maju 100 piksel
    t.left(90) # Belok kiri 90 derajat

turtle.done() # Tetap membuka jendela grafis setelah selesai