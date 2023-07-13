import pyttsx3

def talk(text):
    speak = pyttsx3.init()
    speak.say(text)
    speak.runAndWait()

