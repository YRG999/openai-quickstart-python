# Tokens and temperature

A brief description of tokens and temperature.

## Tokens

Models break down text into tokens for processing.

---

> Tokens can be words, chunks of words, or single characters.
Given some text, the model determines which token is most likely to come next. For example, the text "Horses are my favorite" is most likely to be followed with the token "animal".

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
*--From **DEEP DIVE: Understanding tokens and probabilities** 
in the Quickstart 
[Adjust your settings](https://beta.openai.com/docs/quickstart/adjust-your-settings) section.*

---

Tokens are shared between the prompt and completion, with a limit of 4097 between them.

---

> 75 words ~= 100 tokens</br>
> 1 paragraph ~= 100 tokens</br>
> 1,500 words ~= 2048 tokens</br>
> Wayne Gretzky's "You miss 100% of the shots you don't take" = 11 tokens</br>
> OpenAI’s charter = 476 tokens</br>

> Depending on the model used, requests can use up to 4097 tokens shared between prompt and completion. If your prompt is 4000 tokens, your completion can be 97 tokens at most. 

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
*--From 
[What are tokens and how to count them](https://help.openai.com/en/articles/4936856-what-are-tokens-and-how-to-count-them).*

---

## Temperature

Temperature determines probability. Low returns the most likely, high is less likely, or more creative. 

Use a decimal value between 0-1. For example, 0.6 is moderate.