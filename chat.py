import os

import openai
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.environ.get('OPENAI_KEY')


def chat(messages):
    return openai.ChatCompletion.create(
        model="gpt-3.5-turbo", messages=messages, temperature=0, max_tokens=4000)
