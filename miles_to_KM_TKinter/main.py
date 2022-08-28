from tkinter import *


def button_change():

    miles_input = float(input_mile.get())
    km_output = miles_input * 1.609
    km["text"] = km_output


window = Tk()

window.title("Miles to KM")
window.minsize(200, 100)
window.config(padx=20, pady=20)

input_mile = Entry(width=10)
input_mile.grid(row=0, column=1)

label_1 = Label(text="Miles")
label_1.grid(row=0, column=2)

label_2 = Label(text="is equal to")
label_2.grid(row=1, column=0)

km = Label(text="0")
km.grid(row=1, column=1)

label_3 = Label(text="KM")
label_3.grid(row=1, column=2)

my_button = Button(text="Calculate", command=button_change)
my_button.grid(row=2, column=1)











window.mainloop()