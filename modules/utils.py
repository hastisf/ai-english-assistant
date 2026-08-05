import json
import re


def extract_json(text: str) -> dict:
    """
    Extract JSON object from Gemini response.
    Handles responses wrapped in ```json ... ```
    """

    # Remove markdown code fences
    text = re.sub(r"```json", "", text, flags=re.IGNORECASE)
    text = re.sub(r"```", "", text)

    text = text.strip()

    return json.loads(text)
