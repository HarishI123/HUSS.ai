import speech_recognition as sr

def speech_to_text():
    # Initialize recognizer
    recognizer = sr.Recognizer()
    
    # Use microphone as source for input
    with sr.Microphone() as source:
        # print("Adjusting for ambient noise, please wait...")
        recognizer.adjust_for_ambient_noise(source, duration=2)  # Adjust based on background noise
        
        print("Listening...")
        audio = recognizer.listen(source)  # Capture the audio
        
        try:
            # Convert audio to text using Google Web Speech API
            text = recognizer.recognize_google(audio)
            print("You said:", text)
            return text
        
        except sr.UnknownValueError:
            print("Sorry, I couldn't understand that. Please try speaking more clearly.")
            return None
        
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
            return None

# Run the function to test speech-to-text
if __name__ == "__main__":
    result = speech_to_text()
    if result:
        print("Transcription successful:", result)
    else:
        print("Transcription failed.")



if __name__ == "__main__":
    speech_to_text()
