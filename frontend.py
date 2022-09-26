from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image #pip install Pillow for this

window = tk.Tk()

bgcolour=("ivory2")
bgcolour2 = ("snow2")
window.configure(background=bgcolour)
window.geometry("1500x900+10+10")
window.title("Tulu Translator")

tk.Label(window, text="WELCOME TO TULU-ENGLISH TRANSLATOR!",fg = "tomato",bg='white',font = "Verdana 32 bold").pack(pady=20)   


img = ImageTk.PhotoImage(Image.open("translator.jpeg"))
label = Label(window, image = img).pack()

def translate_button():
    translate_window = Toplevel(window)
    translate_window.title("Translate Window")
    translate_window.geometry("1500x900+10+10")
    tk.Label(translate_window).pack()
    
    tk.Label(translate_window, text="WELCOME TO TULU-ENGLISH TRANSLATOR!",fg = "tomato",bg='white',font = "Verdana 32 bold").pack(pady=20)
    tk.Button(translate_window, text="Typing",fg = "black",bg='white',font = "Verdana 26 bold").pack(side=LEFT, anchor='ne', padx=25, pady=5)
    tk.Button(translate_window, text="Speaking",fg = "black",bg='white',font = "Verdana 26 bold").pack(side=RIGHT, anchor='nw', padx=25, pady=5)
    
    translate_window.mainloop()



def translatenow_button():
    translatenow_window = Toplevel(window)
    translatenow_window.title("Button Window")
    translatenow_window.geometry("1500x900+10+10")
    tk.Label(translatenow_window).pack()
    
    tk.Label(translatenow_window, text="WELCOME TO TULU-ENGLISH TRANSLATOR!",fg = "tomato",bg='white',font = "Verdana 32 bold").pack(pady=20)
    tk.Button(translatenow_window, text="Enter Word",fg = "black",bg='white',font = "Verdana 26 bold").pack(side=LEFT, anchor='ne', padx=25, pady=5)
    tk.Button(translatenow_window, text="Enter Sentence",fg = "black",bg='white',font = "Verdana 26 bold").pack(side=RIGHT, anchor='nw', padx=25, pady=5)
    

    tk.Button(translatenow_window, text="Translate",fg = "black",bg='white',font = "Verdana 26 bold", command=translate_button).pack(side=TOP, anchor='n', padx=25, pady=5)
    translatenow_window.mainloop()
    
tk.Button(window, text="Translate Now!",fg = "blue",bg='white',font = "Verdana 26 bold", command=translatenow_button).pack(pady= 70)



window.mainloop() #this is reqd for the tkinter window to open