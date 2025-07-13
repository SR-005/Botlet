from dotenv import load_dotenv
import os
import google.generativeai as genai

#for loading API Key into file
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "gemini-bot-abcdef123456.json"

model = genai.GenerativeModel("gemini-pro")
def main(userinput):
    try:
        #getting respose from api
        response = model.generate_content(userinput)
        botreply=response.text
    except Exception as e:
        botreply = f"Error: {str(e)}"
    print(botreply)
    return botreply

main(userinput="what is the date today?")