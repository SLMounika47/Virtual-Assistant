import streamlit as st
from datetime import datetime
import time

# 1. Set up the webpage title and look
st.set_page_config(page_title="AI Virtual Assistant", page_icon="🤖")
st.title("🤖 AI Virtual Assistant")
st.write("Welcome! Ask me a question about programming, AI, or general topics.")

# 2. Keep the chat history on screen so it does not disappear
if "messages" not in st.session_state:
    st.session_state.messages = []

# 3. Show all previous messages every time the screen updates
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 4. Wait for the user to type a message
if user_input := st.chat_input("Type your message here..."):
    
    # Show what the user typed in the chat
    with st.chat_message("user"):
        st.markdown(user_input)
    
    # Save user message to history
    st.session_state.messages.append({"role": "user", "content": user_input})

    # 5. Assistant reply logic (matching your original features)
    message = user_input.lower()
    
    if "hello" in message or "hi" in message:
        reply = "Hello! How can I help you today?"
    elif "how are you" in message:
        reply = "I am doing great. Thank you for asking."
    elif "your name" in message:
        reply = "I am your AI Virtual Assistant."
    elif "python" in message:
        reply = "Python is a powerful programming language used in AI, automation, data science, and web development."
    elif "html" in message:
        reply = "HTML is the standard language used to create web pages."
    elif "css" in message:
        reply = "CSS is used to style and design websites."
    elif "javascript" in message:
        reply = "JavaScript adds interactivity and dynamic behavior to websites."
    elif "flask" in message:
        reply = "Flask is a lightweight Python framework used for web applications."
    elif "ai" in message:
        reply = "Artificial Intelligence allows machines to learn, reason, and solve problems."
    elif "time" in message:
        reply = f"Current time is {datetime.now().strftime('%I:%M %p')}"
    elif "date" in message:
        reply = f"Today's date is {datetime.now().strftime('%d-%m-%Y')}"
    else:
        reply = f"You asked: '{user_input}'. I am a basic AI assistant. To answer everything like ChatGPT, I need an AI API integration."

    # Simulate a realistic typing delay
    time.sleep(1.5)

    # Show the assistant reply in the chat
    with st.chat_message("assistant"):
        st.markdown(reply)
        
    # Save assistant reply to history
    st.session_state.messages.append({"role": "assistant", "content": reply})
