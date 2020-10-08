import speech_recognition
def listen():
    robot_ear = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as mic:
        print("Robot: I'm listening")
        audio = robot_ear.record(mic,duration = 5)
    print("^_^: ...")
    try:
        you = robot_ear.recognize_google(audio)
    except:
        you = "please say again"
    return you
# print(listen())