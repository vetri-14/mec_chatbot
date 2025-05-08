// Get DOM elements
const userInput = document.getElementById('user-input');
const chatBox = document.getElementById('chat-box');

// Function to append message to chat window
function appendMessage(message, sender) {
  const messageDiv = document.createElement('div');
  messageDiv.classList.add(sender === 'user' ? 'user-message' : 'bot-message');
  messageDiv.innerText = message;
  chatBox.appendChild(messageDiv);
  chatBox.scrollTop = chatBox.scrollHeight; // Auto-scroll
}

// Function to speak bot replies using TTS
function speak(text) {
  const synth = window.speechSynthesis;
  const utterance = new SpeechSynthesisUtterance(text);
  utterance.lang = 'en-US';
  synth.speak(utterance);
}

// Function to send user message to backend
function sendMessage() {
  const message = userInput.value.trim();
  if (message === '') return;

  // Show user message
  appendMessage(message, 'user');
  userInput.value = '';

  // Fetch bot reply from backend
  fetch('/get-response', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ message: message })
  })
    .then(response => response.json())
    .then(data => {
      appendMessage(data.reply, 'bot');
      speak(data.reply); // Speak the bot's reply
    })
    .catch(error => {
      console.error('Error:', error);
      const errorMsg = "Oops! Something went wrong.";
      appendMessage(errorMsg, 'bot');
      speak(errorMsg);
    });
}

// Allow sending on Enter key
userInput.addEventListener('keypress', function (e) {
  if (e.key === 'Enter') {
    sendMessage();
  }
});
