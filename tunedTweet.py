import os
import openai
import random
import datetime

# Generates a tweet based on tuned data
# Using random maximum tokens and temperature

openai.api_key = os.getenv("OPENAI_API_KEY")

# Uncomment 1 or 2 only, not both

# - - - - -
# 1. Uncomment to specify maximum tokens and temperature
max_tokens = input("Max tokens:\n")
temp = input("Temperature:\n")
# Get prompt from user
input_prompt = input("Start or style of tweet:\n")
# - - - - -
# # 2. Uncomment to for random maximum tokens and temperature
# max_tokens = str(random.randrange(200))
# temp = "0."+str(random.randrange(9))
# - - - - -

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

# Append to file
f = open("txt/demofile2.txt", "a")
f.write("\n----------\nTWEET\n----------\n")
f.write(dt_str)
f.write("\n")
f.write(response["choices"][0]["text"])
f.close()