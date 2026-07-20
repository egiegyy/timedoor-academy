// Array questions berisi daftar pertanyaan trivia negara
let questions = [
  "What is the capital city of Japan?",
  "Which country has the Eiffel Tower?",
  "What country has a maple leaf on its flag?",
  "What is the capital city of Indonesia?",
  "Which country is famous for the Great Wall?"
];

// Array answers berisi jawaban yang sesuai dengan urutan questions
let answers = ["tokyo", "france", "canada", "jakarta", "china"];

// Function ini menjalankan quiz
function startQuiz() {
  let score = 0;

  // Loop untuk menanyakan semua pertanyaan
  for (let i = 0; i < questions.length; i++) {
    let userAnswer = prompt(questions[i]);

    // Jika user menekan Cancel, jawaban dianggap kosong
    if (userAnswer === null) {
      userAnswer = "";
    }

    // Jawaban dibuat lowercase agar lebih mudah dibandingkan
    if (userAnswer.toLowerCase() === answers[i]) {
      score += 20;
      console.log(`Question ${i + 1}: correct`);
    } else {
      console.log(`Question ${i + 1}: wrong. Correct answer: ${answers[i]}`);
    }
  }

  // Menampilkan score akhir ke console, alert, dan halaman web
  console.log("Final score:", score);
  alert(`Your final score is ${score}`);
  document.getElementById("output").textContent = `Final score: ${score}`;
}

// Pesan awal saat halaman dibuka
console.log("Country Trivia siap dimainkan. Klik tombol Start Country Trivia.");
