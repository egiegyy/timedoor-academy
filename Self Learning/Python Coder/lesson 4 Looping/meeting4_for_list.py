city_list = ["New York City", "Los Angeles", "Chicago", "Houston", 
"Phoenix", "Philadelphia", "San Antonio", "San Diego", "Dallas", "San Jose"]  # Buat list berisi 10 nama kota

for i in city_list:  # Cetak semua kota satu per satu (elemen langsung)
    print(i) 
    
for i in range(4):  # Cetak 4 kota pertama (indeks 0 sampai 3)
    print(city_list[i])
    
for i in range(1, 10, 2):  # Cetak kota pada indeks ganjil (1, 3, 5, 7, 9)
    print(city_list[i])