fruits = ["apple", "banana", "cherry"] # indeks dimulai dari 0
print(fruits)

print(len(fruits)) # len untuk menghitung jumlah item dalam list
print(type(fruits)) # type untuk mengetahui tipe data variabel

# print berdasarkan indeks
print(fruits[0]) # urutan 1 yaitu apple
print(fruits[1]) # urutan 2 yaitu banana
print(fruits[-1]) # -1 yaitu cherry (indeks negatif dimulai dari belakang)

# list campuran
list1 = ["abc", 34, True, 40, "male"]
print(list1)

# mengubah item dalam list
taste= ["chocolate", "strawberry", "vanilla", "peanut"]
print("Before : ", taste)

#Change index number 1
taste[1] = "banana"
print("After : ", taste)