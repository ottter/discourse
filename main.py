"""
Main function that controls the rest of the program
"""
from settings import CHATTER_NAME, AI_NAME, STOP_MSG
from model.create import create_request

def main():
    """Initiate the API request and save conversation history to text file"""
    active_conversation = True

    # openai_prompt is used as the prompt that all conversation is based on (on top of model)
    # check README.md > Important Links for more info on creating a good prompt
    with open("prompts/default_prompt.txt", "r", encoding='utf-8') as file:
        prompt = file.read().rstrip()

    while active_conversation:
        openai_input = input(f'{CHATTER_NAME}: ')

        if openai_input in ["quit", "exit"]:
            break

        openai_prompt = f"{prompt}\n\n{openai_input}"

        response = create_request(openai_prompt)
        total_tokens = response['usage']['total_tokens']
        prompt_response = response['choices'][0]['text'].replace('\n', '')
        print(f"{AI_NAME}: {prompt_response} ({total_tokens})")

        # Save all conversations in a file that will be used as the prompt for future conversations
        with open("prompts/conversation_history.txt", "a", encoding='utf-8') as file:
            file.write(f"{STOP_MSG[1]} {openai_input}\n{STOP_MSG[0]} {prompt_response}\n")
            file.close()

if __name__ == "__main__":
    main()
