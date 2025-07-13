import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load .env file
load_dotenv()

# Read API key
api_key = os.getenv("GEMINI_API_KEY")
print("🔑 Using API Key:", api_key[:10] + "...")

# Configure Gemini SDK
genai.configure(api_key=api_key)

# Correct model name
model = genai.GenerativeModel("models/gemini-2.5-pro")


# Test a prompt
def main(userinput):
    try:
        response = model.generate_content(userinput)
        print("✅ Response:", response.text)
    except Exception as e:
        print("❌ Error:", e)

main("Tell me a joke")
