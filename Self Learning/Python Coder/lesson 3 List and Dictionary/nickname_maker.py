import random  # Impor modul acak

first_names = ["Super", "Mighty", "Fantastic", "Electric", "Swift", "Newbie"] # List kata depan
last_names = ["Dragon", "Warrior", "Ninja", "Wizard", "Champion", "Master"] # List kata belakang

first_name = random.choice(first_names) # Pilih acak nama depan
last_name = random.choice(last_names) # Pilih acak nama belakang

random_number = random.randint(100, 1000) # Buat angka acak (100-1000)

nickname = first_name + last_name + str(random_number) # Gabungkan jadi satu teks
print(nickname)  # Tampilkan hasil nickname