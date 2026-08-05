from PIL import Image
import streamlit as st

# ==========================================
# Load Logo
# ==========================================
logo = Image.open("assets/swim.png")

# ==========================================
# Page Configuration
# ==========================================
st.set_page_config(
    page_title="SWIM",
    page_icon=logo,
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================
# Custom CSS
# ==========================================
st.markdown("""
<style>

.main{
    padding-top:2rem;
}

.title{
    font-size:34px;
    font-weight:700;
    color:#0F172A;
    margin-top:12px;
    margin-bottom:0;
}

.subtitle{
    font-size:20px;
    color:#64748B;
    line-height:1.7;
    margin-top:18px;
}

.feature-box{
    background:#F8FAFC;
    border:1px solid #E5E7EB;
    border-radius:15px;
    padding:20px;
}

.footer-container {
    text-align:center;
    color:#64748B;
    font-size:13px;
    margin-top:40px;
    padding-top:20px;
    padding-bottom:20px;
    border-top:1px solid #E2E8F0;
}

.footer-links a{
    color:#2563EB;
    text-decoration:none;
    font-weight:600;
    margin:0 10px;
}

.footer-links a:hover{
    text-decoration:underline;
}

</style>
""", unsafe_allow_html=True)

# ==========================================
# Header
# ==========================================

col_logo, col_title = st.columns([1, 6], vertical_alignment="center")

with col_logo:
    st.image(logo, width=90)

with col_title:
    st.markdown("""
    <div class="title">
        Speaking & Writing Improvement Mate
    </div>
    """, unsafe_allow_html=True)

st.markdown("""
<div class="subtitle">
Improve your English writing and speaking with instant AI-powered feedback.
</div>
""", unsafe_allow_html=True)

st.divider()

# ==========================================
# Welcome
# ==========================================

st.markdown("## Welcome")

st.write("""
**SWIM** is an AI-powered English learning assistant designed to help you
improve your writing and speaking skills.

Receive instant feedback on grammar, vocabulary, fluency, coherence,
and overall communication through Google Gemini.
""")

st.divider()

# ==========================================
# Features
# ==========================================

st.markdown("## Features")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
<div class="feature-box">

### 📝 Writing Evaluation

- Grammar correction
- Vocabulary suggestions
- Writing feedback
- CEFR level evaluation
- AI recommendations

</div>
""", unsafe_allow_html=True)

with col2:
    st.markdown("""
<div class="feature-box">

### 🎙️ Speaking Evaluation

- Pronunciation feedback
- Fluency assessment
- Vocabulary analysis
- Speaking recommendations
- CEFR level evaluation

</div>
""", unsafe_allow_html=True)

# ==========================================
# Footer
# ==========================================

st.markdown(
"""
<div class="footer-container">

<strong>Hasti Sri Fatmawati</strong> | Data Analyst Portfolio

<div class="footer-links" style="margin-top:8px;">
<a href="https://www.linkedin.com/in/hasti-sri-fatmawati-361b49417/" target="_blank">
LinkedIn
</a>

•

<a href="https://github.com/hastisf/" target="_blank">
GitHub
</a>

</div>

</div>
""",
unsafe_allow_html=True
)
