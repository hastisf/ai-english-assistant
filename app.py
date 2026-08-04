import streamlit as st

# =========================
# Page Configuration
# =========================
st.set_page_config(
    page_title="AI English Assistant",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================
# Home Page
# =========================
st.title("🤖 AI English Assistant")

st.markdown("""
Welcome to **AI English Assistant**!

This application uses **Google Gemini AI** to evaluate your English skills.

### Features
- ✍️ Writing Evaluation
- 🎤 Speaking Evaluation
- 📜 Evaluation History

👈 Select a feature from the sidebar to get started.
""")