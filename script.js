function addMessage(message, className) {

    let chatBox =
        document.getElementById("chat-box");

    let div =
        document.createElement("div");

    div.className =
        "message " + className;

    div.innerText =
        message;

    chatBox.appendChild(div);

    chatBox.scrollTop =
        chatBox.scrollHeight;

    localStorage.setItem(
        "chatHistory",
        chatBox.innerHTML
    );
}

function showTyping() {

    let chatBox =
        document.getElementById("chat-box");

    let typing =
        document.createElement("div");

    typing.id = "typing";

    typing.className = "typing";

    typing.innerText =
        "Assistant is typing...";

    chatBox.appendChild(typing);
}

function removeTyping() {

    let typing =
        document.getElementById("typing");

    if (typing) {
        typing.remove();
    }
}

function speak(text) {

    let speech =
        new SpeechSynthesisUtterance(text);

    speech.lang = "en-US";

    window.speechSynthesis.speak(
        speech
    );
}

function sendMessage() {

    let input =
        document.getElementById("user-input");

    let message =
        input.value.trim();

    if (message === "")
        return;

    addMessage(
        "You: " + message,
        "user"
    );

    showTyping();

    fetch("/chat", {

        method: "POST",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify({
            message: message
        })
    })

        .then(response =>
            response.json()
        )

        .then(data => {

            removeTyping();

            addMessage(
                "Assistant: " +
                data.reply,
                "bot"
            );

            speak(data.reply);
        });

    input.value = "";
}

function fillQuestion(text) {

    document
        .getElementById("user-input")
        .value = text;
}

function clearChat() {

    document
        .getElementById("chat-box")
        .innerHTML = "";

    localStorage.removeItem(
        "chatHistory"
    );
}

window.onload = () => {

    let history =
        localStorage.getItem(
            "chatHistory"
        );

    if (history) {

        document
            .getElementById("chat-box")
            .innerHTML = history;
    }

    speak(
        "Welcome to AI Virtual Assistant"
    );
};

document
    .getElementById("theme-btn")
    .addEventListener(
        "click",
        () => {

            document.body.classList
                .toggle("dark-mode");

        });

document
    .getElementById("user-input")
    .addEventListener(
        "keypress",
        function (event) {

            if (event.key === "Enter") {

                sendMessage();

            }

        });

const SpeechRecognition =
    window.SpeechRecognition ||
    window.webkitSpeechRecognition;

if (SpeechRecognition) {

    const recognition =
        new SpeechRecognition();

    recognition.lang =
        "en-US";

    document
        .getElementById("mic-btn")
        .addEventListener(
            "click",
            () => {

                recognition.start();

            });

    recognition.onresult =
        (event) => {

            let transcript =
                event.results[0][0]
                    .transcript;

            document
                .getElementById(
                    "user-input"
                )
                .value =
                transcript;

            sendMessage();

        };

}