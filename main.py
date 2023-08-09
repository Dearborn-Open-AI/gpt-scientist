from dotenv import load_dotenv

import os

from prompt_toolkit import prompt
from prompt_toolkit.shortcuts import message_dialog
from prompt_toolkit.styles import Style as PromptStyle

from colorama import Fore

import openai

load_dotenv()

openai.api_key = os.environ.get("OPENAI_API_KEY")

# Define style
style = PromptStyle.from_dict(
    {
        "dialog": "bg:#88ff88",
        "button": "bg:#ffffff #000000",
        "dialog.body": "bg:#44cc44 #ffffff",
        "dialog shadow": "bg:#003800",
    }
)


def api_call(conversation):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", messages=conversation, temperature=0.7
    )
    return response



def get_input(data):
    system_prompt = {
        "role": "system",
        "content": "You are looking to discover basic truths via the scientific method. ",
    }
    content_data = f"Observation:{data}"
    user_prompt = {"role": "user", "content": content_data}
    conversation = [system_prompt, user_prompt]
    response = api_call(conversation)
    print(response)
    print(Fore.GREEN + f"gpt-scientist: {response}", end="")


def main():
    message_dialog(
        title="gpt-scientist",
        text="This is a chatbot that will help you discover basic truths via the scientific method.",
        style=style,
    ).run()

    os.system("clear")  # Clears the terminal screen

    data = prompt("Enter in the data: ")

    os.system("clear")  # Clears the terminal screen

    # Now use the provided initial message
    get_input(data)


if __name__ == "__main__":
    main()
