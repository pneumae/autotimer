from tkinter import *
from threading import Timer
import time

class CountdownTimer():
    #def __init__(self):
        #self.starttime = time.time()
    def startTimer(self, seconds):
        self.starttime = time.time()
        self.endtime = self.starttime + seconds
    def getTime():
        return int(self.endtime - time.time())

class AutoTimerUI():
    def __init__(self):
        self.minute = 0
        self.second = 0

    def secondAdjuster(self):
        if(self.second != ""):
            m, s = divmod(int(self.second), 60)
            try:
                m = int(self.minute) + m
            except ValueError:
                pass
            self.minute = m
            try:
                self.second = s
            except ValueError:
                pass           
            return
        else:
            return

    def confirmEntry(self): 
        self.minute = self.minentry.get()
        self.second = self.secentry.get()
        self.winx = root.winfo_rootx()
        self.winy = root.winfo_rooty()
        self.w = root.winfo_width()
        self.h = root.winfo_height()
        print(str(self.minute)+"."+str(self.second))
        self.secondAdjuster()
        root.destroy()
        #debug stuff
        print(str(self.minute)+"."+str(self.second))
        # print(winx,winy)
        # print(w,h)

    def timeEntryWindow(self): 
       # root = Tk()
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
        self.minentry = Entry(root)
        self.minentry.grid(row=0, column=0)
        self.minentry.config(width=3)
        colon = Label(root, text=":")
        colon.grid(row=0, column=1)
        self.secentry = Entry(root)
        self.secentry.grid(row=0, column=2)
        self.secentry.config(width=3)
        confirm = Button(root, text="Ok", command=self.confirmEntry)
        confirm.grid(row=1, columnspan=3)
       # root.mainloop()

    increment = 0
    # root = Tk()
    # if second == "":second = 0
    # if minute == "":minute = 0

    def refreshTimer(self):
        self.second = self.us
        self.minute = self.um
        self.countdown()
        # increment += 1

    def countdown(self):

        self.ml.configure(text=self.minute)
        self.sl.configure(text=f'{self.second:02}')
        if self.second == 0:
            if self.minute > 0:
                self.minute -= 1
                self.second = 59
                root.after(1000, self.countdown)
            elif self.minute == 0:
    #TIMER END
                root.lift()
                root.attributes('-topmost', 1)
                root.attributes('-topmost', 0)
                #root.focus_force()
                root.after(1000, self.refreshTimer)
                return
        elif self.second > 0:
            self.second -= 1
            root.after(1000, self.countdown)
        else:
            return
    def timeDisplayWindow(self):
        root.geometry('%dx%d+%d+%d' % (self.w, self.h, self.winx, self.winy))
        self.ml = Label(root)
        self.ml.grid(row=0,column=0,sticky=W+E)
        cl = Label(root, text=":")
        cl.grid(row=0,column=1)
        self.sl = Label(root)
        self.sl.grid(row=0,column=2)
        self.us = self.second
        self.um = self.minute
        self.countdown()
        # root.mainloop()
        # print(increment)
        #t = Timer(60,hi)

windowOne = AutoTimerUI()
root = Tk()
windowOne.timeEntryWindow()
root.mainloop()
root = Tk()
windowOne.timeDisplayWindow()
root.mainloop()