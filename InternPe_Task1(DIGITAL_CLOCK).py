from tkinter import *
from time import strftime

mk = Tk()
mk.title("DIGITAL CLOCK")

def time():
     string = strftime('%I:%M:%S %p')
     lbl.config(text=string)
     lbl.after(1000, time)

lbl = Label(mk,font=('calibri',65,'bold'),bg='yellow',fg='black')
lbl.pack(anchor='center')
time()

mainloop()

