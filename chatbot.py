import os
from dotenv import load_dotenv
import google.generativeai as genai

#API Fetch Function
def main(userinput):
    print("-----entered mainfun------")
    #Load and Read API Ket from .env file
    load_dotenv()
    api_key = os.getenv("GEMINI_API_KEY")

    #configure Gemini SDK
    genai.configure(api_key=api_key)
    #setting up gemini model
    model = genai.GenerativeModel("models/gemini-2.5-pro")
    try:
        response = model.generate_content(userinput)
        return response.text
    except Exception as e:
        return f"Error: {e}"

#print(main("Tell me a joke"))
