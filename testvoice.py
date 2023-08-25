import pyttsx3

def voice():
        engine = pyttsx3.init()
        engine.say("I will speak this text")
        engine.runAndWait()

voice()
        