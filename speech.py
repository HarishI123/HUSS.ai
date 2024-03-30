import pyttsx3
from textGeneration import generator

def text_to_speech(text):
    engine = pyttsx3.init()
    rate = engine.getProperty("rate") #default speed is 200 
    engine.setProperty("rate",175) # speed changed to 135
    engine.say(text)
    print(text)
    engine.runAndWait()

if __name__ == "__main__":
    while True:
        prompt = input("enter you prompt: ")
        if "bye" in prompt:
            text_to_speech("bye, if you have any questions feel free to ask me")
            break
        text_to_speech(generator(prompt))

