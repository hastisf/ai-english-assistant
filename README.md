<div align="center">

<img src="assets/swim.png" alt="SWIM Logo" width="90">

# SWIM — Speaking & Writing Improvement Mate

**An AI-powered English practice app for evaluating and improving speaking and writing skills.**

🚀 **Live Demo:** [swim-ai-english-assistant.streamlit.app](https://swim-ai-english-assistant.streamlit.app)

</div>

---

## Overview

**SWIM (Speaking & Writing Improvement Mate)** is an AI-powered English learning application built with Streamlit.

The application helps users practice their **speaking and writing skills** by providing AI-based evaluations, scores, structured feedback, and personalized suggestions for improvement.

SWIM is designed to make English practice more interactive by allowing users to receive immediate feedback on their performance.

## Features

### 🎙️ Speaking Evaluation

- Record or upload English speech
- Generate speech transcription
- Evaluate **fluency, pronunciation, grammar, and vocabulary**
- Get an overall speaking score
- Identify strengths and weaknesses
- Receive personalized improvement suggestions
- View English proficiency level based on the overall score

### ✍️ Writing Evaluation

- Submit English writing directly in the application
- Select CEFR level
- Select writing type
- Evaluate writing using AI
- Receive structured feedback
- Identify strengths and weaknesses
- Get an overall writing score
- Receive suggestions for improvement

### 📚 Evaluation History

- Store previous evaluations
- View speaking and writing evaluation results
- Review previous scores and feedback
- Keep track of learning progress

## Tech Stack

| Technology | Purpose |
|---|---|
| **Python** | Application development |
| **Streamlit** | Web application framework |
| **Google Gemini API** | AI-powered evaluation |
| **SQLite** | Evaluation history storage |
| **Pandas** | Data processing |
| **Pillow** | Image handling |

## How It Works

```text
                    SWIM
                     │
          ┌──────────┴──────────┐
          │                     │
      Speaking                Writing
          │                     │
     Audio Input            Text Input
          │                     │
          ▼                     ▼
   Speech Processing      Text Processing
          │                     │
          └──────────┬──────────┘
                     │
                     ▼
              Gemini AI Evaluation
                     │
          ┌──────────┼──────────┐
          │          │          │
        Score     Feedback   Suggestions
          │          │          │
          └──────────┼──────────┘
                     │
                     ▼
             Evaluation History
