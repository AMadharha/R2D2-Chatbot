from pyChatGPT import ChatGPT
from secret import SESSION_TOKEN

def get_response(text):
    api = ChatGPT(SESSION_TOKEN)
    response = api.send_message(text + " (in 1-3 sentences)")
    api.close()
    return response["message"]