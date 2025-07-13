import os
from dotenv import load_dotenv
import google.generativeai as genai
import json

#for loading API Key into file
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Configure the model
genai.configure()

model = genai.GenerativeModel(model_name="models/gemini-pro")

def main(userinput):
    try:
        response=model.generate_content(userinput)
        botreply=response.text    

    except Exception as e:
        botreply = f"Error: {str(e)}"

    print(botreply)
    return botreply

main("what is the date today?")