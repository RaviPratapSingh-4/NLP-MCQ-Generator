from flask import Flask, render_template, request, flash, redirect, url_for, session
from flask_bootstrap import Bootstrap
import spacy
import random
import re
from PyPDF2 import PdfReader

app = Flask(__name__)
app.config['SECRET_KEY'] = '0dcf2fd94d3412278163ad19e97360ba'
app.config['MAX_CONTENT_LENGTH'] = 10 * 1024 * 1024  # 10MB upload limit
Bootstrap(app)

# Load spaCy model
try:
    nlp = spacy.load("en_core_web_sm")
except:
    import spacy.cli
    spacy.cli.download("en_core_web_sm")
    nlp = spacy.load("en_core_web_sm")

def clean_text(text):
    """Cleans the input text by removing extra whitespaces."""
    return re.sub(r'\s+', ' ', text.strip())

def process_pdf(file):
    """Extracts text from a PDF file."""
    text = ""
    try:
        reader = PdfReader(file)
        for page in reader.pages:
            text += page.extract_text() or ""
    except Exception:
        flash("Failed to read PDF file.", 'danger')
    return text

def generate_mcqs(text, num_questions=5):
    """
    Generates multiple-choice questions from the given text.
    It identifies sentences, selects a subject (noun), replaces it with a blank,
    and generates distractors for choices.
    """
    text = clean_text(text)
    doc = nlp(text)
    sentences = [sent.text for sent in doc.sents if len(sent.text.strip()) > 10]
    
    # Ensure we don't try to select more questions than available sentences
    num_questions = min(num_questions, len(sentences))
    
    # Select random sentences to base MCQs on
    selected = random.sample(sentences, num_questions)
    mcqs = []

    for sent in selected:
        doc = nlp(sent)
        # Find nouns to use as potential subjects for the MCQ
        nouns = [token.text for token in doc if token.pos_ == "NOUN" and not token.is_stop and 2 < len(token.text) < 20]
        
        if len(nouns) < 2:
            # Skip if not enough nouns to create a meaningful MCQ
            continue
        
        subject = random.choice(nouns) # The correct answer
        stem = sent.replace(subject, "______", 1) # The question with a blank
        
        # Create distractors from other nouns
        distractors = list(set(nouns) - {subject})
        random.shuffle(distractors)
        
        # Combine subject and distractors to form choices
        choices = [subject] + distractors[:3]
        
        # Ensure there are always 4 choices, even if not enough unique nouns
        while len(choices) < 4:
            choices.append(f"Option {len(choices)+1}") # Generic options if needed
        
        random.shuffle(choices) # Shuffle the choices
        
        # Determine the correct answer's letter (A, B, C, D)
        correct = chr(65 + choices.index(subject))
        
        mcqs.append((stem, choices, correct))
    return mcqs

@app.route('/', methods=['GET', 'POST'])
def index():
    """Handles file uploads and text input for MCQ generation."""
    if request.method == 'POST':
        text = ""
        files_uploaded = False

        # Process uploaded files
        if 'files[]' in request.files:
            files = request.files.getlist('files[]')
            for file in files:
                if file and file.filename:
                    files_uploaded = True
                    if file.filename.endswith('.pdf'):
                        text += process_pdf(file)
                    elif file.filename.endswith('.txt'):
                        text += file.read().decode('utf-8')

        # Process manual text input if no files were uploaded or no text extracted from files
        if not files_uploaded or not text.strip():
            manual_text = request.form.get('text', '')
            if manual_text.strip():
                text += manual_text

        # If no text is provided at all, show an error
        if not text.strip():
            flash("❗ Please upload a valid file or enter some text.", 'warning')
            return redirect(url_for('index'))

        num = int(request.form['num_questions']) # Get the number of questions requested

        # Generate MCQs
        mcqs = generate_mcqs(text, num)
        return render_template('mcqs.html', mcqs=list(enumerate(mcqs, 1)))

    return render_template('index.html')

# The export_csv route and generate_flashcards function are removed as per the request.

if __name__ == '__main__':
    app.run(debug=True)