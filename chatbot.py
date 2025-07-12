from dotenv import load_dotenv
import os
import openai
from openai import OpenAI
from dotenv import load_dotenv

#for loading API Key into file
load_dotenv()
client = OpenAI()

def main(userinput):
    try:
        #getting respose from api
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful and friendly chatbot."},
                {"role": "user", "content": userinput}
            ]
        )
        botreply = response.choices[0].message.content.strip()
    except Exception as e:
        botreply = f"Error: {str(e)}"
    print(botreply)
    return botreply

main(userinput="what is the date today?")