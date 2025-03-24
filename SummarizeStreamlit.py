import streamlit as st
import fitz  # PyMuPDF
import openai
import os
import re
import json
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
openai.api_key = st.secrets["OPENAI_API_KEY"]

# GPT summarizer function
def summarize_with_gpt(text):
    prompt = (
        "Provide a structured, in-depth synopsis of the following academic paper. "
        "First, write 2-3 detailed paragraphs explaining the paper's objectives, methodology, and key findings. Use clear line breaks to separate paragraphs. "
        "Then, include concise bullet-point lists for methods, discussions, important statistics, and notable citations. "
        "If the provided text is not detected to be from an academic or research paper, respond with: 'This document is not an academic paper and cannot be summarized.' "
        "Format the response in JSON with keys: 'authors', 'synopsis_paragraphs', 'methods', 'discussions', 'statistics', and 'citations'. "
        f"\n\nPaper content:\n{text[:3000]}\n\nJSON:"
    )

    try:
        client = openai.OpenAI()
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are an assistant that reads academic papers and outputs structured, readable synopses with paragraphs and bullet lists."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=4000,
            temperature=0.2
        )

        summary_text = response.choices[0].message.content
        cleaned_text = re.sub(r'```json|```', '', summary_text).strip()
        summary_json = json.loads(cleaned_text)
        return summary_json

    except Exception as e:
        st.error(f"Error calling GPT API: {e}")
        return None

# Streamlit app UI
st.title("📚 Academic Paper Synopsis Generator")

uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")

if uploaded_file is not None:
    st.info("Processing and Summarizing...")

    # Extract text from PDF
    doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()

    summary = summarize_with_gpt(text)

    if summary:
        st.success("Synopsis generated successfully!")
        st.subheader("📖 In-Depth Synopsis")

        if summary.get('authors'):
            st.write(f"**Authors:** {', '.join(summary['authors'])}")

        for paragraph in summary.get('synopsis_paragraphs', []):
            st.write(paragraph)
            st.write("\n")

        if summary.get('methods'):
            st.subheader("🧪 Methods")
            for method in summary['methods']:
                st.write(f"- {method}")

        if summary.get('discussions'):
            st.subheader("💬 Discussions")
            for discussion in summary['discussions']:
                st.write(f"- {discussion}")

        if summary.get('statistics'):
            st.subheader("📊 Key Statistics")
            for stat in summary['statistics']:
                st.write(f"- {stat}")

        if summary.get('citations'):
            st.subheader("📚 Notable Citations")
            for citation in summary['citations']:
                st.write(f"- {citation}")

        st.balloons()