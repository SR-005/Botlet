from dotenv import load_dotenv
import os
import openai

#for loading API Key into file
load_dotenv()
apikey = os.getenv("API_KEY")

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

    except:
        pass
    botreply=""
    return botreply