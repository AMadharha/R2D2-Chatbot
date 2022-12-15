from pyChatGPT import ChatGPT
from secret import SESSION_TOKEN

def get_chat_gpt_response(text):
    session_token = SESSION_TOKEN
    api = ChatGPT(session_token)
    response = api.send_message(text + " (in 1-2 sentences)")
    api.close()
    return response["message"]