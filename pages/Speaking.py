import streamlit as st
from modules.gemini_client import MODEL, client

st.title("🎙️ Speaking Evaluation")

audio_file = st.audio_input("Record your speaking")
# Atau gunakan: audio_file = st.file_uploader("Upload Audio", type=["wav", "mp3", "m4a"])

if audio_file is not None:
  st.audio(audio_file)

  if st.button("🎙️ Evaluate Speaking", use_container_width=True):
    with st.spinner("Transcribing & Analyzing..."):
      audio_bytes = audio_file.read()

      prompt = """
            Transcribe this audio, then evaluate the speaking ability based on:
            1. Transcribed text
            2. Fluency & Pronunciation
            3. Grammar & Vocabulary
            4. Overall Score (0-100)
            5. Improvement Suggestions

            Return valid JSON only.
            """

      response = client.models.generate_content(
          model=MODEL,
          contents=[
              prompt,
              {"mime_type": audio_file.type or "audio/wav", "data": audio_bytes},
          ],
      )

      st.markdown(response.text)
