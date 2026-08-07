import json
import time
import streamlit as st
from google.genai import types
from modules.database import save_evaluation
from modules.gemini_client import MODEL, client

st.markdown(
    """
    <h2 style='font-size: clamp(1.4rem, 4vw, 2.2rem); font-weight: 700; margin-bottom: 0.5rem;'>
        🎙 Speaking Evaluation
    </h2>
    """, 
    unsafe_allow_html=True
)

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

audio_file = st.audio_input("Record your speaking")

if audio_file is not None:
    st.audio(audio_file)

    if st.button(
    "✨ Evaluate Speaking",
    use_container_width=True,
    ):
        
        # -----------------------------------------------------------------
        # BLOOMING ANIMATION LOADING
        # -----------------------------------------------------------------
        loading_text = st.empty()
        progress_bar = st.progress(0)

        growth_stages = [
            (15, "🌰 Processing audio recording..."),
            (40, "🌱 Transcribing speech to text..."),
            (65, "🌿 Analyzing fluency & pronunciation..."),
            (85, "🌷 Evaluating grammar & vocabulary..."),
        ]

        for percent, text in growth_stages:
            progress_bar.progress(percent)
            loading_text.markdown(
                f"""
                <p style="
                    text-align: center;
                    color:#2563EB;
                    font-size:16px;
                    font-weight: 600;
                ">
                    {text}
                </p>
                """,
                unsafe_allow_html=True
            )
            time.sleep(0.4)

        # 1. Baca byte dari file audio
        audio_bytes = audio_file.getvalue()
        
        # 2. Deteksi Mime Type
        mime_type = audio_file.type if audio_file.type else "audio/wav"

        prompt = """
        You are an experienced English speaking evaluator.

        Analyze the uploaded speech and return ONLY a valid JSON object.

        Return ONLY the JSON object.

        Do not include markdown.
        Do not include explanation.
        Do not wrap with ```.

        Do not add any text before or after the JSON.
        
        Use this exact structure:
        
        {
            "transcript": "...",
            "overall_score": 0,
            "fluency_feedback": "...",
            "pronunciation_feedback": "...",
            "grammar_feedback": "...",
            "vocabulary_feedback": "...",
            "strengths": "...",
            "weaknesses": "...",
            "improvement_suggestion": "..."
        }

        Scoring:
        - Overall score must be between 0-100.
        - Keep every feedback concise.

        Write all feedback directly to the user.

        Always use second-person language such as:
        - "You..."
        - "Your..."

        Never refer to the user as:
        - "The speaker"
        - "The candidate"
        - "The student"
        - "The speaker's"

        """

        # 3. Kirim ke Gemini
        try:
            response = client.models.generate_content(
                model=MODEL,
                contents=[
                    prompt,
                    types.Part.from_bytes(
                        data=audio_bytes,
                        mime_type=mime_type
                    )
                ]
            )

            clean_text = (
                response.text
                .replace("```json", "")
                .replace("```", "")
                .strip()
            )

            try:
                result = json.loads(clean_text)
            except json.JSONDecodeError:
                st.error("AI returned an invalid response. Please try again.")
                st.stop()

            progress_bar.progress(100)
            loading_text.markdown(
                """
                <p style="
                    text-align: center; 
                    font-weight: 700; 
                    font-size:16px;
                    color: #16A34A;
                    margin-top:8px;
                ">
                    🌸 Evaluation Complete!
                </p>
                """, 
                unsafe_allow_html=True
            )
            
            time.sleep(0.6)

            loading_text.empty()
            progress_bar.empty()

            score = int(result.get("overall_score", 0))
            
            # 1. Tentukan Level Proficiency
            if score >= 85:
                level = "Advanced"
            elif score >= 70:
                level = "Upper-Intermediate"
            elif score >= 50:
                level = "Intermediate"
            else:
                level = "Beginner"

            # 2. Garis Pembatas
            st.divider()
            
            # 3. Hero Card (Skor & Level)
            with st.container(border=True):
                col_score, col_level = st.columns(2, vertical_alignment="center")
                
                with col_score:
                    st.caption("Overall Score")
                    st.subheader(f"{score}/100")
                    
                with col_level:
                    st.caption("Proficiency Level")
                    st.markdown(f"**{level}**")
            
            with st.container(border=True):
                st.write("**Transcript**")
                st.info(f'"{result.get("transcript", "-")}"')
            
            st.write("**Skill Breakdown**")
            tab1, tab2, tab3, tab4 = st.tabs(["Fluency", "Pronunciation", "Grammar", "Vocabulary"])

            with tab1:
                st.write(result.get('fluency_feedback', '-'))
            with tab2:
                st.write(result.get('pronunciation_feedback', '-'))
            with tab3:
                st.write(result.get('grammar_feedback', '-'))
            with tab4:
                st.write(result.get('vocabulary_feedback', '-'))

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
            {result.get("strengths", "-")}

            </div>
            """, unsafe_allow_html=True)

            st.markdown(f"""
            <div style="
            background:#F8FAFC;
            border-left:5px solid #64748B;
            padding:15px;
            border-radius:8px;
            margin-top:12px;
            margin-bottom:12px;
            ">

            <b>Weaknesses</b><br>
            {result.get("weaknesses", "-")}

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
            {result.get("improvement_suggestion", "-")}

            </div>
            """, unsafe_allow_html=True)

            save_evaluation(
                eval_type="Speaking",
                user_input=result.get("transcript", ""),
                overall_score=score,
                feedback_json=json.dumps(result),
            )
                
            st.toast("Speaking evaluation saved successfully!")
        
        except Exception as e:
            loading_text.empty()
            progress_bar.empty()
            st.error(f"An error occurred during evaluation: {e}")
