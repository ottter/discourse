"""
Create the API request
"""
import openai
from settings import OPENAI_API_KEY, STOP_MSG, OPENAI_MODEL, TEMPERATURE
from settings import MAX_TOKENS, TOP_P, FREQUENCY_PENALTY, PRESENCE_PENALTY

openai.api_key = OPENAI_API_KEY

# "start" is the name of the AI and is declared in settings.py under AI_NAME
start_sequence = f"\n{STOP_MSG[0]}"
# "restart" the name of chatter and is declared in settings.py under CHATTER_NAME
restart_sequence = f"\n{STOP_MSG[1]}"

def create_request(input_prompt):
    """Function that creates request is sent to OpenAI servers"""

    # Details on all these variables are available in settings.py
    response = openai.Completion.create(
        model=OPENAI_MODEL,
        prompt=input_prompt,
        temperature=TEMPERATURE,
        max_tokens=MAX_TOKENS,
        top_p=TOP_P,
        frequency_penalty=FREQUENCY_PENALTY,
        presence_penalty=PRESENCE_PENALTY,
        stop=STOP_MSG
        )

    return response
