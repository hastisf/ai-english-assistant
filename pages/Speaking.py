import streamlit as st
from google.genai import types
from modules.gemini_client import MODEL, client

st.title("🎙️ Speaking Evaluation")

audio_file = st.audio_input("Record your speaking")

if audio_file is not None:
    st.audio(audio_file)

    if st.button("🎙️ Evaluate Speaking", use_container_width=True):
        with st.spinner("Transcribing & Analyzing..."):
            # 1. Baca byte dari file audio
            audio_bytes = audio_file.read()
            
            # 2. Deteksi Mime Type (default ke audio/wav jika tidak terdeteksi)
            mime_type = audio_file.type if audio_file.type else "audio/wav"

            prompt = """
            Transcribe this audio, then evaluate the speaking ability based on:
            1. Transcribed text
            2. Fluency & Pronunciation
            3. Grammar & Vocabulary
            4. Overall Score (0-100)
            5. Improvement Suggestions

            Return valid JSON only.
            """

            # 3. Kirim ke Gemini dengan types.Part.from_bytes
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

            st.markdown(response.text)
