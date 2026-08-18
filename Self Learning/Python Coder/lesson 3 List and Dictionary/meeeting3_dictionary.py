# membuat dictionary song
song = {
    "title": "All Of Me",
    "singer": "John Legend",
    "release": 2013
}

# menambahkan key baru ke dictionary song
song.update({"genre" : "R&B/Soul"})
song["title"] = "We Loved It"

del song["singer"] # menghapus key singer dari dictionary song
print(song["title"]) # menampilkan value dari key title
print(song.get("release")) # menampilkan value dari key release
