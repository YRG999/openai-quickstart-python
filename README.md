# Readme <!-- omit in toc -->

- [Apps](#apps)
- [Activate venv](#activate-venv)
- [Run app](#run-app)
- [Related](#related)

## Apps

1. [Python example app](/doc/originalREADME.md) - follow these steps first to generate your virtual env with dependencies and put your OPENAI_API_KEY in an .env file and test your integration.
2. `completeSentence.py` - completes your sentence when you add a prompt.
Some things to try "A long time ago in a galaxy far, far away..." or "The quick brown fox ". You can also request prompts in a style of writing, or other things, such as "Write a scene from the tv show Mad Men with Don Draper in 1980's New York: "
3. `tunedTweet.py` - Creates a tweet based on a tuned babbage engine. If this doesn't work, just replace the engine with a generic. See [Fine tuning](doc/tuning.md) for details.
4. `sentimentAnalysis.py` - Scrape tweets and analyse sentiment. Choose 1 to do both or if you already have a CSV, run 2. Note that you shouldn't grab more than 25 tweets or so as you may run out of OpenAI tokens. 
5. `gpt4sample.py` - Working example from [Chat completions introduction](https://platform.openai.com/docs/guides/chat/introduction).
6. `gpt4code.py` - Modified sample to output code from GPT-4.
7. `gpt4chat.py` - Simple GPT-4 chatbot.

## Activate venv

Activate the virtual environment with:

```bash
$ . venv/bin/activate
```

## Run app

Run an app in the venv terminal with the `python` command. For example:

`python completeSentence.py`

## Related

* [OpenAI API Quickstart - Python example app](doc/originalREADME.md)
* [Tokens and temperature](doc/tokensTemp.md)
* [Fine tuning](doc/tuning.md)
* [Resources](doc/resources.md)
* [Scraper](https://github.com/YRG999/Scraper)
