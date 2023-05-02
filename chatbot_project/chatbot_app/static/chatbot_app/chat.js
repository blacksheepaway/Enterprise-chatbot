function displayMessage(text, sender = 'user') {
    const chatWindow = document.getElementById('chat-window');
    const messageElem = document.createElement('div');
    messageElem.classList.add('message');
    messageElem.classList.add(sender);
    messageElem.textContent = text;
    chatWindow.appendChild(messageElem);
}

function clearChat() {
    const chatWindow = document.getElementById('chat-window');
    chatWindow.innerHTML = '';
}

document.addEventListener('DOMContentLoaded', () => {
    const chatForm = document.getElementById('chat-form');
    chatForm.addEventListener('submit', async (event) => {
        event.preventDefault();
        const chatInput = document.getElementById('chat-input');
        const message = chatInput.value;
        chatInput.value = '';

        displayMessage(message);

        const response = await fetch('/message/', {
            method: 'POST',
            body: new URLSearchParams({user_message: message}),
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
                'X-CSRFToken': document.getElementsByName('csrfmiddlewaretoken')[0].value,
            },
        });

        if (response.ok) {
            const data = await response.json();
            displayMessage(data.message, 'bot');
        } else {
            console.error('Error sending message:', response.statusText);
        }
    });

    const clearChatBtn = document.getElementById('clear-chat-btn');
    clearChatBtn.addEventListener('click', clearChat);
});
