import openai
import sys
from time import sleep
import apis
openai.api_key=apis.OPENAI_KEY
prompt = "Explain neural network like Shakespeare."
response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
        {"role": "assistant", "content": prompt},
    ]
)
api_response = response['choices'][0]['message']['content']
# assigning color to my text
green = '\033[32m'
red = '\033[31m'

# real chatGPT print effect
def delayed_print(text):
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        sleep(0.02)
    print('')
    return ">>"
delayed_print(red + "Question: " + prompt)
delayed_print(green + "ChatGPT response: " + api_response)