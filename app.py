import time
from datetime import datetime
from openai import OpenAI
import streamlit as st

# 1. Page Configuration & UI Headers
st.set_page_config(page_title="AI Virtual Assistant", page_icon="🤖", layout="centered")

st.title("🤖 AI Virtual Assistant")
st.write("Welcome! Ask me a question about programming, AI, or general topics.")

# 2. Fetch API Keys Securely from Platform Secrets Dashboard Manager
# Replaces 'os.getenv' to align with online cloud deployment rules
if "OPENAI_API_KEY" in st.secrets:
    client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
else:
    st.error("Missing Setup Configuration: Please paste 'OPENAI_API_KEY = \"your_key\"' into your platform's Secrets settings panel.")
    client = None

# Helper function to invoke OpenAI Completions API
def get_ai_response(user_query: str) -> str:
    if not client:
        return "API connection offline. Valid API Key missing."
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini", # Fast, high-accuracy default cloud model
            messages=[
                {"role": "system", "content": "You are a helpful AI Virtual Assistant specializing in programming and general knowledge."},
                {"role": "user", "content": user_query}
            ],
            max_tokens=150
        )
        return response.choices.message.content.strip()
    except Exception as e:
        return f"Error contacting AI API backend: {str(e)}"

# 3. Handle Persistent Chat History State Variables
if "messages" not in st.session_state:
    st.session_state.messages = []

# Redraw interface chat logs on UI frame update refreshes
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# 4. Process Live Interactive User Input Strings
if user_message := st.chat_input("Type your message here..."):
    
    # Render user prompt chat bubble immediately
    with st.chat_message("user"):
        st.write(user_message)
    
    # Store inside internal dictionary history memory log arrays
    st.session_state.messages.append({"role": "user", "content": user_message})

    # Prepare lower cased parsing checks for immediate local evaluation triggers
    message_lower = user_message.lower()

    # --- Match Fast Local Keyword Strings First ---
    if "hello" in message_lower or "hi" in message_lower:
        reply = "Hello! How can I help you today?"

    elif "how are you" in message_lower:
        reply = "I am doing great. Thank you for asking."

    elif "your name" in message_lower:
        reply = "I am your AI Virtual Assistant."

    elif "python" in message_lower:
        reply = "Python is a powerful programming language used in AI, automation, data science, and web development."

    elif "html" in message_lower:
        reply = "HTML is the standard language used to create web pages."

    elif "css" in message_lower:
        reply = "CSS is used to style and design websites."

    elif "javascript" in message_lower:
        reply = "JavaScript adds interactivity and dynamic behavior to websites."

    elif "flask" in message_lower:
        reply = "Flask is a lightweight Python framework used for web applications."

    elif "ai" in message_lower:
        reply = "Artificial Intelligence allows machines to learn, reason, and solve problems."

    elif "time" in message_lower:
        reply = f"Current time is {datetime.now().strftime('%I:%M %p')}"

    elif "date" in message_lower:
        reply = f"Today's date is {datetime.now().strftime('%d-%m-%Y')}"

    # --- Fallback directly to live cloud OpenAI endpoints for all general inquiries ---
    else:
        with st.spinner("Assistant is thinking..."):
            reply = get_ai_response(user_message)

    # Short output buffer simulation for realistic pacing flow
    time.sleep(0.3)

    # Render generated AI reply inside interface chat viewport
    with st.chat_message("assistant"):
        st.write(reply)

    # Append assistant's answer block back to global historical message session arrays
    st.session_state.messages.append({"role": "assistant", "content": reply})
