from tkinter import *
from PIL import Image,ImageTk
from  googletrans import Translator
import pyttsx3
import tkinter
display = tkinter.Tk()
display.title("Rin is Linh")
display.geometry("500x500")
# display.iconbitmap("/home/rin/Pictures/image_logo/part11.png")

imgebackground = Image.open("/home/rin/Documents/Code/Rintr/background.jpg")
show = ImageTk.PhotoImage(imgebackground)
showbackground = Label(display,image = show)
showbackground.place(x=0,y=0)

selected = IntVar()
selected2 = IntVar()
rad1 = Radiobutton(display,text='Vietnam', value=1, variable=selected)
rad2 = Radiobutton(display,text='English', value=2, variable=selected)
rad3 = Radiobutton(display,text='Japan', value=3, variable=selected)
rad1.place(x = 100,y=0)
rad2.place(x = 200,y=0)
rad3.place(x = 300,y=0)


rad4 = Radiobutton(display,text='Vietnam', value=4, variable=selected2)
rad5 = Radiobutton(display,text='English', value=5, variable=selected2)
rad6 = Radiobutton(display,text='Japan  ', value=6, variable=selected2)
rad4.place(x = 100,y=230)
rad5.place(x = 200,y=230)
rad6.place(x = 300,y=230)


box = Text(display,width = 40,heigh = 8)
box.pack(pady = 40)
boxtran = Text(display,width = 40,heigh = 8)
boxtran.pack(pady = 40)

def clear():
    box.delete(1.0,END)
    boxtran.delete(1.0,END)
def trans():
    strk = box.get(1.0,END)
    transs = Translator()
    print(clickedtran(),clicked())
    temp = transs.translate(strk,dest=clicked(),src=clickedtran())
    b = temp.text
    boxtran.insert(END,b)
def clicked():
    check = selected2.get()
    if (check == 4):
       return "vi"
    elif (check == 5):
       return "en"
    elif (check == 6):
       return "ja"


def clickedtran():
    check = selected.get()
    if (check == 1):
       return "vi"
    elif (check == 2):
       return "en"
    elif (check == 3):
       return "ja"
def speak1():
    you = box.get(1.0,END)
    bran = pyttsx3.init()
    bran.say(you)
    bran.runAndWait()
def speak2():
    you = boxtran.get(1.0,END)
    bran = pyttsx3.init()
    if (you == ""):
        you = "I do not understand"
    bran.say(you)
    bran.runAndWait()

button_tran = tkinter.Button(display,text = "tran",font = (("Arial"),15,'bold'),command = trans)
button_clear = tkinter.Button(display,text = "clear",font = (("Arial"),15,'bold'),command = clear)
button_tran.place(x=0,y=450)
button_clear.place(x = 420,y=450)
but_speak1 = tkinter.Button(display,text = 'speak',command = speak1)
but_speak1.place(x = 400,y = 0)
but_speak2 = tkinter.Button(display,text = 'speak',command = speak2)
but_speak2.place(x = 400,y = 230)
but_listen = tkinter.Button(display,text = 'listen',command = speak2)
but_listen.place(x = 220,y = 450)
display.mainloop()