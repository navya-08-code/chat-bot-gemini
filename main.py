import os
import streamlit as st
from dotenv import load_dotenv
import google.generativeai as gen_ai

# Load environment variables
load_dotenv()

# Configure Streamlit page settings
st.set_page_config(
    page_title="Tipu - ChatBot",
    page_icon="🤖",
    layout="centered",
)

# Fetch Google API Key
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Configure the generative model using gemini-2.5-flash
if GOOGLE_API_KEY:
    gen_ai.configure(api_key=GOOGLE_API_KEY)
    # Using gemini-2.5-flash as the main model
    model = gen_ai.GenerativeModel('gemini-2.5-flash')
else:
    model = None

# Custom CSS for Premium Design & Aesthetic Upgrade
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700&display=swap');
    
    /* Apply global font family and background */
    .stApp {
        font-family: 'Plus Jakarta Sans', sans-serif;
        background: linear-gradient(135deg, #0e1117 0%, #161a25 50%, #0d0f14 100%) !important;
        color: #e2e8f0;
    }
    
    /* Header style */
    .chat-header {
        text-align: center;
        margin-top: -2rem;
        margin-bottom: 2rem;
        animation: fadeInDown 0.8s ease-out;
    }
    
    .chat-header h1 {
        font-size: 2.8rem;
        font-weight: 700;
        background: linear-gradient(90deg, #38bdf8, #818cf8, #a78bfa);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.2rem;
        letter-spacing: -0.05em;
        text-shadow: 0px 4px 20px rgba(99, 102, 241, 0.15);
    }
    
    .chat-header p {
        font-size: 1rem;
        color: #94a3b8;
        font-weight: 400;
    }
    
    /* Chat message container styling */
    [data-testid="stChatMessage"] {
        background-color: rgba(30, 41, 59, 0.4) !important;
        border: 1px solid rgba(255, 255, 255, 0.05) !important;
        border-radius: 16px !important;
        padding: 1.25rem !important;
        margin-bottom: 1rem !important;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06) !important;
        backdrop-filter: blur(10px) !important;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
        animation: fadeInUp 0.5s ease-out;
    }
    
    [data-testid="stChatMessage"]:hover {
        transform: translateY(-2px) !important;
        border-color: rgba(99, 102, 241, 0.2) !important;
        box-shadow: 0 10px 15px -3px rgba(99, 102, 241, 0.05), 0 4px 6px -2px rgba(99, 102, 241, 0.05) !important;
    }
    
    /* Custom Styling for different roles */
    [data-testid="stChatMessageContent"] {
        font-size: 0.975rem !important;
        line-height: 1.6 !important;
        color: #f1f5f9 !important;
    }
    
    /* Avatar layout adjustments */
    [data-testid="stChatMessage"] [data-testid="stAvatar"] {
        background: linear-gradient(135deg, #4f46e5, #06b6d4) !important;
        border-radius: 10px !important;
    }
    
    /* Make assistant messages slightly distinct */
    div[data-testid="stChatMessage"]:has(img[src*="assistant"]) {
        background-color: rgba(17, 24, 39, 0.6) !important;
        border-left: 3px solid #6366f1 !important;
    }
    
    /* Input Container glassmorphism */
    div[data-testid="stChatInput"] {
        border-radius: 16px !important;
        border: 1px solid rgba(255, 255, 255, 0.08) !important;
        background-color: rgba(15, 23, 42, 0.6) !important;
        box-shadow: 0 -4px 30px rgba(0, 0, 0, 0.2) !important;
        backdrop-filter: blur(12px) !important;
        padding: 0.4rem !important;
    }
    
    div[data-testid="stChatInput"] textarea {
        color: #f8fafc !important;
        background-color: transparent !important;
        font-family: 'Plus Jakarta Sans', sans-serif !important;
    }
    
    /* Streamlit error card customization */
    div[data-testid="stNotification"] {
        border-radius: 12px !important;
        border: 1px solid rgba(239, 68, 68, 0.2) !important;
        background-color: rgba(239, 68, 68, 0.05) !important;
        backdrop-filter: blur(8px) !important;
        color: #fca5a5 !important;
    }
    
    /* Animations */
    @keyframes fadeInUp {
        from {
            opacity: 0;
            transform: translateY(12px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    @keyframes fadeInDown {
        from {
            opacity: 0;
            transform: translateY(-12px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    /* Hide default Streamlit decoration elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    </style>
    """,
    unsafe_allow_html=True
)

# Header Section
st.markdown(
    """
    <div class="chat-header">
        <h1>🤖 Tipu Chatbot</h1>
        <p>Powered by Google Gemini 2.5 Flash • Premium Experience</p>
    </div>
    """,
    unsafe_allow_html=True
)

# Helper function to map standard model roles to Streamlit avatar terminology
def translate_role_for_streamlit(user_role):
    if user_role == "model":
        return "assistant"
    else:
        return user_role

# Initialize chat session in Streamlit's session state if not already present
if "chat_session" not in st.session_state:
    if model:
        st.session_state.chat_session = model.start_chat(history=[])
    else:
        st.session_state.chat_session = None

# Show warning if no API key is set
if not GOOGLE_API_KEY:
    st.error("⚠️ GOOGLE_API_KEY is not set. Please set it in your `.env` file.")
else:
    # Render conversation history inside native Streamlit chat blocks
    if st.session_state.chat_session:
        for message in st.session_state.chat_session.history:
            with st.chat_message(translate_role_for_streamlit(message.role)):
                st.markdown(message.parts[0].text)

    # Input prompt from user
    user_prompt = st.chat_input("Ask Tipu...")
    if user_prompt:
        # Render user message
        st.chat_message("user").markdown(user_prompt)

        # Fetch response from Gemini
        if st.session_state.chat_session:
            try:
                with st.spinner("Tipu is thinking..."):
                    response = st.session_state.chat_session.send_message(user_prompt)
                
                # Render Assistant's response
                with st.chat_message("assistant"):
                    st.markdown(response.text)
            except Exception as e:
                with st.chat_message("assistant"):
                    if "429" in str(e) or "quota" in str(e).lower() or "limit" in str(e).lower():
                        st.markdown(
                            """
                            <div style="border: 1px solid rgba(245, 158, 11, 0.3); background-color: rgba(245, 158, 11, 0.05); padding: 16px; border-radius: 12px; color: #fbbf24; font-size: 0.95rem; backdrop-filter: blur(8px); margin: 8px 0; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);">
                                <strong style="font-size: 1.05rem; display: block; margin-bottom: 4px;">⚠️ Quota Exceeded (429 Error)</strong>
                                Your Gemini API Key has reached the daily limit of 20 requests for the free tier of the <strong>gemini-2.5-flash</strong> model.
                                <div style="margin-top: 8px; color: #d1d5db; font-size: 0.85rem;">
                                    💡 <strong>To resolve this:</strong><br>
                                    - Please wait for the daily quota to reset.<br>
                                    - Configure billing in your Google AI Studio account.<br>
                                    - Try again later.
                                </div>
                            </div>
                            """, 
                            unsafe_allow_html=True
                        )
                    else:
                        st.error(f"❌ An error occurred: {e}")
        else:
            st.error("Chat session is not initialized. Please check your API key.")
