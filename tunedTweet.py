import os
import openai
import random
import datetime
from dotenv import load_dotenv

# Generates a tweet based on tuned data (see readme for more)

# Load the API key from the .env file
load_dotenv()
# Set up the API key so OpenAI can authenticate the request'
openai.api_key = os.getenv("OPENAI_API_KEY")

def decideToken(choice):
    if choice == "1":
        max_tokens = input("Max tokens (0-200):\n")
    elif choice == "2":
        max_tokens = str(random.randrange(200))
    else:
        print("Sorry, try again.")
    return max_tokens

def decideTemp(choice):
    if choice == "1":
        temp = input("Temperature (0-1, one decimal place):\n")
    elif choice == "2":
        temp = str(round((random.uniform(0, 1.0)),1))
    else:
        print("Sorry, try again.")
    return temp

# user input, prompt, 1 for manual token & temp, 2 for random
input_prompt = input("Start or style of tweet (or press enter for random):\n")
choice = input("Enter 1 to specify tokens & temp or 2 for random:\n")
max_tokens = decideToken(choice)
temp = decideTemp(choice)

response = openai.Completion.create(
    # engine="text-davinci-002",
    engine="babbage:ft-personal-2022-06-02-04-05-09",
    prompt=input_prompt,
    max_tokens=int(max_tokens),
    temperature=float(temp),
)

# Date time
date_time = datetime.datetime.now()
dt_str = str(date_time)

# Print to response text console
print(response.choices[0].text)

# create txt directory if it doesn't exist
if not os.path.exists('txt'):
   os.makedirs('txt')

# Append the predicted continuation to file
f = open("txt/demofile2.txt", "a")
f.write("\n----tuned tweet----\nDate and time: "+dt_str)
f.write("\n")
f.write("Max tokens: "+max_tokens+" | Temp: "+temp)
f.write("\nPrompt:\n"+input_prompt+"\n")
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
