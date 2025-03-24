import os
from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
from dotenv import load_dotenv
import fitz  # PyMuPDF
import uuid
from gpt_summarizer import summarize_with_gpt
from flask_cors import CORS

# Load environment variables
load_dotenv()

UPLOAD_FOLDER = os.getenv("UPLOAD_FOLDER", "uploads")
ALLOWED_EXTENSIONS = {'pdf'}
MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB max upload size

app = Flask(__name__)
CORS(app)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = MAX_CONTENT_LENGTH

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def extract_text_from_pdf(filepath):
    doc = fitz.open(filepath)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file part in request"}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No file selected"}), 400

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_id = str(uuid.uuid4())
        saved_path = os.path.join(app.config['UPLOAD_FOLDER'], f"{file_id}_{filename}")
        file.save(saved_path)

        try:
            extracted_text = extract_text_from_pdf(saved_path)
            summary_data = summarize_with_gpt(extracted_text)
        except Exception as e:
            return jsonify({"error": f"Failed to process PDF: {e}"}), 500
        finally:
            os.remove(saved_path)

        return jsonify({"summary": summary_data}), 200

    return jsonify({"error": "Invalid file type"}), 400

@app.route('/')
def home():
    return "Academic Paper Visual Summarizer API is running. Use POST /upload to submit PDFs."

if __name__ == "__main__":
    app.run(debug=False, port=5000)
