import os

# TODO: validation checks on all variables below
# TODO: Split out python code from .yaml tier data to create proper settings file

###
### SECRETS

OPENAI_API_KEY= os.getenv("OPENAI_API_KEY")

###
### GENERAL

# Name of the chatter that will be attached to it's messages in conversation history. Example: "Deckard"
CHATTER_NAME="James"

# Name of the AI that will be attached to it's messages in conversation history. Example: "Roy"
AI_NAME="Bardock"

###
### OPENAI

# Pretrained models in order of complexity: ada, babbage, curie, davinci
OPENAI_MODEL="davinci"

# Controls randomness. 0.00 to 1.00
TEMPERATURE=0.5

# Length of tokens between prompt and completion. 1 token = 4 characters. Max=4000 (INT)
MAX_TOKENS=300

# Controls diversity. Range: 0.00 to 1.00
TOP_P=1.0

# Decreases chances of repeating the same line. Range: 0.00 to 2.00
FREQUENCY_PENALTY=0.5

# Higher more likely to talk about new subjects. Range: 0.00 to 2.00 
PRESENCE_PENALTY=0.0

##########
######################## BELOW HERE SHOULD NOT BE EDITTED ########################

MODEL_DICT = {
    "ada" : "text-ada-001",
    "babbage" : "text-babbage-001",
    "curie" : "text-curie-001",
    "davinci" : "text-davinci-003",
}
OPENAI_MODEL = MODEL_DICT.get(OPENAI_MODEL).lower()
assert OPENAI_MODEL

# Where it will stop generating further tokens. Max entries: 4. (List)
STOP_MSG=[f"{AI_NAME}:", f"{CHATTER_NAME}:"]