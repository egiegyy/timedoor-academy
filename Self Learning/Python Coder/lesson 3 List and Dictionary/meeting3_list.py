fruits = ["Apple", "Mango", "Banana", "Orange"]

print("before : ", fruits) # isi sebelum ditambahkan item baru

# menambahkan item dalam list
fruits.append("Grapes") # append() untuk menambahkan item di akhir list
fruits.insert(2, "Pineapple")  # insert() untuk menambahkan item di indeks tertentu

print("after : ", fruits) # isi setelah ditambahkan item baru

# menghapus item dalam list
fruits.remove("Apple")
fruits.remove("Orange")

print("after remove", fruits)

#sorting list
fruits.sort() # sort() untuk mengurutkan item dalam list secara ascending
print("after remove and sort", fruits)