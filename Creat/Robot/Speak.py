import pyttsx3
def speak(you):
    engine = pyttsx3.init()
    engine.say(you)
    engine.runAndWait()
# you = "Hello Linh"
# speak(you)