# 🤖 Gemini 2.5 Flash - Streamlit ChatBot

A beautiful, modern, and interactive chatbot web application built with **Streamlit** and powered by Google's state-of-the-art **Gemini 2.5 Flash** model. 

---

## ✨ Features
* **Modern Chat UI:** Implements a sleek, responsive, and interactive chat interface using native Streamlit chat components.
* **Powered by Gemini 2.5 Flash:** Uses the latest fast, lightweight, and highly optimized multimodal AI model from Google.
* **Persistent Sessions:** Keeps track of conversation history in real-time within your current browser session.
* **Secure Key Management:** Automatically loads your Google API credentials securely from a local `.env` configuration file to prevent exposure on GitHub.

---

## 🚀 Getting Started

### 📋 Prerequisites
Ensure you have the following installed on your machine:
* Python 3.9 or higher (fully supports Python 3.11+ and experimental Python 3.14)
* A Google Gemini API Key (get yours from [Google AI Studio](https://aistudio.google.com/))

### 🔧 Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/navya-08-code/chat-bot-gemini.git
   cd chat-bot-gemini
   ```

2. **Create and activate a Virtual Environment:**
   * **Windows:**
     ```powershell
     python -m venv .venv
     .venv\Scripts\Activate.ps1
     ```
   * **macOS / Linux:**
     ```bash
     python -m venv .venv
     source .venv/bin/activate
     ```

3. **Install the dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure your API Key:**
   Create a `.env` file in the root directory and add your Google API key:
   ```env
   GOOGLE_API_KEY=your_actual_api_key_here
   ```

---

## 🎈 Running the ChatBot

Start the Streamlit application with the following command:
```bash
streamlit run main.py
```

Your web browser will automatically open the application at:
👉 **`http://localhost:8501`**

---

## 🛠️ Technology Stack
* **Frontend/App framework:** [Streamlit](https://streamlit.io/)
* **AI Model API:** [Google Generative AI SDK](https://github.com/google/generative-ai-python)
* **Environment variables management:** [python-dotenv](https://github.com/theofidry/django-dotenv)

---

## 🔒 Security Notice
The `.env` file containing your `GOOGLE_API_KEY` is listed in `.gitignore` and is **never** uploaded to GitHub. Keep your API key private at all times to prevent unauthorized usage.
