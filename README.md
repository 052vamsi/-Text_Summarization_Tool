# Text Summarization Tool

A Django-based web application for summarizing large chunks of text into concise summaries.

## Features
- Paste or upload text for summarization
- Custom text summarization using NLTK
- Editable summaries
- Basic text formatting options
- Clean and intuitive user interface

## Setup
1. Create a virtual environment:
   ```
   python -m venv venv
   ```
2. Activate the virtual environment:
   ```
   .\venv\Scripts\activate
   ```
3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
4. Run migrations:
   ```
   python manage.py migrate
   ```
5. Run the development server:
   ```
   python manage.py runserver
   ```

## Usage
1. Visit http://127.0.0.1:8000 in your web browser
2. Paste or upload text in the input area
3. Click "Summarize" to generate a summary
4. Edit the summary if needed
5. Copy or download the summary
