// Random number from 0 until 9
let random = Math.floor(Math.random() * 10);

// Array of adjective words
let adjectives = [
  "pretty",
  "happy",
  "smart",
  "brave",
  "cool",
  "fast",
  "strong",
  "sweet",
  "bright",
  "silent"
];

// Array of noun words
let nouns = [
  "butterfly",
  "tiger",
  "dragon",
  "flower",
  "planet",
  "phoenix",
  "panda",
  "wizard",
  "castle",
  "ocean"
];

// Array of symbols for password
let symbols = ["!", "@", "#", "$", "%", "&", "*", "?", "+", "="];

// Variables to store generated username and password
let newUsername = "";
let newPassword = "";

// Function to make the first letter uppercase
function capitalize(word) {
  // Take first letter, make it uppercase, then add the rest of the word
  return word.charAt(0).toUpperCase() + word.slice(1);
}

// Function to show result on the website
function showResult(message) {
  // Get output element from HTML
  let output = document.getElementById("output");

  // Change text in the output element
  output.textContent = message;
}

// Function to generate username or password
function generate(option) {
  // Make new random index every time the function is called
  random = Math.floor(Math.random() * 10);

  // If option is 1, generate username
  if (Number(option) === 1) {
    // Username rule: adjective word + noun word
    newUsername = adjectives[random] + nouns[random];

    // Show result in console, alert, and HTML
    console.log("Generated Username:", newUsername);
    alert("Generated Username: " + newUsername);
    showResult("Generated Username: " + newUsername);
  } else if (Number(option) === 2) {
    // random password
    let capitalAdjective = capitalize(adjectives[random]);
    let randomNumber = random;
    let randomSymbol = symbols[random];

    // Save generated password to variable
    newPassword = capitalAdjective + nouns[random] + randomNumber + randomSymbol;

    // Show result in console, alert, and HTML
    console.log("Generated Password:", newPassword);
    alert("Generated Password: " + newPassword);
    showResult("Generated Password: " + newPassword);
  }
}

// Variable for user choice from prompt
let userOption;

// Ask user until the answer is 1 or 2
// 1 means generate username, 2 means generate password
do {
  userOption = prompt("Choose option:\n1. Generate Username\n2. Generate Password");
} while (userOption !== "1" && userOption !== "2");

// If the input is valid, call generate function
// Number() changes prompt string into number
if (userOption === "1" || userOption === "2") {
  generate(Number(userOption));
}

