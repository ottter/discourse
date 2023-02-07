import os
import json
import openai
import requests
from settings import *

openai.api_key = OPENAI_API_KEY

# "start" is the name of the AI and is declared in settings.py under AI_NAME
start_sequence = f"\n{STOP_MSG[0]}"
# "restart" the name of chatter and is declared in settings.py under CHATTER_NAME
restart_sequence = f"\n{STOP_MSG[1]}"

def create_request(openai_input):

    # Details on all these variables are available in settings.py
    response = openai.Completion.create(
        model=OPENAI_MODEL,
        prompt=openai_input,
        temperature=0.5,
        max_tokens=25,
        top_p=1.0,
        frequency_penalty=0.5,
        presence_penalty=0.0,
        stop=STOP_MSG
        )

    return response
