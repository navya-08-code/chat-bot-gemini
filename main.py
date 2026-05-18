import os
import streamlit as st
from dotenv import load_dotenv
import google.generativeai as gen_ai

# Load environment variables
load_dotenv()

# Configure Streamlit page settings with a custom tab title and icon
st.set_page_config(
    page_title="Tipu AI - The Royal Intelligence Engine",
    page_icon="🐯",
    layout="centered",
)

# Fetch Google API Key
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Configure the generative model using gemini-2.5-flash
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

# Display the bespoke native Streamlit header
st.title("🐯 Tipu AI")
st.subheader("The Royal Intelligence Engine")
st.caption("Powered by Gemini 2.5 Flash | Secure Session Active")
st.divider()

# Render conversation history inside native Streamlit chat blocks
for message in st.session_state.chat_session.history:
    role = translate_role_for_streamlit(message.role)
    avatar = "🐯" if role == "assistant" else "👤"
    with st.chat_message(role, avatar=avatar):
        st.markdown(message.parts[0].text)

# Input prompt from user
user_prompt = st.chat_input("Ask Tipu AI...")
if user_prompt:
    # Render user message with human avatar
    with st.chat_message("user", avatar="👤"):
        st.markdown(user_prompt)

    # Fetch response from Tipu AI (Gemini 2.5 Flash backend)
    response = st.session_state.chat_session.send_message(user_prompt)

    # Render Assistant's response with Tiger avatar
    with st.chat_message("assistant", avatar="🐯"):
        st.markdown(response.text)
