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
    font-size:30px;
    font-weight:700;
    color:#0F172A;
    margin-bottom:5px;
}

.subtitle{
    font-size:18px;
    color:#6B7280;
    line-height:1.7;
}

.feature-box{
    background:#F8FAFC;
    border:1px solid #E5E7EB;
    border-radius:15px;
    padding:20px;
}

.footer{
    text-align:center;
    color:#9CA3AF;
    font-size:14px;
}

</style>
""", unsafe_allow_html=True)

# ==========================================
# Header
# ==========================================
col_logo, col_text = st.columns([1, 6])

with col_logo:
    st.image(logo, width=90)

with col_text:
    st.markdown("""
<div class="title">
Speaking & Writing Improvement Mate
</div>

<div class="subtitle">
Improve your English with AI-powered writing and speaking feedback.
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

Evaluate your English writing and receive:

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

Evaluate your spoken English with AI:

- Pronunciation feedback
- Fluency assessment
- Vocabulary analysis
- Speaking recommendations
- CEFR level evaluation

</div>
""", unsafe_allow_html=True)

st.divider()

# ==========================================
# Footer
# ==========================================
st.markdown("""
<div class="footer">

© 2026 <b>SWIM</b> • Powered by Google Gemini

</div>
""", unsafe_allow_html=True)
