from modules.gemini_client import client, MODEL
from modules.prompts import get_writing_prompt
from modules.utils import extract_json


def evaluate_writing(text: str, cefr_level: str, writing_type: str):

    prompt = get_writing_prompt(
        cefr_level=cefr_level,
        writing_type=writing_type,
        user_text=text
    )

    response = client.models.generate_content(
        model=MODEL,
        contents=prompt
    )

    try:
        return extract_json(response.text)

    except Exception:

        return {
            "overall_score": None,
            "grammar_feedback": "Unable to parse Gemini response.",
            "vocabulary_feedback": "",
            "coherence_feedback": "",
            "task_achievement": "",
            "strengths": "",
            "weaknesses": "",
            "improvement_suggestion": "",
            "corrected_version": "",
            "raw_response": response.text
        }
