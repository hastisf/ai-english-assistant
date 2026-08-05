import json
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
        with st.spinner("Analyzing..."):
            result = evaluate_writing(user_text, cefr_level, writing_type)

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
