from flask import Flask
import replicate
import os

app = Flask(__name__)

os.environ['REPLICATE_API_TOKEN'] = 'r8_I6byr460oRsgfcmkJELYfHtl9VACL8d1QsffB'
output = replicate.run(
  "meta/llama-2-70b-chat:02e509c789964a7ea8736978a43525956ef40397be9033abf9fd2badfe68c9e3",
  input={
    "debug": False,
    "top_k": 50,
    "top_p": 1,
    "prompt": word,
    "temperature": 0.5,
    "system_prompt": "You are a helpful, respectful and honest assistant. Always answer as helpfully as possible, while being safe. Your answers should not include any harmful, unethical, racist, sexist, toxic, dangerous, or illegal content. Please ensure that your responses are socially unbiased and positive in nature.\n\nIf a question does not make any sense, or is not factually coherent, explain why instead of answering something not correct. If you don't know the answer to a question, please don't share false information.",
    "max_new_tokens": 500,
    "min_new_tokens": -1
    }
  )
texter=""
for item in output:
       texter+=item
@app.route("/api/<word>")
def apix(word):
  
  return texter

