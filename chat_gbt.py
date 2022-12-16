from pyChatGPT import ChatGPT
from secret import SESSION_TOKEN

# Function to get 
def get_response(prompt):
    api = ChatGPT(SESSION_TOKEN)
    response = api.send_message(prompt + " (in 1-3 sentences)")
    api.close()
    return response["message"]