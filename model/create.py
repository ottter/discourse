import os
import json
import openai
import requests
from settings import *

openai.api_key = OPENAI_API_KEY

# "start" is the name of the AI and "restart" the name of chatter
# declared in settings.py under AI_NAME and CHATTER_NAME
start_sequence = f"\n{STOP_MSG[0]}"
restart_sequence = f"\n{STOP_MSG[1]}"

def create_request(openai_input):

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
