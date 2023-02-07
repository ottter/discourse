from settings import *
from model.create import create_request

def main():
    openai_input = input('Text:')
    
    # openai_input is used as the prompt that all conversation is based on, along with the base pretrained model. 
    # check README.md > Important Links for more info on creating a good prompt
    response = create_request(openai_input)
    print(response)

    prompt_response = response['choices'][0]['text'].replace('\n', '')
    # Save all conversations in a file that will be used as the prompt for future conversations
    prompt_file = open("prompts/generated_prompt.txt", "a")
    prompt_file.write(f"{STOP_MSG[1]} {openai_input}\n{STOP_MSG[0]} {prompt_response}\n")
    prompt_file.close()

    return

if __name__ == "__main__":
    main()