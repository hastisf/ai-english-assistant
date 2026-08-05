import time
import streamlit as st
from google.genai import types
from modules.gemini_client import MODEL, client

st.markdown(
    """
    <h2 style='font-size: clamp(1.4rem, 4vw, 2.2rem); font-weight: 700; margin-bottom: 0.5rem;'>
        🗣️ Speaking Evaluation
    </h2>
    """, 
    unsafe_allow_html=True
)
audio_file = st.audio_input("Record your speaking")

if audio_file is not None:
    st.audio(audio_file)

    if st.button("🎙️ Evaluate Speaking", use_container_width=True):
        # -----------------------------------------------------------------
        # BLOOMING ANIMATION LOADING
        # -----------------------------------------------------------------
        loading_text = st.empty()
        progress_bar = st.progress(0)

        growth_stages = [
            (15, "🌰 Planted seeds (Processing audio recording)..."),
            (40, "🌱 Sprouting (Transcribing speech to text)..."),
            (65, "🌿 Growing stem (Analyzing fluency & pronunciation)..."),
            (85, "🌷 Preparing to bloom (Evaluating grammar & vocabulary)..."),
        ]

        for percent, text in growth_stages:
            progress_bar.progress(percent)
            loading_text.markdown(f"<p style='text-align: center; font-weight: bold;'>{text}</p>", unsafe_allow_html=True)
            time.sleep(0.4)

        # 1. Baca byte dari file audio
        audio_bytes = audio_file.getvalue()
        
        # Debug
        with open("debug.wav", "wb") as f:
            f.write(audio_bytes)
            
        st.success("Audio saved as debug.wav.")
        
        st.write("Mime Type:", audio_file.type)
        st.write("Audio Size:", len(audio_bytes), "bytes")
        
        # 2. Deteksi Mime Type
        mime_type = audio_file.type if audio_file.type else "audio/wav"

        prompt = """
        You are an experienced English speaking evaluator.

        Analyze the uploaded speech and evaluate the speaker's English proficiency.

        Organize your response using the following headings:

        ## Transcribed Text
        Provide the complete transcription of the audio.

        ## Fluency & Pronunciation
        Evaluate the speaker's pronunciation, fluency, intonation, speaking pace, and clarity in one concise paragraph.

        ## Grammar & Vocabulary
        Evaluate grammar accuracy, vocabulary range, and sentence structure in one concise paragraph.

        ## Overall Score
        Provide an overall score between 0 and 100, followed by a brief explanation.

        ## Suggestions for Improvement
        Provide 3–5 practical suggestions to help the speaker improve.

        Requirements:
        - Return the response in Markdown format.
        - Do not return JSON.
        - Do not use code blocks.
        - Keep the evaluation concise, professional, and constructive.
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

            progress_bar.progress(100)
            loading_text.markdown("<p style='text-align: center; font-weight: bold; color: #2e7d32;'>🌸 Full Bloom! Evaluation Complete.</p>", unsafe_allow_html=True)
            time.sleep(0.6)

            loading_text.empty()
            progress_bar.empty()

            st.markdown(response.text)

        except Exception as e:
            loading_text.empty()
            progress_bar.empty()
            st.error(f"An error occurred during evaluation: {e}")
