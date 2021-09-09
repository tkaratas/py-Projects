"""Count Down timer with tkinter. 
I know it's not the best practice :'(
"""

from tkinter import *
import winsound
import time

duration = 100
freq = 440


window = Tk()
window.geometry('200x200')


def newWindow():
    textInput = int(text.get())
    newWin = Tk()
    newWin.geometry('200x300')

    def countDown():
        count = int(label.cget('text'))
        winsound.Beep(freq, duration)
        if count > 0:
            count -= 1
            label.config(text=count)
            window.after(1000, countDown)
        else:
            label.config(text=count, fg='red')
            winsound.Beep(380, 1000)

    button = Button(newWin, text='Start', fg='white', bg='gray',
                    font=('Arial'), command=countDown)
    button.pack()
    label = Label(newWin, text=textInput, font=('Arial', 15))
    label.pack()


text = Entry(window)
text.grid(row=0, column=2)
button = Button(window, text='Set', fg='white', bg='gray',
                font=('Arial'), command=newWindow)
button.grid(row=1, column=2)

mainloop()
