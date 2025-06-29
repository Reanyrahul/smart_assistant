# we are  importing necessary libraries and backend modules
import streamlit as st
from backend.summarize import generate_summary             
from backend.qna import answer_question                      
from backend.logic_questions import generate_questions, evaluate_answer  
from utils.pdf_parser import parse_pdf                       
from utils.txt_parser import parse_txt                       

# Set up the page configuration for the Streamlit app
st.set_page_config(page_title="Smart Assistant for Research Summarization", layout="wide")

# Our app title
st.title("📚 Smart Assistant")

# File uploader for user to upload either PDF or TXT file
uploaded_file = st.file_uploader("Upload a PDF or TXT file", type=["pdf", "txt"])

# If a file is uploaded, proceed
if uploaded_file:
    # Check file type and parse text accordingly
    if uploaded_file.type == "application/pdf":
        doc_text = parse_pdf(uploaded_file)   # Extract text from PDF
    else:
        doc_text = parse_txt(uploaded_file)   # Extract text from TXT

    # Generate a summary from the parsed document text
    summary = generate_summary(doc_text)

    # Display the summary on the UI
    st.subheader("📄 Document Summary")
    st.write(summary)

    # Allow user to choose interaction mode: Q&A or Challenge Mode
    mode = st.radio("Choose Interaction Mode", ["Ask Anything", "Challenge Me"])

    # --- Mode 1: Ask Anything (Open-ended Question Answering) ---
    if mode == "Ask Anything":
        user_q = st.text_input("Ask a question from the document:")  # User inputs a question

        if user_q:
            response, justification = answer_question(doc_text, user_q)  # Get answer and justification
            st.markdown("**Answer:** " + response)                       # Show answer
            st.markdown("*Justification:* " + justification)            # Show reasoning

    # --- Mode 2: Challenge Me (Auto-generated Questions + User Answers) ---
    elif mode == "Challenge Me":
        questions = generate_questions(doc_text)  # Generate questions from document
        user_answers = []                         # Store user answers

        # Loop through questions and get user's answers via text input
        for i, q in enumerate(questions):
            ans = st.text_input(f"Q{i+1}: {q}", key=f"challenge_{i}")
            user_answers.append(ans)

        # Once user clicks submit, evaluate each answer
        if st.button("Submit Answers"):
            for i, user_ans in enumerate(user_answers):
                result, explanation = evaluate_answer(doc_text, questions[i], user_ans)  # Evaluate user response
                st.markdown(f"**Q{i+1} Result:** {result}")                             # Display result
                st.markdown(f"*Explanation:* {explanation}")                            # Explain the correct answer
