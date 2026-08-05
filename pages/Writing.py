import streamlit as st

# ==========================================
# Page Configuration
# ==========================================
st.set_page_config(
    page_title="Writing Evaluation | SWIM",
    page_icon="📝",
    layout="wide"
)

# ==========================================
# Header
# ==========================================
st.title("📝 Writing Evaluation")

st.write(
    """
Improve your English writing with AI-powered evaluation.
Receive detailed feedback on grammar, vocabulary, coherence,
and overall writing quality.
"""
)

st.divider()

# ==========================================
# Writing Settings
# ==========================================

col1, col2 = st.columns(2)

with col1:
    writing_type = st.selectbox(
        "Writing Type",
        [
            "Essay",
            "Email",
            "Letter",
            "Story",
            "Article",
            "Report"
        ]
    )

with col2:
    cefr = st.selectbox(
        "CEFR Level",
        [
            "A1 Beginner",
            "A2 Elementary",
            "B1 Intermediate",
            "B2 Upper Intermediate",
            "C1 Advanced",
            "C2 Proficient"
        ]
    )

# ==========================================
# Writing Input
# ==========================================

essay = st.text_area(
    "Write your English text",
    height=350,
    placeholder="Start typing here..."
)

word_count = len(essay.split())

st.caption(f"Word Count: **{word_count}**")

st.divider()

# ==========================================
# Buttons
# ==========================================

col1, col2, col3 = st.columns([2,2,6])

with col1:

    evaluate = st.button(
        "🚀 Evaluate",
        use_container_width=True
    )

with col2:

    clear = st.button(
        "🗑️ Clear",
        use_container_width=True
    )

if clear:
    st.rerun()

# ==========================================
# Validation
# ==========================================

if evaluate:

    if essay.strip() == "":
        st.warning("Please enter your writing first.")

    elif word_count < 20:
        st.warning("Please write at least 20 words.")

    else:

        st.success("Your writing is ready for AI evaluation!")

        st.info(
            """
The next step will send your writing to Google Gemini
and generate detailed feedback.
"""
        )
