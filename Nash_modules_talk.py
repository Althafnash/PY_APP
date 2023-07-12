def talk(text):
    speak = pyttsx3.init()
    speak.say(text)
    speak.runAndWait()

