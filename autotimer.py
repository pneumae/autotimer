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
        minute = m
        try:
            second = s
        except ValueError:
            pass
    else:
        return

def confirmEntry():
    global minute
    global second
    global winx
    global winy
    global root

    minute = minentry.get()
    second = secentry.get()
    winx = root.winfo_rootx()
    winy = root.winfo_rooty()
    w = root.winfo_width()
    h = root.winfo_height()
    root.destroy()
    print(str(minute)+"."+str(second))
    secondAdjuster()
    print(str(minute)+"."+str(second))
    print(winx,winy)
    print(w,h)

root = Tk()
root.title("Timer")
#w = root.winfo_width()
#h = root.winfo_height()
w = 68
h = 48
ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)
root.geometry('%dx%d+%d+%d' % (w, h, x, y))
#winfo_rootx()

minentry = Entry(root)
minentry.grid(row=0, column=0)
minentry.config(width=3)
colon = Label(root, text=":")
colon.grid(row=0, column=1)
secentry = Entry(root)
secentry.grid(row=0, column=2)
secentry.config(width=3)
confirm = Button(root, text="Ok", command=confirmEntry)
confirm.grid(row=1, columnspan=3)
root.mainloop()

increment = 0
root = Tk()
if second == "":second = 0
if minute == "":minute = 0
us = second
um = minute
def refreshTimer():
    global us
    global um
    global second
    global minute
    global increment
    second = us
    minute = um
    countdown()
    increment = increment+1

def countdown():
    global ml
    global sl
    global second
    global minute
    global root
    ml.configure(text=minute)
    sl.configure(text=f'{second:02}')
    if second == 0:
        if minute > 0:
            minute = minute - 1
            second = 59
            root.after(1000, countdown)
        elif minute == 0:
#TIMER END
            root.lift()
            root.attributes('-topmost', 1)
            root.attributes('-topmost', 0)
            root.focus_force()
            root.after(1000, refreshTimer)
            return
    elif second > 0:
        second = second - 1
        root.after(1000, countdown)
    else:
        return
root.geometry('%dx%d+%d+%d' % (w, h, winx, winy))
ml = Label(root)
ml.grid(row=0,column=0,sticky=W+E)
cl = Label(root, text=":")
cl.grid(row=0,column=1)
sl = Label(root)
sl.grid(row=0,column=2)
countdown()
root.mainloop()

t = Timer(60,hi)

