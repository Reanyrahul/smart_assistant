from transformers import pipeline
import random

# Load a lightweight local text generation model (distilgpt2) for generating questions
question_generator = pipeline("text-generation", model="distilgpt2")

def generate_questions(text):
    """
    Generate 3 logic-based or comprehension questions from a given text.
    
    Parameters:
    - text (str): Input document text from which questions are to be generated.

    Returns:
    - questions (list): A list of 1–3 generated questions.
    """
    # Create a prompt instructing the model to generate questions based on the input text
    prompt = (
        "Based on the following text, generate 3 logic-based or comprehension questions to test understanding.\n\n"
        f"{text[:1000]}\n\nQuestions:"  # Only use the first 1000 characters to fit model context window
    )

    # Generate text using the model; sample with a bit of randomness
    response = question_generator(
        prompt,
        max_length=256,              # Limit the response length
        num_return_sequences=1,      # Generate only one set of questions
        do_sample=True               # Enable randomness to vary output
    )

    # Extract the generated text, specifically the part after "Questions:"
    generated = response[0]['generated_text'].split("Questions:")[-1]

    # Clean up the generated output and split into individual questions
    questions = [
        q.strip("-•0123456789. ")    # Remove bullet points or numbering
        for q in generated.strip().split("\n") if q.strip()
    ]

    # Return up to 3 questions
    return questions[:3] if len(questions) >= 3 else questions

def evaluate_answer(text, question, user_answer):
    """
    Evaluate user's answer by checking if any words in it match content from the document.
    
    Parameters:
    - text (str): Original document content.
    - question (str): The generated question.
    - user_answer (str): Answer submitted by the user.

    Returns:
    - result (str): "Correct or partially correct" or "Incorrect or irrelevant"
    - explanation (str): A brief justification of the result.
    """
    # Simple keyword-based evaluation: checks if any word from the user answer appears in the original text
    if user_answer and any(word.lower() in text.lower() for word in user_answer.split()):
        return "Correct or partially correct", f"Matched with content: '{text[:200]}...'"  # Show snippet as justification

    # If no match found, return incorrect
    return "Incorrect or irrelevant", f"No clear match found in: '{text[:200]}...'"  # Still show snippet for reference
