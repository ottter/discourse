import os
import json
import openai
import requests
from settings import *

openai.api_key = OPENAI_API_KEY

openai_prompt = input('Text:')

response = openai.Completion.create(
  model=OPENAI_MODEL,
  prompt=openai_prompt,
  temperature=0.5,
  max_tokens=25,
  top_p=1.0,
  frequency_penalty=0.5,
  presence_penalty=0.0,
  stop=["You:"]
)

# print(response["choices"][0]["text"])
print(response)
