import json
import time
import streamlit as st
from modules.database import save_evaluation  # Akan dibuat di langkah DB
from modules.writing import evaluate_writing

st.markdown("""
<h2 style="
font-size: clamp(1.4rem, 4vw, 2.2rem);
font-weight:700;
margin-bottom:0.3rem;
color:#0F172A;
">
🖋️ Writing Evaluation
</h2>

<div style="
width:90px;
height:5px;
border-radius:999px;
background:linear-gradient(90deg,#1D4ED8,#22D3EE);
margin-bottom:20px;
"></div>
""", unsafe_allow_html=True)

st.caption("Receive AI-powered feedback to improve your English writing skills.")

cefr_level = st.selectbox("CEFR Level", ["A1", "A2", "B1", "B2", "C1", "C2"])
writing_type = st.selectbox(
    "Writing Type", ["Sentence", "Paragraph", "Essay", "Email", "Story"]
)

user_text = st.text_area(
    "Write your text here", height=200, placeholder="Start writing..."
)

if st.button("✨ Analyze Writing", use_container_width=True):
    if not user_text.strip():
        st.warning("Please enter your writing first.")
    else:
        # -----------------------------------------------------------------
        # BLOOMING ANIMATION LOADING
        # -----------------------------------------------------------------
        loading_text = st.empty()
        progress_bar = st.progress(0)

        growth_stages = [
            (15, "🌰 Scanning your writing..."),
            (40, "🌱 Checking grammar & sentence structure..."),
            (65, "🌿 Evaluating vocabulary & coherence..."),
            (85, "🌷 Preparing your feedback report..."),
        ]

        for percent, text in growth_stages:
            progress_bar.progress(percent)
            loading_text.markdown(
                f"""
                <p style="
                    text-align:center;color:#2563EB;
                    font-size:16px;
                    font-weight:600;
                ">
                    {text}
                </p>
                """,
                unsafe_allow_html=True)
            time.sleep(0.4)

        result = evaluate_writing(user_text, cefr_level, writing_type)

        progress_bar.progress(100)
        loading_text.markdown("""
        <p style="
        text-align:center;
        font-size:16px;
        font-weight:700;
        color:#16A34A;
        margin-top:8px;
        ">
        🌸 Analysis Complete!
        </p>
        """, unsafe_allow_html=True)
        
        time.sleep(0.6)

        loading_text.empty()
        progress_bar.empty()
        # -----------------------------------------------------------------

        # Tampilkan Overall Score
        score = int(result.get("overall_score", 0))

        if score >= 85:
            level = "Advanced"
        elif score >= 70:
            level = "Upper-Intermediate"
        elif score >= 50:
            level = "Intermediate"
        else:
            level = "Beginner"

        st.divider()

        with st.container(border=True):

            col_score, col_level = st.columns(
                2,
                vertical_alignment="center"
            )
            

            with col_score:
                st.caption("Overall Score")
                st.subheader(f"{score}/100")

            with col_level:
                st.caption("Writing Level")
                st.markdown(f"**{level}**")

        # Tampilkan Detail Feedback dalam Tab/Expander
        st.write("**Skill Breakdown**")

        tab1, tab2, tab3, tab4 = st.tabs([
            "Grammar",
            "Vocabulary",
            "Coherence",
            "Task Achievement"
        ])

        with tab1:
            st.write(result.get("grammar_feedback","-"))

        with tab2:
            st.write(result.get("vocabulary_feedback","-"))

        with tab3:
            st.write(result.get("coherence_feedback","-"))

        with tab4:
            st.write(result.get("task_achievement","-"))

        st.write("")
        
        st.markdown(f"""
        <div style="
        background:#EFF6FF;
        border-left:5px solid #1D4ED8;
        padding:15px;
        border-radius:8px;
        margin-top:12px;
        margin-bottom:12px;
        ">

        <b>Strengths</b><br>
        {result.get("strengths","-")}

        </div>
        """, unsafe_allow_html=True)

        st.markdown(f"""
        <div style="
        background:#E0F7FA;
        border-left:5px solid #0EA5E9;
        padding:15px;
        border-radius:8px;
        margin-top:12px;
        margin-bottom:12px;
        ">

        <b>Weaknesses</b><br>
        {result.get("weaknesses","-")}

        </div>
        """, unsafe_allow_html=True)

        st.markdown(f"""
        <div style="
        background:#ECFEFF;
        border-left:5px solid #22D3EE;
        padding:15px;
        border-radius:8px;
        margin-top:12px;
        margin-bottom:12px;
        ">

        <b>Improvement Suggestion</b><br>
        {result.get("improvement_suggestion","-")}

        </div>
        """, unsafe_allow_html=True)

        if result.get("corrected_version"):
            with st.container(border=True):
                st.write("**AI Corrected Version**")
                st.write(result.get("corrected_version"))

        # Simpan ke Database
        save_evaluation(
            eval_type="Writing",
            user_input=user_text,
            overall_score=score,
            feedback_json=json.dumps(result),
        )
        
        st.toast("Writing evaluation saved successfully!")
