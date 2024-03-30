import openai
import pathlib
import textwrap
import google.generativeai as genai
from IPython.display import display
from IPython.display import Markdown as md
import time
from credentials import geminikey,openaikey



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



def generator(text):
  openai.api_key = openaikey

  response = openai.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
      {
        "role": "user",
        "content": text + "make it more natural not hyperbolical just straight forward",
      }
    ],
    temperature=1,
    max_tokens=100,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
  )
  return response.choices[0].message.content

if __name__ == "__main__":
    res = generator("give about google oneliner")
    print(res)