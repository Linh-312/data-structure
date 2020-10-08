import Listen, Speak,Think
def tree_speak():
    while True:
        you = Listen.listen()
        # print("Robot: ",you)
        if "hello" in you: 
            Think.start(you)
        elif "bye" in you:
            Speak.speak("Goodbye,See you again")
            break 
        elif "dictionary" in you:
            Think.dictionary()
        else:
            you = Think.think(you)
            print(you)
            Speak.speak(you)
def tree_write():
    while True:
        you = input("Input: ")
        # print("Robot: ",you)
        if "hello" in you: 
            Think.start(you)
        if "shut down"in you:
            Think.shut_down()
        elif "bye" in you:
            Speak.speak("Goodbye,see you again")
            break 
        elif "dictionary" in you:
            Think.dictionary()
        else:
            you = Think.think(you)
            print(you)
            Speak.speak(you)