from tkinter import *

window = Tk()
window.geometry("312x324")
window.title("Binary Conversion")

window.configure(bg="#fef8e8")
data_input = StringVar()

def dec_bin(*args):
    try:
        data = int(input_field.get())
        binary_num= bin(data).replace('0b', '')
        data_input.set(binary_num)
    except ValueError:
        data_input.set("ERROR!")
        pass

def bin_dec(*args):
    try:
        data = str(input_field.get())
        dec_num = int(data, 2)
        data_input.set(dec_num)
    except ValueError:
        data_input.set("ERROR!")
        pass

def clear1_btn():
    input_field.delete(0, END)
    output_field.delete(0, END)

def delete():
    data_input.set("")

def string_bin():
    try:
        data = str(input_field.get())
        string_bin = " ".join(format(i, '08b') for i in bytearray(data, encoding ='utf-8'))
        data_input.set(string_bin)
    except ValueError:
        data_input.set("ERROR!")
        pass

def bin_string():
    try:
        data = int(input_field.get(),2)
        data_number = (data.bit_length() + 7) // 8
        data_array = data.to_bytes(data_number, "big")
        bin_string = data_array.decode()
        data_input.set(bin_string)
    except ValueError:
        data_input.set("ERROR!")
        pass


conv_frame = Frame(width=312, height=50, bd=0,bg = "#fef8e8")
conv_frame.pack(side=TOP)
lbl = Label(conv_frame, text = "Enter:", font = ("Verdana", 12), bg = "#fef8e8")
lbl.grid(row=0, column=0, pady=0, sticky=W)
lbl2 = Label(conv_frame, text = "Converted to:", font = ("Verdana", 12), bg = "#fef8e8")
lbl2.grid(row=2, column=0, pady=0, sticky=W)
lbl3 = Label(conv_frame, text = "Choose operation:", font = ("Verdana", 12),bg = "#fef8e8")
lbl3.grid(row=4, column=0, pady=0, sticky=W)
input_field = Entry(conv_frame, font=('arial', 18, 'bold'), width=50)
input_field.grid(row=1, column=0, pady=10)
output_field = Entry(conv_frame, font=('arial', 18, 'bold'), width=50, textvariable=data_input)
output_field.grid(row=3, column=0, pady=10)
frame_btn = Frame(width=312, height=272.5, bg = "#fef8e8")
frame_btn.pack()


decbin_btn = Button(frame_btn, text="DEC-BIN", width=15, height=3, bd=0, bg="#FFD700", command=lambda: dec_bin())
decbin_btn.grid(row=5, column=0, padx=1, pady=1)
bindec_btn = Button(frame_btn, text="BIN-DEC", width=15, height=3, bd=0,bg="#FFD700", command=lambda: bin_dec())
bindec_btn.grid(row=5, column=1, padx=1, pady=1)
clear_btn = Button(frame_btn, text="Clear", width=10, height=3, bd=0, bg="#ff9a9a", command=lambda: clear1_btn())
clear_btn.grid(row=5, column=2, padx=1, pady=1)
delete_btn = Button(frame_btn, text="Del", width=10, height=3, bd=0, bg="#ff4e4e", command=lambda: delete())
delete_btn.grid(row=6, column=2, padx=1, pady=1)
stringbin_btn = Button(frame_btn, text="TEXT-BIN", width=15, height=3, bd=0, bg="#c4d3ff", command=lambda: string_bin())
stringbin_btn.grid(row=6, column=0, padx=1, pady=1)
binstring_btn = Button(frame_btn, text="BIN-TEXT", width=15, height=3, bd=0, bg="#c4d3ff", command=lambda: bin_string())
binstring_btn.grid(row=6, column=1, padx=1, pady=1)

window.mainloop()
