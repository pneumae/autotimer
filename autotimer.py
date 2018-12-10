from tkinter import *
from threading import Timer

def secondAdjuster():
    global minute
    global second
    if(second != ""):
        m, s = divmod(int(second), 60)
        try:
            m = int(minute) + m
        except ValueError:
            pass
        minute = str(m)
        try:
            second = str(s)
        except ValueError:
            pass
    else:
        return

def confirmEntry():
    global minute
    global second
    minute = minentry.get()
    second = secentry.get()
    minentry.destroy()
    secentry.destroy()
    colon.destroy()
    confirm.destroy()
    print(minute+"."+second)
    secondAdjuster()
    print(minute+"."+second)

root = Tk()
root.title("Timer")
#root.geometry("200x200+50+50")
minentry = Entry(root)
minentry.pack(side=LEFT)
minentry.config(width=3)
colon = Label(root, text=":")
colon.pack(side=LEFT)
secentry = Entry(root)
secentry.pack(side=LEFT)
secentry.config(width=3)
confirm = Button(root, text="Ok", command=confirmEntry)
confirm.pack(side=TOP)
root.mainloop()
t = Timer(60,hi)

