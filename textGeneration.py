import pathlib
import textwrap
import google.generativeai as genai
from IPython.display import display
from IPython.display import Markdown as md
import time

API_KEY = "AIzaSyBFQPazFXJpdQjj0iINy3BtP0RVI-3-4L8"

# def to_markdown(text):
#   text = text.replace('•', '  *')
#   return md(textwrap.indent(text, '> ', predicate=lambda _: True))

genai.configure(api_key=API_KEY)
#loop to see the available models
# for m in genai.list_models():
#   if 'generateContent' in m.supported_generation_methods:
#     print(m.name)
def generator(text):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(text + "in 50 words")
    return response.text
# display(to_markdown(response.text))

if __name__ == "__main__":
    res = generator("what is google")
    print(res)