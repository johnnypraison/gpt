# Python + Ollama Lab Exam Programs

20 separate programs covering all 30 questions in the provided question sheet. Repeated questions use the same program.

## Setup

1. Install Python 3.9 or later and Ollama.
2. Install dependency: `pip install -r requirements.txt`
3. Download model: `ollama pull llama3.2`
4. Start Ollama: `ollama serve`
5. Open another terminal in this folder and run a program, for example:
   `python programs/q01_grammar_correction.py`

## Question mapping

| Question(s) | Program |
|---|---|
| 1, 21 | q01_grammar_correction.py |
| 2, 22 | q02_sentiment_analysis.py |
| 3, 23 | q03_mcq_generator.py |
| 4, 24 | q04_study_assistant.py |
| 5, 25 | q05_flashcard_generator.py |
| 6, 26 | q06_meeting_minutes.py |
| 7, 27 | q07_resume_analyzer.py |
| 8, 28 | q08_college_faq_chatbot.py |
| 9, 29 | q09_customer_feedback_analyzer.py |
| 10, 20 | q10_interview_preparation.py |
| 11 | q11_story_generator.py |
| 12 | q12_text_translation.py |
| 13 | q13_text_summarizer.py |
| 14 | q14_question_paper_generator.py |
| 15 | q15_paragraph_rewriter.py |
| 16 | q16_keyword_extractor.py |
| 17 | q17_assignment_topic_generator.py |
| 18 | q18_product_description_generator.py |
| 19 | q19_daily_task_planner.py |
| 30 | q30_email_assistant.py |

## Notes

- Each program includes the common `ask_ollama()` function.
- Text output files are created in the folder from which you run the program.
- For Q7, keep `resume.txt` in the project root. A sample file is included; replace it with your own test content.
- The FAQ answers are examples. Replace them with verified college information.
- AI responses can vary. Review generated answers before using them.
