"""Claculator with tkinter"""

from tkinter import *
expression = ""


def press(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)


def equalPress():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = ""

    except:
        equation.set("")
        expression = ""


def Clear():
    global expression
    expression = ""
    equation.set(expression)


root = Tk()
root.title('Calculator')
root.geometry("470x230")
root.configure(bg='light blue')
equation = StringVar()
result = Entry(root, textvariable=equation)
result.grid(columnspan=3, ipadx=110, ipady=10)

button1 = Button(root, text="1", command=lambda: press(1), height=2, width=15)
button1.grid(row=2, column=0)

button2 = Button(root, text="2", command=lambda: press(2), height=2, width=15)
button2.grid(row=2, column=1)

button3 = Button(root, text="3", command=lambda: press(3), height=2, width=15)
button3.grid(row=2, column=2)

button4 = Button(root, text="4", command=lambda: press(4), height=2, width=15)
button4.grid(row=3, column=0)

button5 = Button(root, text="5", command=lambda: press(5), height=2, width=15)
button5.grid(row=3, column=1)

button6 = Button(root, text="6", command=lambda: press(6), height=2, width=15)
button6.grid(row=3, column=2)

button7 = Button(root, text="7", command=lambda: press(7), height=2, width=15)
button7.grid(row=4, column=0)

button8 = Button(root, text="8", command=lambda: press(8), height=2, width=15)
button8.grid(row=4, column=1)

button9 = Button(root, text="9", command=lambda: press(9), height=2, width=15)
button9.grid(row=4, column=2)

button0 = Button(root, text="0", command=lambda: press(0), height=2, width=15)
button0.grid(row=5, column=0)

plus = Button(root, text="+", command=lambda: press('+'), height=2, width=15)
plus.grid(row=2, column=3)

minus = Button(root, text="-", command=lambda: press('-'), height=2, width=15)
minus.grid(row=3, column=3)

multiply = Button(root, text=' * ',
                  command=lambda: press('*'), height=2, width=15)
multiply.grid(row=4, column=3)

divide = Button(root, text=' / ', command=lambda: press('/'),
                height=2, width=15)
divide.grid(row=5, column=3)

equal = Button(root, text=' = ', command=equalPress, height=2, width=15)
equal.grid(row=5, column=2)

clear = Button(root, text='Clear', command=Clear, height=2, width=15)
clear.grid(row=0, column=3)

decimal = Button(root, text=".", command=lambda: press("."),
                 height=2, width=15)
decimal.grid(row=5, column=1)
root.mainloop()
