import os
from dotenv import load_dotenv
from prompt_toolkit import prompt
from prompt_toolkit.shortcuts import message_dialog
from prompt_toolkit.styles import Style as PromptStyle

from colorama import Fore

import openai

load_dotenv()

openai.api_key = os.environ.get("OKEY")

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
    """
    Calls chat api endpoint
    """
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", messages=conversation, temperature=0.7
    )
    return response


def get_input(data):
    """
    Gets the input from the terminal 
    """
    system_content = """
You will observe some phenomenon and use the scientific method to form a better understanding of such phenomonon. Use established method of scientific inquiry. 
Observation: Observing something of interest in the natural world.
Questioning: Formulating a clear and concise question about a phenomenon.
Literature Review: Doing a thorough review of the existing research to find out what is already known about the subject.
Hypothesis Formation: Developing a testable hypothesis or prediction that can be examined through experimentation. A hypothesis often takes the form of a statement that can either be supported or refuted through observation or experimentation.
Experimentation: Designing and conducting an experiment to test the hypothesis. This includes identifying variables and controls, collecting data, and ensuring that the experiment is replicable.
Data Collection and Analysis: Gathering and analyzing the data from the experiment to determine whether it supports or refutes the hypothesis. This includes using statistical methods to interpret the data.
Conclusion: Drawing a conclusion based on the data analysis. This might support the original hypothesis, or lead to the formation of a new hypothesis.
Communication: Publishing the findings in a scientific journal or other venue so that others can review and replicate the work. This also includes discussing the implications of the findings, the limitations of the study, and suggesting further research.
Reiteration: If the results call the original hypothesis into question, the process may start again with a new hypothesis.
Replication: Other researchers attempt to replicate the findings to see if they hold true in different circumstances or under slightly different conditions. Replication is essential for establishing the validity and reliability of scientific findings.

Because we will operate in a contained environment we will only conduct the observation, questioning, and hypothesis formation steps. You may move between these steps freely as you formulate your ideas but please complete the task with a hypothesis. 

At each step (observation, questioning, hypothesis), include your current thinking as well as what action you will take next to continue to improve your hypothesis. See an example below. 

__
Phenomenon: You drop a feather and a hammer on earth. The hammer hits the ground first.

{ 
    "observation": "The feather drops slower than the hammer in earths gravity.",
    "thought": "There must be a difference between the feather and the hammer. I wonder if other factors could be at play."
    "action": "I will drop the feather and hammer in a vacuum to see if the results are the same."
}

"""
    system_prompt = {
        "role": "system",
        "content": system_content,
    }
    content_data = f"Phenomenon:{data}"
    user_prompt = {"role": "user", "content": content_data}
    conversation = [system_prompt, user_prompt]
    response = api_call(conversation)
    print(response)
    print(Fore.GREEN + f"gpt-scientist: {response}", end="")


def main():
    """
    is the main thing
    """
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
