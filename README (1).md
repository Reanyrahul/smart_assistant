# 📚 Smart Assistant for Research Summarization

An AI-powered assistant built with Streamlit that enables summarization of research papers, interactive Q&A based on content, and logic-based quiz generation to test user comprehension.

---

## 🚀 Features

- 📄 Upload and summarize PDF or TXT documents
- 🤖 Ask questions based on uploaded content and get justified answers
- 🧠 "Challenge Me" mode generates logic-based questions to test your understanding
- ✅ Basic evaluation of user-submitted answers using keyword matching

---

## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/reanyrahul/smart-assistant.git
cd smart-assistant
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
# Activate the environment
source venv/bin/activate      # For Linux/macOS
venv\Scripts\activate         # For Windows
```

### 3. Install Required Packages

If you have a `requirements.txt` file, use:

```bash
pip install -r requirements.txt
```

Or manually install:

```bash
pip install streamlit transformers flake8
```

### 4. Run the App

```bash
streamlit run app.py
```

---

## 🧠 Architecture & Reasoning Flow

### 🔧 Project Structure

```
📦 smart-assistant/
├── app.py                      # Main Streamlit UI logic
├── backend/
│   ├── summarize.py            # Generates document summary
│   ├── qna.py                  # Answers user questions using document context
│   └── logic_questions.py      # Generates and evaluates logical questions
├── utils/
│   ├── pdf_parser.py           # Extracts text from PDF
│   └── txt_parser.py           # Extracts text from TXT
```

---

### ⚙️ Functional Flow

1. **File Upload**  
   - User uploads `.pdf` or `.txt` file.
   - Text is extracted using appropriate utility (PDF/TXT parser).

2. **Summarization**  
   - The document content is passed to a transformer model (`generate_summary`) for summarization.
   - Displayed on screen using Streamlit.

3. **Interaction Modes**  
   - **Ask Anything**
     - User enters a question.
     - `answer_question()` searches context and provides a justified response.
   - **Challenge Me**
     - `generate_questions()` uses a local GPT model (`distilgpt2`) to create logic-based questions.
     - User submits answers which are evaluated using `evaluate_answer()` (keyword-matching).

---

## 🧪 Key Components Explained

### `generate_questions(text)`
- Uses `transformers.pipeline("text-generation", model="distilgpt2")`
- Input: First 1000 characters of the text
- Output: 3 logic/comprehension-style questions

### `evaluate_answer(text, question, user_answer)`
- Evaluates based on presence of answer keywords in the document
- Basic match → "Correct or partially correct"
- No match → "Incorrect or irrelevant"

---

## ✅ Example Use Cases

- Academic research summarization
- Self-testing tool for comprehension
- EdTech & e-learning applications

---

## 🔒 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👤 Author

**Rahul Pareek**  
Feel free to fork, improve, and contribute to this project.

---

📬 *Need help or want to improve this assistant? Open an issue or create a pull request!*