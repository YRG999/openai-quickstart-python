# gpt4chat.py
# Simple GPT-4 chatbot

import os
import openai
import csv
import datetime

# Authenticate
openai.api_key = os.getenv("OPENAI_API_KEY")

# generate chat
def generate_chat(system, user, temperature, max_tokens):
    completion = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": system},
            {"role": "user", "content": user}],
        temperature=float(temperature),
        max_tokens=int(max_tokens),
    )
    # return message
    return completion.choices[0].message.content

# choose system message
def choose_system(system_number):
    if system_number == "1":
        response = input("Enter a system message:\n")
    else:
        response = "You are an expert python programmer"
        print(response)

    return response

# Get max tokens, temp, and prompt from user
system = choose_system(input("Enter '1' to write a custom message or any key for 'You are an expert python programmer'):\n"))
user = input("Ask a question or enter a prompt:\n")
temperature = input("Temperature (0-2 decimal):\n")
max_tokens = input("Max tokens (0-2048, 4000 shared):\n")

# Generate the text
generated_text = generate_chat(system, user, temperature, max_tokens)
print(generated_text)

# Append to CSV
def append_to_csv(file_name, system, user, temperature, max_tokens, generated_text):
    with open(file_name, "a", newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([date_time, "system content: "+system, "user content: "+user, temperature, max_tokens, generated_text])

# Date time
date_time = str(datetime.datetime.now())

# Set your CSV file name
csv_file_name = "csv/output2.csv"

# Append the data to the CSV file
append_to_csv(csv_file_name, system, user, temperature, max_tokens, generated_text)