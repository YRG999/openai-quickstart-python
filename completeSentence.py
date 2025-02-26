# completeSentence.py
# Simple GPT-3 CLI to that completes sentences.
# The start of this code was generated by asking chatGPT how to create a completion in python.

import os
import openai
import datetime
from dotenv import load_dotenv

# Load the API key from the .env file
load_dotenv()
# Set up the API key so OpenAI can authenticate the request
openai.api_key = os.getenv("OPENAI_API_KEY")

# Get max tokens, temp, and prompt from user
max_token_val = input("Max tokens:\n")
temp_val = input("Temperature:\n")
input_prompt = input("Ask a question or enter a prompt:\n")

# Use the `completion` endpoint to get a predicted continuation of a given text
response = openai.Completion.create(
    engine="text-davinci-003",
    prompt=input_prompt,
    # temperature=0.5,
    # max_tokens=200,
    temperature=float(temp_val),
    max_tokens=int(max_token_val),
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
)

# Date time
date_time = datetime.datetime.now()
dt_str = str(date_time)

# Print the predicted continuation to console
print(response["choices"][0]["text"])

# create txt directory if it doesn't exist
if not os.path.exists('txt'):
   os.makedirs('txt')

# Append the predicted continuation to file
f = open("txt/demofile2.txt", "a")
f.write("\n----complete sentence----\nDate and time: ")
f.write(dt_str)
f.write("\n")
f.write("Temperature: ")
f.write(temp_val)
f.write("\n")
f.write("Max tokens: ")
f.write(max_token_val)
f.write("\n")
f.write("Prompt:\n")
f.write(input_prompt)
f.write("\n")
f.write("Response:\n")
f.write(response["choices"][0]["text"])
f.close()

# remove empty lines from sentimentAnalysis.txt
with open('txt/demofile2.txt', 'r+') as file:
    # Read all lines in the file
    lines = file.readlines()
    # Seek to the beginning of the file
    file.seek(0)
    # Iterate through all lines
    for line in lines:
        # If the line is not empty, write it to the file
        if line.strip():
            file.write(line)
    # Truncate the file to remove any excess lines
    file.truncate()
