# OpenAI API Quickstart - amended

## TOC

There are 3 apps:

1. [Python example app](#python-example-app) - follow these steps first to generate your virtual env with dependencies and put your OPENAI_API_KEY in an .env file and test your integration.
2. completeSentence.py - completes your sentence, run `python3 completeSentence.py` in the terminal to try it.
3. tunedTweet.py - Creates a tweet based on a tuned babbage engine. If this doesn't work, just replace the engine with a generic.

## Python example app

This is an example pet name generator app used in the OpenAI API [quickstart tutorial](https://beta.openai.com/docs/quickstart). It uses the [Flask](https://flask.palletsprojects.com/en/2.0.x/) web framework. Check out the tutorial or follow the instructions below to get set up.

## Setup

1. If you don’t have Python installed, [install it from here](https://www.python.org/downloads/)

2. Clone this repository

3. Navigate into the project directory

   ```bash
   $ cd openai-quickstart-python
   ```

4. Create a new virtual environment

   ```bash
   $ python -m venv venv
   $ . venv/bin/activate
   ```

5. Install the requirements

   ```bash
   $ pip install -r requirements.txt
   ```

6. Make a copy of the example environment variables file

   ```bash
   $ cp .env.example .env
   ```

7. Add your [API key](https://beta.openai.com/account/api-keys) to the newly created `.env` file

8. Run the app

   ```bash
   $ flask run
   ```

You should now be able to access the app at [http://localhost:5000](http://localhost:5000)! For the full context behind this example app, check out the [tutorial](https://beta.openai.com/docs/quickstart).

## Tokens

Models break down text into tokens for processing.

---

> Tokens can be words, chunks of words, or single characters.
Given some text, the model determines which token is most likely to come next. For example, the text "Horses are my favorite" is most likely to be followed with the token "animal".

*From **DEEP DIVE: Understanding tokens and probabilities** in the Quickstart [Adjust your settings](https://beta.openai.com/docs/quickstart/adjust-your-settings) section.*

---

Tokens are shared between the prompt and completion, with a limit of 4097 between them.

---

> 75 words ~= 100 tokens</br>
> 1 paragraph ~= 100 tokens</br>
> 1,500 words ~= 2048 tokens</br>
> Wayne Gretzky's "You miss 100% of the shots you don't take" = 11 tokens</br>
> OpenAI’s charter = 476 tokens</br>

> Depending on the model used, requests can use up to 4097 tokens shared between prompt and completion. If your prompt is 4000 tokens, your completion can be 97 tokens at most. 

*From [What are tokens and how to count them](https://help.openai.com/en/articles/4936856-what-are-tokens-and-how-to-count-them).*

---

## Temperature

Temperature determines probability. Low returns the most likely, high is less likely, or more creative. 

Use a decimal value between 0-1. For example, 0.6 is moderate.