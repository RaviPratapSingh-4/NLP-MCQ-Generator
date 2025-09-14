📝 NLP MCQ Generator

A Flask-based web application that uses Natural Language Processing (NLP) and spaCy to automatically generate Multiple-Choice Questions (MCQs) from user-provided text or documents.

✨ Features

📄 File Upload: Upload .pdf or .txt files.

🖊️ Text Input: Paste text directly into a text area.

🤖 MCQ Generation: Creates questions with stem, options, and correct answers.

🎨 User-Friendly UI: Simple, clean, and intuitive web interface.

⚙️ Setup
# Clone repo
git clone https://github.com/your-username/nlp-mcq-generator.git
cd nlp-mcq-generator

# Create virtual environment
python -m venv venv
source venv/bin/activate   # macOS/Linux
.\venv\Scripts\activate    # Windows

# Install dependencies
pip install Flask Flask-Bootstrap spacy PyPDF2 transformers

# Download spaCy English model
python -m spacy download en_core_web_sm


Project Structure:

your-project/
├── app.py
├── static/
│   └── style.css
├── templates/
│   ├── index.html
│   └── mcqs.html
└── venv/


Run the app:

python app.py


🚀 Usage

Upload a .pdf or .txt file or paste text into the input box.

Select the number of MCQs to generate (e.g., 5, 10, 15).

Click Generate MCQs.

View the generated questions, options, and answers.

🎯 Sample Output

Q: The Amazon rainforest is the largest rainforest in the world, primarily spread across Brazil, Peru, and ______.

A. Argentina

B. Colombia ✅

C. Ecuador

D. Venezuela
