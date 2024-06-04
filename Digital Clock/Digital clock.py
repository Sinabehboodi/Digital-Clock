from tkinter import * 
import time 


window = Tk()
window.title("Digital Clock")
window.geometry()


def mytime():
    hour = time.strftime("%H")
    minute = time.strftime("%M")
    second = time.strftime("%S")
    am_pm = time.strftime("%p")
    day = time.strftime("%A")
    area = time.strftime("%Z")
    mytext = hour + ":" + minute + ":" + second + " " + am_pm
    mytext2 = day + "," + area 
    mylabel.config(text=mytext)
    mylabel2.config(text=mytext2)
    mylabel.after(1000, mytime)


mylabel = Label(window, text="", font=("Arial", 72), fg="white", bg="green")
mylabel.pack()

mylabel2 = Label(window, text="", font=("Arial", 24))
mylabel2.pack()

mytime()

window.mainloop()
