LLM MCQ Generator
This is a Flask-based web application that leverages a pre-trained Large Language Model (LLM) and spaCy to generate multiple-choice questions (MCQs) from user-provided text or documents. Users can upload PDF or plain text files, or paste text directly, and the application will generate a specified number of MCQs.

Features
Text Input: Paste text directly into a text area.
LLM MCQ Generator
This is a Flask-based web application that leverages a pre-trained Large Language Model (LLM) and spaCy to generate multiple-choice questions (MCQs) from user-provided text or documents. Users can upload PDF or plain text files, or paste text directly, and the application will generate a specified number of MCQs.
Features
* Text Input: Paste text directly into a text area.
* File Upload: Upload .pdf or .txt files.
* MCQ Generation: Automatically creates multiple-choice questions with a question stem, choices, and the correct answer.
* User-friendly Interface: Simple and intuitive web interface.
Setup
To run this project locally, follow these steps:
1. Clone the repository (if applicable) or download the project files.
2. Create a virtual environment (recommended):
python -m venv venv

3. Activate the virtual environment:
   * On Windows:
.\venv\Scripts\activate

   * On macOS/Linux:
source venv/bin/activate

      4. Install the required Python packages:
pip install Flask Flask-Bootstrap spacy PyPDF2 transformers

      5. Download the spaCy English model:
python -m spacy download en_core_web_sm

      6. Ensure your project structure is correct:
your-project-folder/
├── app.py
├── static/
│   └── style.css
├── templates/
│   ├── index.html
│   └── mcqs.html
└── venv/

Make sure style.css is inside a static folder and index.html and mcqs.html are inside a templates folder.
      7. Run the Flask application:
python app.py

      8. Access the application: Open your web browser and go to http://127.0.0.1:5000/.
Usage
         1. Input Text:
         * Upload File(s): Click on "Choose Files" and select one or more .pdf or .txt files from your computer.
         * Paste Text: Alternatively, paste your desired text directly into the provided text area.
         2. Select Number of Questions: Choose the desired number of MCQs to generate from the dropdown menu (e.g., 5, 10, 15).
         3. Generate MCQs: Click the "Generate MCQs" button.
         4. View Generated MCQs: The application will display the generated multiple-choice questions on a new page, showing the question stem, options, and the correct answer.
         5. Generate More: Click "Generate More" to return to the input page and generate new MCQs.
Sample Output
Here's an example of what the generated MCQs might look like (actual output will vary based on input text):
1. The Amazon rainforest is the largest rainforest in the world, covering an immense area across nine South American countries, primarily Brazil, Peru, and ______.
  A. Argentina
  B. Colombia
  C. Ecuador
  D. Venezuela
  Correct Answer: B

2. Deforestation, mainly due to cattle ranching and ______, poses a significant threat to this invaluable natural resource and its inhabitants.
  A. mining
  B. fishing
  C. agriculture
  D. logging
  Correct Answer: C

3. The Amazon River, which flows through the rainforest, is the second-longest river globally and plays a vital role in the region's ______.
  A. economy
  B. climate
  C. ecosystem
  D. culture
  Correct Answer: C
File Upload: Upload .pdf or .txt files.

MCQ Generation: Automatically creates multiple-choice questions with a question stem, choices, and the correct answer.

User-friendly Interface: Simple and intuitive web interface.

Setup
To run this project locally, follow these steps:

Clone the repository (if applicable) or download the project files.

Create a virtual environment (recommended):

python -m venv venv

Activate the virtual environment:

On Windows:

.\venv\Scripts\activate

On macOS/Linux:

source venv/bin/activate

Install the required Python packages:

pip install Flask Flask-Bootstrap spacy PyPDF2 transformers

Download the spaCy English model:

python -m spacy download en_core_web_sm

Ensure your project structure is correct:

your-project-folder/
├── app.py
├── static/
│   └── style.css
├── templates/
│   ├── index.html
│   └── mcqs.html
└── venv/

Make sure style.css is inside a static folder and index.html and mcqs.html are inside a templates folder.

Run the Flask application:

python app.py

Access the application: Open your web browser and go to http://127.0.0.1:5000/.

Usage
Input Text:

Upload File(s): Click on "Choose Files" and select one or more .pdf or .txt files from your computer.

Paste Text: Alternatively, paste your desired text directly into the provided text area.

Select Number of Questions: Choose the desired number of MCQs to generate from the dropdown menu (e.g., 5, 10, 15).

Generate MCQs: Click the "Generate MCQs" button.

View Generated MCQs: The application will display the generated multiple-choice questions on a new page, showing the question stem, options, and the correct answer.

Generate More: Click "Generate More" to return to the input page and generate new MCQs.

Sample Output
Here's an example of what the generated MCQs might look like (actual output will vary based on input text):

1. The Amazon rainforest is the largest rainforest in the world, covering an immense area across nine South American countries, primarily Brazil, Peru, and ______.
   A. Argentina
   B. Colombia
   C. Ecuador
   D. Venezuela
   Correct Answer: B

2. Deforestation, mainly due to cattle ranching and ______, poses a significant threat to this invaluable natural resource and its inhabitants.
   A. mining
   B. fishing
   C. agriculture
   D. logging
   Correct Answer: C

3. The Amazon River, which flows through the rainforest, is the second-longest river globally and plays a vital role in the region's ______.
   A. economy
   B. climate
   C. ecosystem
   D. culture
   Correct Answer: C
