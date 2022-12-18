import os
import openai
import snscrape.modules.twitter as sntwitter
import pandas as pd
import re
from collections import Counter

openai.api_key = os.getenv("OPENAI_API_KEY")

# create txt directory if it doesn't exist
if not os.path.exists('txt'):
   os.makedirs('txt')

# create csv directory if it doesn't exist
if not os.path.exists('csv'):
   os.makedirs('csv')

def processTweet (tweet):
    tweet_words = []
    tweet_proc = ""
    for i in range(len(tweet)):
        tweet = tweet.replace(",", ". ", 1)
    for word in tweet.split(' '):
        if word.startswith('@') and len(word) > 1:
            word = '@user'
        elif word.startswith('\"@') and len(word) > 1:
            word = '\"@user'
        elif word.startswith('http'):
            word = "http\n"
        tweet_words.append(word)
    tweet_proc = " ".join(tweet_words)
    return(tweet_proc)

def count_words(s):
    # use a regular expression to find all the words in the string
    words_pattern = '[a-z]+'  # match any word that contains only letters
    words = re.findall(words_pattern, s, flags=re.IGNORECASE)
    # create a Counter object and return the count of each word
    return Counter(words)

def scrapeTweets():
    # Scrapes tweets & saves to /csv

    # User input
    tweet_file = "csv/"+input("Enter the name of the csv file to save tweets:\n")+".csv"
    max_num = int(input("Enter the number of tweets to scrape:\n"))
    search_term = input("Enter the search term:\n(e.g. from:username since:2022-01-01 until:2022-12-01)\n")

    tweet_list = []

    # get tweets; save to csv file
    for i,tweet in enumerate(sntwitter.TwitterSearchScraper(search_term).get_items()):
        if i > (max_num - 1):
            break
        tweet_list.append([tweet.content])
    tweets_df = pd.DataFrame(tweet_list)
    tweets_df.to_csv(tweet_file)

def sentimentAnalysis():
    # Run sentiment analysis on csv

    # User input
    file = "csv/"+input("Enter the name of the csv file to read:\n")+".csv"

    # create prompt with csv
    reader2 = "Classify the sentiment in these tweets:\n\n"
    with open(file, "r") as f:
        for line in f:
            line = processTweet(line)
            reader2 = reader2 + ''.join(line)

    # send to OpenAI and get sentiment analysis response
    response = openai.Completion.create(
    model="text-davinci-003",
    prompt=reader2,
    temperature=0,
    max_tokens=1200,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=0.0
    )

    # Count words in response and print
    response_updated =  response["choices"][0]["text"]
    response_word_count = count_words(response_updated)
    print(response_word_count)

    # save the text of the response to a .txt file
    with open("txt/sentimentAnalysis.txt", "a") as f:
        f.write("\n----------\n")
        f.write("File="+file+"\n")
        f.write(reader2)
        f.write(response_updated+"\n")
        f.write(str(response_word_count))

# User input: choose 1 or 2
choice = input("Enter 1 for both or 2 for just sentiment analysis:\n")
if choice == "1":
    scrapeTweets()
    sentimentAnalysis()
elif choice == "2":
    sentimentAnalysis()
else:
    print("Sorry, try again.")
