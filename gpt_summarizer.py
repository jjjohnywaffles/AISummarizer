import os
import openai
from dotenv import load_dotenv
import json
import re

load_dotenv()
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def summarize_with_gpt(text):
    prompt = (
        "Begin by providing the authors' names and the title of the article. "
        "Segment this academic paper into the following sections: Introduction, Methods, Results, Discussion, and Conclusion. "
        "For each section, provide a concise summary in bullet points. Additionally, list any important statistics or percentages found in the paper in a separate list. "
        "Provide a list of citations the paper utilized. "
        "Respond with strictly valid JSON, with keys: 'title', 'authors', 'introduction', 'methods', 'results', 'discussion', 'conclusion', 'statistics', and 'citations'."
        f"\\n\\nPaper content:\\n{text[:3000]}\\n\\nJSON:"
    )

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are an assistant that reads academic papers and outputs structured JSON summaries with section-based bullet points and statistics."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=5000,
            temperature=0.2
        )

        summary_text = response.choices[0].message.content
        print(f"GPT structured response received: {summary_text}")

        # ✅ Strip markdown code block formatting
        cleaned_text = re.sub(r'```json|```', '', summary_text).strip()

        # ✅ Parse the cleaned JSON
        summary_json = json.loads(cleaned_text)
        return summary_json

    except openai.OpenAIError as e:
        print(f"OpenAI API Error: {e}")
        return "GPT summarization failed due to API error."
    except Exception as e:
        print(f"Unexpected Error: {e}")
        return "GPT summarization failed due to unexpected error."