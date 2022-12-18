# Resources

Some resources I found helpful.

## Open AI

* https://github.com/openai/openai-cookbook/tree/main/examples
* https://beta.openai.com/docs/quickstart/adjust-your-settings
* https://openai.com/api/pricing/
* https://help.openai.com/en/articles/4936856-what-are-tokens-and-how-to-count-them

## Python write to file

* https://www.w3schools.com/python/python_file_write.asp
* https://www.w3schools.com/python/python_datetime.asp
* https://www.freecodecamp.org/news/python-print-variable-how-to-print-a-string-and-variable/
* https://stackoverflow.com/questions/16822016/write-multiple-variables-to-a-file
* https://docs.python.org/3/tutorial/inputoutput.html
* https://www.pythontutorial.net/python-basics/python-write-text-file/

## Python other

* Comments
  * https://www.codecademy.com/forum_questions/505ba3cfc6addb000200e33c
  * https://peps.python.org/pep-0008/#block-commentspip
* https://stackoverflow.com/questions/423379/using-global-variables-in-a-function

## VSCode

* https://stackoverflow.com/questions/38561881/how-do-i-turn-on-text-wrapping-by-default-in-vs-code
* https://code.visualstudio.com/updates/v1_10#_editor

## Open AI upgrade 3.5
* https://beta.openai.com/docs/model-index-for-researchers
```
Models referred to as "GPT 3.5"
GPT-3.5 series is a series of models that was trained on a blend of text and code from before Q4 2021. The following models are in the GPT-3.5 series:

code-davinci-002 is a base model, so good for pure code-completion tasks
text-davinci-002 is an InstructGPT model based on code-davinci-002
text-davinci-003 is an improvement on text-davinci-002
```
* https://github.com/openai/openai-python
```
Command-line interface

This library additionally provides an openai command-line utility which makes it easy to interact with the API from your terminal. Run openai api -h for usage.

# list engines
openai api engines.list

# create a completion
openai api completions.create -e ada -p "Hello world"

# generate images via DALL·E API
openai api image.create -p "two dogs playing chess, cartoon" -n 1
```
Run: `openai api engines.list` to list engines.

## Sentiment analysis
* https://beta.openai.com/examples/default-adv-tweet-classifier
* https://beta.openai.com/playground/p/default-adv-tweet-classifier?model=text-davinci-003
* https://www.youtube.com/watch?v=uPKnSq6TaAk
* https://github.com/mehranshakarami/AI_Spectrum/tree/main/2022/Sentiment_Analysis