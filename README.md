# Academic Paper Summarizer

## Project Overview
This repository contains two different applications for summarizing academic papers:

### 1. **Streamlit-Based Application**
A lightweight, user-friendly web app built with **Streamlit** that allows users to:
- Upload PDF files.
- Generate an in-depth AI-powered synopsis of the paper using AI.
- View structured paragraphs and bullet-point lists (methods, discussions, key statistics, citations).

### 2. **Standalone Flask Backend + React Frontend**
A more traditional web app setup consisting of:
- A **Flask backend** for handling file uploads, PDF text extraction, and GPT summarization.
- A **React + Tailwind frontend** for file uploading and displaying summaries in a formatted UI.

---

## Features
- PDF Upload support.
- Automatic detection of academic papers (with fallback messaging if not detected).
- Multi-paragraph synopsis generation.
- Display of methods, discussions, key statistics, and citations as bullet lists.
- Clean UI to show information clearly.
- Secure API key handling via `.env` (locally) and `st.secrets` (for Streamlit Cloud).

---

## Repository Structure
```
/streamlit_app
  └── SummarizeStreamlit.py   # Streamlit app code
  └── requirements.txt        # Dependencies

/backend
  └── app.py                  # Flask backend routes
  └── gpt_summarizer.py       # GPT call logic
  └── .env.example            # Example environment variables

/frontend
  └── React app for file upload and summary viewing
  └── components/             # React components (FileUploader, SummaryViewer)
```

---

## How to Run Locally

### **Streamlit App:**
1. Clone the repository.
2. Navigate to `/streamlit_app`.
3. Create a `.env` file or use `st.secrets` for `OPENAI_API_KEY`.
4. Install dependencies:
```
pip install -r requirements.txt
```
5. Run the app:
```
streamlit run SummarizeStreamlit.py
```

### **Flask + React App:**
- Follow the setup instructions in the `/backend` and `/frontend` directories for backend and frontend installation.
- Make sure your `OPENAI_API_KEY` is stored in the backend `.env` file.
- Run `app.py` and the frontend separately.
- Navigate to `/frontend` and use `npm start` to start frontend.

---

## Deployment
- The Streamlit app is deployable to **Streamlit Cloud**. Use `st.secrets` for securely managing API keys.
- Flask + React can be deployed on platforms like Heroku, Railway, or Vercel.

---

## Future Improvements
- PDF export of summaries.
- Copy-to-clipboard buttons.
- Optional keyword extraction.
- Enhanced visual charts for statistics.

---

