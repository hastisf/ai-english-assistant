import json
import time
import plotly.graph_objects as go
import streamlit as st
from modules.database import save_evaluation  # Akan dibuat di langkah DB
from modules.writing import evaluate_writing

st.markdown(
    """
    <h2 style="
    font-size: clamp(1.4rem, 4vw, 2.2rem);
    font-weight:700;
    margin-bottom:0.3rem;
    color:#0F172A;
    ">
    🖋️ Writing Evaluation
    </h2>
    """, 
    unsafe_allow_html=True)

st.caption("Receive AI-powered feedback to improve your English writing skills.")

st.markdown("""
<style>

/* Evaluate Button */
div.stButton > button {
    background: linear-gradient(90deg, #1D4ED8, #22D3EE);
    color: white;
    border: none;
    border-radius: 10px;
    font-weight: 600;
    transition: 0.2s ease;
}

div.stButton > button:hover {
    background: linear-gradient(90deg, #2563EB, #06B6D4)
    color: white;
}

div.stButton > button:active {
    background: linear-gradient(90deg, #1D4ED8, #22D3EE);
    color: white;
    transform: scale(0.98);
}

div.stButton > button:focus,
div.stButton > button:focus-visible {
    outline: none;
    border-color: #22D3EE;
    box-shadow: 0 0 0 0.2rem rgba(34, 211, 238, 0.35);
}

</style>
""", unsafe_allow_html=True)

cefr_level = st.selectbox("CEFR Level", ["A1", "A2", "B1", "B2", "C1", "C2"])
writing_type = st.selectbox(
    "Writing Type", ["Sentence", "Paragraph", "Essay", "Email", "Story"]
)

user_text = st.text_area(
    "Write your text here", height=200, placeholder="Start writing..."
)

if st.button("✨ Evaluate Writing", use_container_width=True):
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
        🌸 Evaluation Complete!
        </p>
        """, unsafe_allow_html=True)
        
        time.sleep(0.6)

        loading_text.empty()
        progress_bar.empty()
        # -----------------------------------------------------------------

        # Tampilkan Overall Score
        score = int(result.get("overall_score", 0))

        grammar_score = int(result.get("grammar_score", 0))
        vocabulary_score = int(result.get("vocabulary_score", 0))
        coherence_score = int(result.get("coherence_score", 0))
        task_score = int(result.get("task_achievement_score", 0))

        estimated_cefr = result.get("estimated_cefr", "-")
        estimated_ielts = result.get("estimated_ielts", "-")

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

            col1, col2 = st.columns(2)

            with col1:
                st.caption("Overall Score")
                st.subheader(f"{score}/100")

                st.caption("Estimated IELTS")
                st.markdown(f"**Band {estimated_ielts}**")

            with col2:
                st.caption("Proficiency Level")
                st.markdown(f"**{level}**")

                st.caption("Estimated CEFR")
                st.markdown(f"**{estimated_cefr}**")

    with st.container(border=True):
        
        st.write("**Performance Overview**")
        st.caption("Visual summary of your writing performance.")

        categories = [
            "Grammar",
            "Vocabulary",
            "Coherence",
            "Task Achievement"
        ]

        values = [
            grammar_score,
            vocabulary_score,
            coherence_score,
            task_score
        ]

        fig = go.Figure()

        fig.add_trace(
            go.Scatterpolar(
                r=values + [values[0]],
                theta=categories + [categories[0]],
                fill="toself",
                line=dict(
                    color="#1D4ED8",
                    width=3
                ),
                fillcolor="rgba(34,211,238,0.35)"
            )
        )

        fig.update_layout(
            polar=dict(
                radialaxis=dict(
                    visible=True,
                    range=[0, 100],
                    gridcolor="#D6F4FF",
                    tickfont=dict(size=10)
                ),
                angularaxis=dict(
                    tickfont=dict(size=12)
                )
            ),
            showlegend=False,
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            margin=dict(l=20, r=20, t=20, b=20),
            height=420,
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

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
            st.markdown(f"""
            <div style="
            background:#F8FAFC;
            border-left:5px solid #1D4ED8;
            padding:15px;
            border-radius:8px;
            margin-top:12px;
            margin-bottom:12px;
            ">

            <b>AI Corrected Version</b><br>
            {result.get("corrected_version","-")}

            </div>
            """, unsafe_allow_html=True)


        # Simpan ke Database
        save_evaluation(
            eval_type="Writing",
            user_input=user_text,
            overall_score=score,
            feedback_json=json.dumps(result),
        )
        
        st.toast("Writing evaluation saved successfully!")
