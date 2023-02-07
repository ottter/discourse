# discourse

Chatbot that uses OpenAI API. I aim to develop it into a plug-n-play Discord bot module after it is fine-tuned.

## Quickstart

Update `settings.py` with desired config. Note the line where values below it should *not* be changed

    OPENAI_API_KEY= replace with key(string) or use env var
    CHATTER_NAME= string for what to save user text as
    AI_NAME= string for what to save AI text as
    OPENAI_MODEL= ada > babble >> curry >>> davinci

> `settings.py` has more indepth information on what each of these values does

Install required Python packages and run the script

    pip install -r requirements.txt
    python3 main.py

## Important Links

[Environment Varibales on Windows](https://docs.oracle.com/en/database/oracle/machine-learning/oml4r/1.5.1/oread/creating-and-modifying-environment-variables-on-windows.html)

[Prompt Generation](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-openai-api)
