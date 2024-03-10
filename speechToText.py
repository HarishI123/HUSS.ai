import speech_recognition as sr

def speech_to_text():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening..")
        r.pause_threshold = 1
        audio = r.listen(source)
    query = r.recognize_google(audio)
    print(query)


if __name__ == "__main__":
    speech_to_text()
