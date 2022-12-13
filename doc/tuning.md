# Fine tuning

I fine tuned the openai babbage engine with 568 Tweets by Elon Musk from May 2022 and I've been playing around with it. 

1. I grabbed the Tweets using [snscrape](https://github.com/JustAnotherArchivist/snscrape) as a Python library as described in [How to Scrape Tweets With snscrape](https://betterprogramming.pub/how-to-scrape-tweets-with-snscrape-90124ed006af) (see [Scraper](https://github.com/YRG999/Scraper) for my fork with a working example).

2. In a Google Sheet, I created two columns, prompts and completions, as described in the [cli prep tool doc](https://beta.openai.com/docs/guides/fine-tuning/cli-data-preparation-tool). I added empty prompts and used Elon's Tweets as completions, saved as a CSV file, then used the prep tool to prepare the JSONL file. See [Example CSV and table](#example-tweet-csv-and-table) for details.

3. I followed the [fine tuning](https://beta.openai.com/docs/guides/fine-tuning) steps to train a model, then created a Python program to randomize the max tokens between 0-200 and temperature between 0-1. That's the code in `tunedTweet.py`.

## Example CSV and table

I used empty prompts so that when I entered an empty prompt, I'd get back a generated Elon Tweet. Openai used the completions from the empty prompts as an example dataset of tweets.

Here's an example of the Google sheet:

prompt | completion
--- | ---
&nbsp; | @Cernovich No kidding …
&nbsp; | @pmarca Humans
&nbsp; | "@GovMikeHuckabee Authentication is important, but so is anonymity for many. A balance must be struck."

Here's an example of the exported CSV:

```
prompt,completion
,@Cernovich No kidding …
,@pmarca Humans
,"@GovMikeHuckabee Authentication is important, but so is anonymity for many. A balance must be struck."
```