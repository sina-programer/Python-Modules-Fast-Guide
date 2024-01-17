import pyttsx3

TEXT = "Your Text"

engine = pyttsx3.init()
engine.say(TEXT)
engine.runAndWait()
