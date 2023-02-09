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

def create_request(INPUT):

    # Details on all these variables are available in settings.py
    response = openai.Completion.create(
        model=OPENAI_MODEL,
        prompt=INPUT,
        temperature=TEMPERATURE,
        max_tokens=MAX_TOKENS,
        top_p=TOP_P,
        frequency_penalty=FREQUENCY_PENALTY,
        presence_penalty=PRESENCE_PENALTY,
        stop=STOP_MSG
        )

    return response
