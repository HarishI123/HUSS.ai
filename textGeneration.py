import openai
import pathlib
import textwrap
import google.generativeai as genai
from IPython.display import display
from IPython.display import Markdown as md
import time
from credentials import geminikey,openaikey



openaikey = "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"
def to_markdown(text):
  text = text.replace('•', '  *')
  return md(textwrap.indent(text, '> ', predicate=lambda _: True))

genai.configure(api_key=geminikey)
# loop to see the available models
# for m in genai.list_models():
#   if 'generateContent' in m.supported_generation_methods:
#     print(m.name)


# def generator(text):
#     model = genai.GenerativeModel('gemini-1.0-pro-latest')
#     response = model.generate_content(text + "single liner")
#     return response.text


messages = [{
      "role":"user",
      "content":"act as an personal assitant bot and your name is pookie"}]
def generator(text):
  openai.api_key = "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"

  messages.append({"role":"user","content":text})
  response = openai.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=messages,
    temperature=1,
    max_tokens=100,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
  )
  messages.append(response.choices[0].message)
  return response.choices[0].message.content

if __name__ == "__main__":
    res = generator("give about google oneliner")
    print(res)