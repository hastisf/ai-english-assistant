from google.genai import types
from modules.gemini_client import MODEL, client

def evaluate_speaking(audio_file):
    audio_bytes = audio_file.getvalue()

    mime_type = (
        audio_file.type
        if audio_file.type
        else "audio/wav"
    )

    prompt = """
    Transcribe this audio, then evaluate the speaking ability based on:
    1. Transcribed text
    2. Fluency & Pronunciation
    3. Grammar & Vocabulary
    4. Overall Score (0-100)
    5. Improvement Suggestions

    Return valid Markdown.
    """

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

    return response.text
