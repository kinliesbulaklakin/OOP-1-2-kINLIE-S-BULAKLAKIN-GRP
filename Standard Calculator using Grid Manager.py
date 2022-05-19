
from tkinter import *
window = Tk()
window.geometry("312x324")
window.title("Standard Calculator using Grid Manager")

data = ""
data_input = StringVar()

def input_btn(item):
    global data
    data = data + str(item)
    data_input.set(data)
def clear_btn():
    global data
    data = ""
    data_input.set("")
def equal_btn():
    global data
    result = str(eval(data))
    data_input.set(result)
    data = ""


#frame
calculator_frame = Frame(width=312, height=50, bd=0)
calculator_frame.pack(side=TOP)
input_field = Entry(calculator_frame, font=('arial', 18, 'bold'), textvariable=data_input, width=50)
input_field.grid(row=0, column=0)
input_field.pack(ipady=10)
frame_btn = Frame(width=312, height=272.5, bg="grey")
frame_btn.pack()


#rows
clear = Button(frame_btn, text="Clear", width=32, height=3, bd=0,
               command=lambda: clear_btn())
clear.grid(row=0, column=0, columnspan=3, padx=1, pady=1)
division = Button(frame_btn, text="/",  width=10, height=3, bd=0,
                command=lambda: input_btn("/"))
division.grid(row=0, column=3, padx=1, pady=1)
seven = Button(frame_btn, text="7", width=10, height=3, bd=0,
               command=lambda: input_btn(7))
seven.grid(row=1, column=0, padx=1, pady=1)
eight = Button(frame_btn, text="8", width=10, height=3, bd=0,
               command=lambda: input_btn(8))
eight.grid(row=1, column=1, padx=1, pady=1)
nine = Button(frame_btn, text="9", width=10, height=3, bd=0,
              command=lambda: input_btn(9))
nine.grid(row=1, column=2, padx=1, pady=1)
multiplication = Button(frame_btn, text="*", width=10, height=3, bd=0,
                  command=lambda: input_btn("*"))
multiplication.grid(row=1, column=3, padx=1, pady=1)
four = Button(frame_btn, text="4",  width=10, height=3, bd=0,
              command=lambda: input_btn(4))
four.grid(row=2, column=0, padx=1, pady=1)
five = Button(frame_btn, text="5",width=10, height=3, bd=0,
              command=lambda: input_btn(5))
five.grid(row=2, column=1, padx=1, pady=1)
six = Button(frame_btn, text="6", width=10, height=3, bd=0,
             command=lambda: input_btn(6))
six.grid(row=2, column=2, padx=1, pady=1)
subtraction= Button(frame_btn, text="-", width=10, height=3, bd=0,
               command=lambda: input_btn("-"))
subtraction.grid(row=2, column=3, padx=1, pady=1)
one = Button(frame_btn, text="1", width=10, height=3, bd=0,
             command=lambda: input_btn(1))
one.grid(row=3, column=0, padx=1, pady=1)
two = Button(frame_btn, text="2", width=10, height=3, bd=0,
             command=lambda: input_btn(2))
two.grid(row=3, column=1, padx=1, pady=1)
three = Button(frame_btn, text="3", width=10, height=3, bd=0,
               command=lambda: input_btn(3))
three.grid(row=3, column=2, padx=1, pady=1)
addition = Button(frame_btn, text="+",  width=10, height=3, bd=0,
              command=lambda: input_btn("+"))
addition.grid(row=3, column=3, padx=1, pady=1)
zero = Button(frame_btn, text="0",  width=21, height=3, bd=0,
              command=lambda: input_btn(0))
zero.grid(row=4, column=0, columnspan=2, padx=1, pady=1)
decimal = Button(frame_btn, text=".",  width=10, height=3, bd=0,
               command=lambda: input_btn("."))
decimal.grid(row=4, column=2, padx=1, pady=1)
equalization = Button(frame_btn, text="=",width=10, height=3, bd=0,
                command=lambda: equal_btn())
equalization.grid(row=4, column=3, padx=1, pady=1)

window.mainloop()

