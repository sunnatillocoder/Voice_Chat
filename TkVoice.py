from tkinter import *
import pyttsx3

oyna = Tk()
oyna.title('Voice 🛰')
oyna.geometry('300x200')
oyna.configure(background='black')

matn = Entry()
matn.place(x=60, y=30, width=180, height=30)

def voice():
        engine = pyttsx3.init()
        engine.say(matn.get())
        engine.runAndWait()

voice = Button(text="Ovozga o'girish",background='yellow', border='5', command=voice)
voice.place(x=90, y=62, width=120, height=35)


oyna.mainloop()