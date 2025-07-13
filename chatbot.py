import os
import google.generativeai as genai
import json

#for loading API Key into file
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "directed-craft-465717-c8-d655a7741d5c.json"

# Configure the model
genai.configure()

model = genai.GenerativeModel("gemini-pro")
def main(userinput):
    try:
        response=model.generate_content(user_input)
        botreply=response.text    

    except Exception as e:
        botreply = f"Error: {str(e)}"

    print(botreply)
    return botreply

main("what is the date today?")