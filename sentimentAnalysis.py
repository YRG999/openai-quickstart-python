import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

# gather tweets using Scraper
# TODO: create a scraper that gathers tweets from Twitter and saves them to a csv file
# * just one tweet per line in a numbered list with tweets in quotes
# * change any users to @user and urls to http
# * allow the user to input a search query, e.g. "from:username since:2022-01-01 until:2022-12-01"
# * allow the user to input a number of tweets to scrape
# * allow the user to input a file name to save the csv file & save the file to a csv directory

# initialize strings
reader2 = "Classify the sentiment in these tweets:\n\n"
file = "csv/"+input("Enter the name of the csv file to read:\n")+".csv"

# read .csv file and add to string
with open(file, "r") as f:
    for line in f:
        reader2 = reader2 + ''.join(line)

# send to OpenAI and get sentiment analysis response
response = openai.Completion.create(
  model="text-davinci-003",
  prompt=reader2,
  temperature=0,
  max_tokens=60,
  top_p=1.0,
  frequency_penalty=0.0,
  presence_penalty=0.0
)

# TODO: add up the negative & positive scores and print the total
# * calculate the percentage of negative & positive tweets and print the percentages

# print the text of the response
print(response["choices"][0]["text"])

# save the text of the response to a .txt file
with open("txt/sentimentAnalysis.txt", "a") as f:
    f.write("\n----------\n")
    f.write("File="+file+"\n")
    f.write(reader2)
    f.write(response["choices"][0]["text"])
