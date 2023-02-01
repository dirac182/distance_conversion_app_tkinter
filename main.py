from tkinter import *


def convert():
    miles = int(miles_entry.get())
    kilometers = int(km_entry.get())
    mi_to_km = float(miles * 1.609)
    km_to_mi = float(kilometers / 1.609)
    if miles != 0:
        km_label.config(text=round(mi_to_km,3))
    if kilometers != 0:
        miles_label.config(text=round(km_to_mi,3))


window = Tk()
window.title("Miles to Kilometers Converter")
window.minsize(width=500, height=250)
window.config(padx=25, pady=25)

title_label = Label(text="", font=("Arial", 15, "bold"))
title_label.grid(column=0, row=0)
title_label.config(padx=25, pady=25)

miles_display = Label(text="Miles", font=("Arial", 12, "normal"))
miles_display.grid(column=1, row=1)
miles_display.config(padx=5, pady=5)

miles_entry = Entry(width=20)
miles_entry.insert(0, "0")
miles_entry.grid(column=1, row=4)

km_display = Label(text="Kilometers", font=("Arial", 12, "normal"))
km_display.grid(column=5, row=1)
km_display.config(padx=5, pady=5)

km_entry = Entry(width=20,)
km_entry.grid(column=5, row=4)
km_entry.insert(0, "0")

conv_button = Button(text="Convert!", command=convert)
conv_button.grid(column=3, row=2)

miles_label = Label(font=("Arial", 12, "normal"))
miles_label.grid(column=1,row=2)

km_label = Label(font=("Arial", 12, "normal"))
km_label.grid(column=5,row=2)


window.mainloop()
