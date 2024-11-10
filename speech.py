import pyttsx3
from textGeneration import generator
from speechToText import speech_to_text
import time
from collections import deque

def text_to_speech(text):
    engine = pyttsx3.init()
    rate = engine.getProperty("rate") #default speed is 200 
    engine.setProperty("rate",175) # speed changed to 135
    engine.say(text)
    print(text)
    engine.runAndWait()

if __name__ == "__main__":
    while True:
        with open('detections_log.txt', 'r') as file:
                # data = file.readlines()  # Load text data from file into a Python dictionary
                data = deque(file, maxlen=5)
        prompt = speech_to_text()
        print(prompt)
        if "bye" in prompt:
            text_to_speech("bye, if you have any questions feel free to ask me")
            break
        text_to_speech(generator(prompt,data))
        time.sleep(5)

