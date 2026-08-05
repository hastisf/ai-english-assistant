import json
import time
import streamlit as st
from modules.database import save_evaluation  # Akan dibuat di langkah DB
from modules.writing import evaluate_writing

st.title("🖋️ Writing Evaluation")
st.write("Receive AI-powered feedback on your English writing.")

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
            (15, "🌰 Planted seeds (Scanning user text)..."),
            (40, "🌱 Sprouting (Analyzing grammar & tenses)..."),
            (65, "🌿 Growing stem (Evaluating vocabulary & coherence)..."),
            (85, "🌷 Preparing to bloom (Generating score & feedback)..."),
        ]

        for percent, text in growth_stages:
            progress_bar.progress(percent)
            loading_text.markdown(f"<p style='text-align: center; font-weight: bold;'>{text}</p>", unsafe_allow_html=True)
            time.sleep(0.4)

        result = evaluate_writing(user_text, cefr_level, writing_type)

        progress_bar.progress(100)
        loading_text.markdown("<p style='text-align: center; font-weight: bold; color: #2e7d32;'>🌸 Full Bloom! Analysis Complete.</p>", unsafe_allow_html=True)
        time.sleep(0.6)

        loading_text.empty()
        progress_bar.empty()
        # -----------------------------------------------------------------

        # Tampilkan Overall Score
        score = result.get("overall_score", 0)
        st.metric(label="Overall Score", value=f"{score}/100")

        # Tampilkan Detail Feedback dalam Tab/Expander
        st.subheader("📊 Feedback Detail")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown(
                f"**Grammar:**\n{result.get('grammar_feedback', '-')}"
            )
            st.markdown(
                f"**Vocabulary:**\n{result.get('vocabulary_feedback', '-')}"
            )
        with col2:
            st.markdown(
                f"**Coherence:**\n{result.get('coherence_feedback', '-')}"
            )
            st.markdown(
                f"**Task Achievement:**\n{result.get('task_achievement', '-')}"
            )

        st.success(
            f"**Strengths:** {result.get('strengths', '-')}\n\n"
            f"**Weaknesses:** {result.get('weaknesses', '-')}"
        )

        st.info(
            f"**Improvement Suggestion:**\n{result.get('improvement_suggestion', '-')}"
        )

        if result.get("corrected_version"):
            with st.expander("✨ View Corrected Version"):
                st.write(result.get("corrected_version"))

        # Simpan ke Database
        save_evaluation(
            eval_type="Writing",
            user_input=user_text,
            overall_score=score,
            feedback_json=json.dumps(result),
        )
        st.toast("Hasil evaluasi berhasil disimpan ke Database!")
