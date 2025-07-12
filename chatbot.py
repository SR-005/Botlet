from dotenv import load_dotenv
import os
import openai

#for loading API Key into file
load_dotenv()
apikey = os.getenv("API_KEY")

def main(userinput):
    try:
        response=openai.ChatCompletion.create()
    except:
        pass
    botreply=""
    return botreply