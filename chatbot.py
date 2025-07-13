from dotenv import load_dotenv
import os
import openai

#for loading API Key into file
load_dotenv()
apikey = os.getenv("API_KEY")

model = genai.GenerativeModel("gemini-pro")
def main(userinput):
    try:
        #getting respose from api
        response=openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
             messages=[
                    {"role": "system", "content": "You are a helpful and friendly chatbot."},
                    {"role": "user", "content": userinput}
                ]
        )
        #selecting respose to user from api return
        botreply = response["choices"][0]["message"]["content"].strip()
    except Exception as e:
        botreply = f"Error: {str(e)}"
    print(botreply)
    return botreply

main(userinput="what is the date today?")