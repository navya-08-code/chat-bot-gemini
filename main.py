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

# Premium Custom CSS for professional glassmorphism theme and modern styling
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;800&display=swap');
    
    /* Apply modern typography across the entire app */
    html, body, [class*="css"], .stMarkdown, p, div, label {
        font-family: 'Outfit', sans-serif !important;
    }
    
    /* Dark Radial Background Gradient */
    .stApp {
        background: radial-gradient(circle at 50% 50%, #15141b 0%, #08080b 100%) !important;
    }
    
    /* Sleek Gold Accent Header Container */
    .header-container {
        text-align: center;
        padding: 2.5rem 1.5rem;
        margin-bottom: 2.5rem;
        background: linear-gradient(135deg, rgba(255, 184, 0, 0.06) 0%, rgba(255, 159, 0, 0.02) 100%);
        border: 1px solid rgba(255, 184, 0, 0.15);
        border-radius: 24px;
        backdrop-filter: blur(12px);
        box-shadow: 0 10px 40px 0 rgba(0, 0, 0, 0.5);
    }
    
    .logo-container {
        font-size: 3.5rem;
        margin-bottom: 0.5rem;
        animation: pulse 2.5s infinite alternate;
    }
    
    .main-title {
        font-size: 2.8rem !important;
        font-weight: 800 !important;
        background: linear-gradient(90deg, #FFB800 0%, #FF8A00 50%, #FF5C00 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-top: 0 !important;
        margin-bottom: 0.3rem !important;
        letter-spacing: -0.5px;
    }
    
    .subtitle {
        color: #9CA3AF;
        font-size: 1.05rem;
        font-weight: 400;
        letter-spacing: 1px;
        text-transform: uppercase;
        margin-bottom: 0;
    }
    
    /* Custom Chat Message Cards */
    .stChatMessage {
        background-color: rgba(30, 30, 38, 0.35) !important;
        border: 1px solid rgba(255, 255, 255, 0.04) !important;
        border-radius: 16px !important;
        padding: 1.25rem !important;
        margin-bottom: 1.1rem !important;
        backdrop-filter: blur(10px) !important;
        box-shadow: 0 4px 20px 0 rgba(0, 0, 0, 0.15) !important;
        transition: transform 0.25s ease, border-color 0.25s ease, box-shadow 0.25s ease !important;
    }
    
    .stChatMessage:hover {
        transform: translateY(-2px);
        border-color: rgba(255, 184, 0, 0.25) !important;
        box-shadow: 0 8px 25px 0 rgba(255, 184, 0, 0.05) !important;
    }
    
    /* Customise Avatars and Colors */
    [data-testid="chatAvatarIcon-user"] {
        background-color: #FFB800 !important;
        color: #000000 !important;
    }
    
    [data-testid="chatAvatarIcon-assistant"] {
        background: linear-gradient(135deg, #FFB800 0%, #FF5C00 100%) !important;
    }
    
    /* Sleek Chat Input Container */
    .stChatInputContainer {
        border-radius: 35px !important;
        border: 1px solid rgba(255, 184, 0, 0.25) !important;
        background-color: rgba(22, 22, 28, 0.85) !important;
        box-shadow: 0 8px 30px rgba(0, 0, 0, 0.3) !important;
        transition: all 0.3s ease !important;
    }
    
    .stChatInputContainer:focus-within {
        border-color: #FFB800 !important;
        box-shadow: 0 8px 35px rgba(255, 184, 0, 0.15) !important;
    }
    
    /* Hide default Streamlit aesthetic banners for an bespoke feel */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    @keyframes pulse {
        0% { transform: scale(1); }
        100% { transform: scale(1.05); }
    }
</style>
""", unsafe_allow_html=True)

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

# Display the bespoke Royal Gold header
st.markdown("""
<div class="header-container">
    <div class="logo-container">🐯</div>
    <div class="main-title">Tipu AI</div>
    <div class="subtitle">The Royal Intelligence Engine</div>
</div>
""", unsafe_allow_html=True)

# Render conversation history inside premium glassmorphism chat blocks
for message in st.session_state.chat_session.history:
    with st.chat_message(translate_role_for_streamlit(message.role)):
        st.markdown(message.parts[0].text)

# Input prompt from user
user_prompt = st.chat_input("Ask Tipu AI...")
if user_prompt:
    # Render user message
    st.chat_message("user").markdown(user_prompt)

    # Fetch response from Tipu AI (Gemini 2.5 Flash backend)
    response = st.session_state.chat_session.send_message(user_prompt)

    # Render Assistant's response
    with st.chat_message("assistant"):
        st.markdown(response.text)
