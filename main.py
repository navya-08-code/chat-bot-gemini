import os
import streamlit as st
from dotenv import load_dotenv
import google.generativeai as gen_ai

# Load environment variables
load_dotenv()

# Configure Streamlit page settings
st.set_page_config(
    page_title="Chat with Gemini",
    page_icon=":brain:",
    layout="centered",
)

# Fetch Google API Key
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Configure the generative model using gemini-2.5-flash (which works perfectly on the free tier)
gen_ai.configure(api_key=GOOGLE_API_KEY)
model = gen_ai.GenerativeModel('gemini-2.5-flash')

# Helper function to map standard model roles to Streamlit avatar terminology
def translate_role_for_streamlit(user_role):
    if user_role == "model":
        return "assistant"
    else:
        return user_role

# Initialize chat session in Streamlit's session state if not already present
if "chat_session" not in st.session_state:
    st.session_state.chat_session = model.start_chat(history=[])

# Display the chatbot's title on the page
st.title("🤖 Gemini 2.5 Flash - ChatBot")

# Render conversation history inside native Streamlit chat blocks
for message in st.session_state.chat_session.history:
    with st.chat_message(translate_role_for_streamlit(message.role)):
        st.markdown(message.parts[0].text)

# Input prompt from user
user_prompt = st.chat_input("Ask Gemini...")
if user_prompt:
    # Render user message
    st.chat_message("user").markdown(user_prompt)

    # Fetch response from Gemini
    response = st.session_state.chat_session.send_message(user_prompt)

    # Render Assistant's response
    with st.chat_message("assistant"):
        st.markdown(response.text)
