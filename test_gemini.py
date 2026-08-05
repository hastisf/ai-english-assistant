from modules.writing import evaluate_writing

result = evaluate_writing(
    text="Yesterday I goes to school.",
    cefr_level="A2",
    writing_type="Paragraph"
)

print(result)