import io , time
from datetime import date
from datetime import datetime
import wikipedia
import Listen
import Speak
import regex
import webbrowser

today = date.today()
def start(you):
    if you in "hello hi":
       Speak.speak("hello Linh")
#========================================================
def think(you):      
        if you in "what is the date today":
            you = today.strftime("%B %d ,%Y")
        elif you in "what time is it":
            now = datetime.now()
            print("time:", you)
            you = now.strftime("%H:%M:%S")
        elif  "wikipedia" in you :
            print("Key word: ")
            key = input()
            you = wikipedia.summary(key)
        elif you in "video":
            you = "Youtobe is open ... "
            youtube()
        elif 'game' in you:
            onetwothree()
        else:
            print("You: ",you)
            you = "please say again"
        return you
#========================================================
def dictionary():
    print("Lua chon 1 trong cac muc sau:")
    dc = ["1: Them tu",
        "2: Xoa tu",
        "3: Tra tu"
        ]
    print(*dc,"\n")
    number = int(input("Selection your: "))


    if number == 1:
        dic = load_dict()
        x = input("Add words: ")
        y = input("Mean: ")
        dic.update({x:y})
        save_dict(dic)
        print(u"Bạn đã thêm từ %s thành công"%x)
        Speak.speak("successfully added")
# phần del phần tử trong dic

    if number == 2:
        dic = load_dict()
        words = input("The word to delete: ")
        print("Are you sure ?","\n","1.yes","\n","2.no")
        sure = int(input("Selection: "))
        if sure == 1:
            del dic[words]
            save_dict(dic)
            print("Ban da xoa thanh cong tu",words)
        else :
            Speak.speak("You are wise")

#phần find phần tử trong dic

    if number == 3:
        find = input("The word to find: ")
        print("I found this word: ",load_dict()[find])
#================================================================
# tệp
def save_dict(dic):
    f = io.open('D:\Code\Python\Creat\data\dict.txt',mode = 'w',encoding='utf-8')
    f.write(str(dic))
    f.close()
#===============================================================
def load_dict():
    f = io.open('D:\Code\Python\Creat\data\dict.txt',mode = 'r',encoding='utf-8')
    data=f.read()
    f.close()
    return eval(data)
#================================================================
def vn(you):
    pass
# dictionary()
def youtube():
    url = "http://youtube.com"
    robot_brain = webbrowser.open_new_tab(url)
import os # hàm tắt máy
def shut_down():
    time_shut_down = input(u"Nhập thời gian tắt máy: ")
    time_shut_down = time_shut_down.split(" ",2)
    i=1
    while i <= int(time_shut_down[0]):
        if 'm' in time_shut_down:
            time.sleep(60)
            unit_of_time = 'minute'
        else:
            time.sleep(1)
            unit_of_time = 'second'
        value = str(i) + " " + unit_of_time 
        print(u"%s has ended"%value)
        i+=1
    print('Please wait a few minutes!')
    Speak.speak('Please wait a few minutes')
    os.system('shutdown -s')
#==========================================================
def onetwothree():
    os.system('D:\Code\Python\Minitest\gkbb.py')