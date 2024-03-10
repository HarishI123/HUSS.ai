import pyttsx3
from textGeneration import generator

def text_to_speech(text):
    engine = pyttsx3.init()
    rate = engine.getProperty("rate") #default speed is 200 
    engine.setProperty("rate",150) # speed changed to 135
    engine.say(text)
    engine.runAndWait()


if __name__ == "__main__":
    text_to_speech(generator("what is google"))
