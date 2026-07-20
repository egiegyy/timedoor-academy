// Array berisi 5 film terakhir yang ditonton
let watchedMovies = [
  "Inside Out 2",
  "The Wild Robot",
  "Kung Fu Panda 4",
  "Dune: Part Two",
  "Moana 2"
];

// Menampilkan array ke console
console.log("5 film terakhir yang ditonton:", watchedMovies);

// Menampilkan list film ke halaman web
const output = document.getElementById("output");
output.innerHTML = watchedMovies.map((movie) => `<li>${movie}</li>`).join("");
