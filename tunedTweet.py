import os
import openai
import random
import datetime

# Generates a tweet based on tuned data
# Using random maximum tokens and temperature

openai.api_key = os.getenv("OPENAI_API_KEY")

def decideToken(choice):
    if choice == "1":
        max_tokens = input("Max tokens:\n")
    elif choice == "2":
        max_tokens = str(random.randrange(200))
    else:
        print("Sorry, try again.")
    return max_tokens

def decideTemp(choice):
    if choice == "1":
        temp = input("Temperature:\n")
    elif choice == "2":
        temp = str(round((random.uniform(0, 1.0)),1))
    else:
        print("Sorry, try again.")
    return temp

# # 1. Uncomment to specify maximum tokens and temperature
# max_tokens = input("Max tokens:\n")
# temp = input("Temperature:\n")
# # Get prompt from user
# # - - - - -
# # # 2. Uncomment to for random maximum tokens and temperature
# # max_tokens = str(random.randrange(200))
# # temp = "0."+str(random.randrange(9))

# user input, prompt, 1 for manual token & temp, 2 for random
input_prompt = input("Start or style of tweet:\n")
choice = input("Enter 1 to specify tokens & temp or 2 for random:\n")
max_tokens = decideToken(choice)
temp = decideTemp(choice)

# print("Max tokens (0-200)= ",max_tokens,"| Temperature (0-1, decimal)= ",temp)
token_temp = ("Max tokens (0-200)= ",max_tokens,"| Temperature (0-1, decimal)= ",temp)

response = openai.Completion.create(
    # engine="text-davinci-002",
    engine="babbage:ft-personal-2022-06-02-04-05-09",

# Use `input_prompt` for option 1 and null prompt for option 2
#    prompt="",
    prompt=input_prompt,
    max_tokens=int(max_tokens),
    temperature=float(temp),
)

# Date time
date_time = datetime.datetime.now()
dt_str = str(date_time)

# Print to console
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