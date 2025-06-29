from transformers import pipeline

qa_pipeline = pipeline("question-answering", model="distilbert-base-uncased-distilled-squad")

def answer_question(text, question):
    result = qa_pipeline(question=question, context=text)
    answer = result["answer"]
    return answer, f"This is supported by context in: '{text[:200]}...'"