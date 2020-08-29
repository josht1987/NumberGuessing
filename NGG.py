import tkinter as tk
from tkinter import *
import random
import os
from PIL import Image, ImageTk

win = tk.TK()
win.configure(bg="Black")
win.geometry("650x550")
win.title("Number Guessing Game")

result= StringVar()
chances= IntVar()
chances1= IntVar()
choice= IntVar()
no=random.randitnt(1,20)
result.set("Think of a number between 1 and 20")
chances.set(5)
chances1.set(chances.get())

def fun():
    chances1.set(chances.get())
    if chances.get()>0:

        if choice.get() > 20 or choice.get()<0:
            result.set("1 chance down")
            chances.set(chances.get()-1)
            chances1.set(chances.get())

            elif no==choice.get():
                result.set("Congrats You've won!")
                chances.set(chances.get()-1)
                chances1.set(chances.get())

            elif no > choice.get():
                result.set("That guess was too low, try a higher number")
                chances.set(chances.get()-1)
                chances1.set(chances.get())
               
            elif no < choice.get():
                result.set("That guess was too high, try a lower number")
                chances.set(chances.get()-1)
                chances1.set(chances.get())

                else result.set("Game over. You lose")
                
                def restart():
                no=random.randint(1,20)
                result.set("Think of a number between 1 and 20")
                chances.set(5)
                chances1.set(chances.get())

                ent1 = Entry(win, textvariable=choice, width=3, font=('Ubuntu', 50), relief=GROOVE)
                ent1.place(relx=0.5, rely=0.3, anchor=CENTER)

                ent2 = Entry(win, textvariable=result, width=50, font=('Courier', 15), relief=GROOVE)
                ent2.place(relx=0.5, rely=0.7, anchor=CENTER)

                ent3 = Entry(win, text=chances1, width=2, font=('Ubuntu', 24), relief=GROOVE)
                ent3.place(relx=0.61, rely=0.85, anchor=CENTER)

                msg = Label(win, text='Think of a number between 1 and 20', font=("Courier", 25), relief=GROOVE)
                msg.place(relx=0.5, rely=0.09, anchor=CENTER)

                msg2 = Label(win, text='Remaining Chances', font=("Courier", 25), relief=GROOVE)
                msg2.place(relx=0.3, rely=0.85, anchor=CENTER)

                try_no = Button(win, width=8, text='TRY', font=('Courier', 25), command=fun, relief=GROOVE)
                try_no.place(relx=0.5, rely=0.5, anchor=CENTER)

                stop =tk.Button(win, text='stop', width=40, command=win.destroy, bg="red", activebackground="red", relief=GROOVE)
                stop.place(relx=0.75, rely=1, anchor=S)

                reset = tk.Button(win, text='Restart', width=40, command=restart, bg="red", activebackground="red", relief=GROOVE)
                reset.place(relx=0.75, rely=1, anchor=S)

                win.mainloop()