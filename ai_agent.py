import google.generativeai as genai
import os


API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError(" API key not found. Set GEMINI_API_KEY environment variable.")

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel(model_name="gemini-1.5-flash")

def ask_gemini(prompt):
    response = model.generate_content(prompt)
    return response.text
