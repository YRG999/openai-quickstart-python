# gpt4code.py
# Output code from GPT-4

import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

completion = openai.ChatCompletion.create(
  model="gpt-4",
  messages=[
        {"role": "system", "content": "You are an expert python programmer."},
        {"role": "user", "content": "Create a simple hello world python program. Do not explain it."}
    ]
)

print(completion.choices[0].message)