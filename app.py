import streamlit as st
import openai

# Load API key securely from Streamlit Secrets
openai.api_key = st.secrets["OPENAI_API_KEY"]

# Streamlit UI
st.title("🚀 AI Chatbot - Powered by GPT-3.5 Turbo")

st.write("Ask me anything, and I'll do my best to assist you!")

# User input
user_input = st.text_input("You:", "")

if user_input:
    try:
        # Generate response from GPT-3.5 Turbo
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "system", "content": "You are a helpful AI assistant."},
                      {"role": "user", "content": user_input}]
        )

        # Display response
        bot_reply = response["choices"][0]["message"]["content"]
        st.write(f"**Bot:** {bot_reply}")

    except Exception as e:
        st.error(f"Error: {e}")
