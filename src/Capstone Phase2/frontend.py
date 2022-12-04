from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image
import os
import time

from add import addSent
import generate
import translate
import audio
from graph import App

if __name__ == "__main__":
    print("Started app.")
    uri = "neo4j+s://2eadc3dc.databases.neo4j.io"
    user = "neo4j"
    password = "Wvkgl4wC8yQD8HrHJCrUWhAbs1RJ4EkWYfT8BsIGDIo"
    app = App(uri, user, password)

window = tk.Tk()
window.configure(background = "ivory2")
window.state('zoomed')
window.title("Tulu Translator")
window.geometry("1400x800")
tk.Label(window, text = "WELCOME TO TULU-ENGLISH TRANSLATOR!", fg = "blue", font = "Verdana 32 bold").pack(pady = 20)


img = ImageTk.PhotoImage(Image.open("translator.jpeg"))
#img=Image.open('langlearn.jpg').resize((300,300))
#img=ImageTk.PhotoImage(img)

label = Label(window, image = img).pack()
window.iconphoto(False, img)

mode = tk.IntVar() #for translate
lang = tk.IntVar() #for translate
buttonval = tk.StringVar() #for generate
txtval = tk.StringVar() #for generate
txtval1 = tk.StringVar() #for generate
posval = [] #for generate
eng_var = tk.StringVar() #for add sentence
tulu_var = tk.StringVar() #for add sentence

#start page
def start_button():
    start_window = Toplevel(window)
    start_window.title("Tulu Translator")
    start_window.state('zoomed')
    start_window.geometry("1400x800")
    tk.Label(start_window).pack()
    tk.Label(start_window, text="WELCOME TO TULU-ENGLISH TRANSLATOR!",fg = "blue",bg='white',font = "Verdana 32 bold").pack(pady=20)
    tk.Button(start_window, text="Enter Sentence",fg = "white",bg='green',font = "Supreme 26 bold", activebackground="#f00", activeforeground="#fff",command=enterSent_button).pack(pady=40)
    tk.Button(start_window, text="Generate Sentence",fg = "white",bg='green',font = "Supreme 26 bold", activebackground="#f00", activeforeground="#fff",command=generateSent_button).pack(pady=40)
    tk.Button(start_window, text="Translate Sentence",fg = "white",bg='green',font = "Supreme 26 bold", activebackground="#f00", activeforeground="#fff",command=translateSent_button).pack(pady=40)
    start_window.mainloop()

def info_button():
    info_window = Toplevel(window)
    info_window.title("Tulu Translator")
    info_window.state('zoomed')
    info_window.geometry("1100x200")
    tk.Label(info_window).pack()
    font_tuple = ("Comic Sans Ms", 15, "bold")
    tk.Label(info_window, text="generate sentence - model generates a sentence and you can determine if the sentence is correct or not!",font=font_tuple).pack()
    tk.Label(info_window, text="translate sentence - model helps you translate a sentence using either audio or text!",font=font_tuple).pack()
    tk.Label(info_window, text="enter sentence - you can feed in new sentences into the model to help it learn!",font=font_tuple).pack()
    info_window.mainloop()

def quit_button():
    quit()

#enter sentence
def enterSent_button():
    enter_window = Toplevel(window)
    enter_window.title("Tulu Translator- Enter Sentence")
    enter_window.state('zoomed')
    enter_window.geometry("1400x800")
    tk.Label(enter_window).pack()

    tk.Label(enter_window, text = "Enter sentence", fg = "green", font = "Serif 27 bold italic").pack(pady = 20, side = TOP, anchor = 'w')
    tk.Label(enter_window, text = 'English:', font=('Verdana',20, 'bold')).pack(pady=30)
    tk.Entry(enter_window,textvariable = eng_var, font=('Verdana',20,'normal')).pack(pady=35)
    tk.Label(enter_window, text = 'Tulu:', font = ('Verdana',20,'bold')).pack(pady=45)
    tk.Entry(enter_window,textvariable = tulu_var, font=('Verdana',20,'normal')).pack(pady=50)
    tk.Button(enter_window,text = 'Submit',fg = "white",bg='#2F74D3',font = "Verdana 20 bold", command = enterSent_submit).pack(pady=60)
    enter_window.mainloop()

def enterSent_submit():
    eng=eng_var.get()
    tulu=tulu_var.get()
    print("English entry : " + eng)
    print("Tulu entry : " + tulu)
    addSent(eng, tulu, app)
    eng_var.set("")
    tulu_var.set("")

#generate sentence
def generateSent_button():
    generateSent_window = Toplevel(window)
    generateSent_window.title("Tulu Translator- Generate Sentence")
    generateSent_window.state('zoomed')
    generateSent_window.geometry("1400x800")
    tk.Label(generateSent_window).pack()

    tk.Label(generateSent_window, text="Generate Sentence",fg = "green",font = "Serif 27 bold italic").pack(pady=20, side=TOP, anchor='w')
    text = Entry(generateSent_window, textvariable = txtval, state='disabled', width=100, justify='center', font=('Verdana',50,'normal')).pack()
    text1 = Entry(generateSent_window, textvariable = txtval1, state='disabled', width=100, justify='center', font=('Verdana',50,'normal')).pack()

    sent = generate.generate_sentence(app)
    txtval.set(sent[0])
    txtval1.set(translate.translateTulu(sent[0], app))
    global posval
    posval = sent[1]
#    text.pack()

    #insert 3 images of correct, incorrect, questionmark
    correct=Image.open('correct.png').resize((150,150))
    correct=ImageTk.PhotoImage(correct)
    incorrect=Image.open('incorrect.png').resize((150,150))
    incorrect=ImageTk.PhotoImage(incorrect)
    questionmark=Image.open('questionmark.png').resize((150,150))
    questionmark=ImageTk.PhotoImage(questionmark)

    cbutton=tk.Button(generateSent_window,image=correct,borderwidth=0,command=lambda m='correct': which_button(m)).pack(padx= 70, pady= 80, side=LEFT, anchor='w')
    qbutton=tk.Button(generateSent_window,image=questionmark,borderwidth=0,command=lambda m='questionmark': which_button(m)).pack(padx= 70, pady= 80, side=LEFT, anchor='center')
    ibutton=tk.Button(generateSent_window,image=incorrect,borderwidth=0,command=lambda m='incorrect': which_button(m)).pack(padx= 70, pady= 80, side=LEFT, anchor='e')

    generateSent_window.mainloop()

def which_button(button_press): #dispays on the terminal which button - correct/question mark/incorrect was clicked
    print(button_press)
    global posval
    generate.update_prob(posval, button_press, app)
    sent = generate.generate_sentence(app)
    txtval.set(sent[0])
    txtval1.set(translate.translateTulu(sent[0], app))
    posval = sent[1]

#translate sentence
def translateSent_button():
    translateSent_window = Toplevel(window)
    translateSent_window.title("Tulu Translator- Translate")
    translateSent_window.state('zoomed')
    translateSent_window.geometry("1400x800")
    tk.Label(translateSent_window).pack()
    #tk.Label(translateSent_window, text="WELCOME TO TULU-ENGLISH TRANSLATOR!",fg = "tomato",bg='white',font = "Verdana 32 bold").pack(pady=20)
    tk.Label(translateSent_window, text="Translate Sentence",fg = "green",font = "Serif 27 bold italic").pack(pady=20, side=TOP, anchor='w')

    tk.Label(translateSent_window, text="Language preference:",fg = "black",font = "Verdana 27 bold italic").pack(pady=20, side=TOP, anchor='center')
    tk.Radiobutton(translateSent_window, text="English",variable=lang,fg = "black",bg='white',indicatoron = 0, font = "Verdana 26",value=1).pack(side=TOP, anchor='center', padx=25, pady=15)
    tk.Radiobutton(translateSent_window, text="Tulu",variable=lang,fg = "black",bg='white',indicatoron = 0, font = "Verdana 26",value=2).pack(side=TOP, anchor='center', padx=25, pady=15)

    tk.Label(translateSent_window, text="Input Format:",fg = "black",font = "Verdana 27 bold italic").pack(pady=20, side=TOP, anchor='center')
    t1 = tk.Radiobutton(translateSent_window, text="Audio", variable=mode, indicatoron = 0, fg = "black",bg='white',font = "Verdana 26",value=1)
    t1.pack(side=TOP, anchor='center', padx=25, pady=15)
    t2 = tk.Radiobutton(translateSent_window, text="Text", variable=mode, indicatoron = 0, fg = "black",bg='white',font = "Verdana 26", value=2)
    t2.pack(side=TOP, anchor='center', padx=25, pady=15)
    tk.Button(translateSent_window, text="OK",fg = "white",bg='#2F74D3',font = "Verdana 26", command=display_input).pack(anchor='center', pady=10)
    print('mode of translation:',mode.get())
    print('language:',lang.get())
    translateSent_window.mainloop()

def display_input():
    if mode.get()==2:
        print("text var 1")
        translateSentText_button()
    elif mode.get()==1:
        print("audio var 1")
        translateSentAudio_button()

def translateSentText_button():
    translateSentText_window = Toplevel(window)
    translateSentText_window.title("Translate by Text")
    translateSentText_window.state('zoomed')
    translateSentText_window.geometry("1400x800")
    tk.Label(translateSentText_window).pack()
    if lang.get()==1:
        l="English"
    else:
        l="Tulu"

    #tk.Label(translateSentText_window, text="WELCOME TO TULU-ENGLISH TRANSLATOR!",fg = "tomato",bg='white',font = "Verdana 32 bold").pack(pady=20)
    tk.Label(translateSentText_window, text="Translate Sentence using Text",fg = "green",font = "Serif 27 bold italic").pack(pady=20, side=TOP, anchor='w')
    tk.Label(translateSentText_window, text="Use "+l,fg = "black",font = "Verdana 15 bold").pack(pady=20, side=TOP, anchor='w')
    tk.Label(translateSentText_window, text="Enter your input:",fg = "black",font = "Verdana 27 bold").pack(pady=20, side=TOP, anchor='center')

    inputtxt=Text(translateSentText_window, height = 5, width = 70, font=40)
    inputtxt.pack()

    printButton = tk.Button(translateSentText_window, text = "Translate Text" ,font='Helvetica 25', command=lambda : texttranslate(inputtxt,lbl)).pack()
    lbl = tk.Label(translateSentText_window, text = "")
    lbl.pack()

    translateSentText_window.mainloop()

def translateSentAudio_button():
    translateSentAudio_window = Toplevel(window)
    translateSentAudio_window.title("Translate by Audio")
    translateSentAudio_window.state('zoomed')
    translateSentAudio_window.geometry("1400x800")
    tk.Label(translateSentAudio_window).pack()

    if lang.get()==1:
        l="English"
    else:
        l="Tulu"


    #tk.Label(translateSentAudio_window, text="WELCOME TO TULU-ENGLISH TRANSLATOR!",fg = "tomato",bg='white',font = "Verdana 32 bold").pack(pady=20)
    tk.Label(translateSentAudio_window, text="Translate Sentence using Audio",fg = "green",font = "Serif 27 bold italic").pack(pady=20, side=TOP, anchor='w')
    tk.Label(translateSentAudio_window, text="Speak in "+l,fg = "black",font = "Verdana 15 bold").pack(pady=20, side=TOP, anchor='w')
    tk.Label(translateSentAudio_window, text="Enter your input:",fg = "black",font = "Verdana 27 bold").pack(pady=20, side=TOP, anchor='center')

    text = Text(translateSentAudio_window,  height = 5, width = 70, font=40)
    text.pack()

    if lang.get()==1:
        recordbutton = Button(translateSentAudio_window, text='Record', bg='Sienna', font='Helvetica 20', command=lambda: text.insert(END, audio.recognizeEnglishVoice()))
        recordbutton.pack()
    elif lang.get()==2:
        recordbutton = Button(translateSentAudio_window, text='Record', bg='Sienna', font='Helvetica 20', command=lambda: text.insert(END, audio.recognizeTuluVoice()))
        recordbutton.pack()

    printButton = tk.Button(translateSentAudio_window, text = "Translate Text" ,font='Helvetica 25', command=lambda : texttranslate(text,lbl)).pack()
    lbl = tk.Label(translateSentAudio_window, text = "")
    lbl.pack()

    translateSentAudio_window.mainloop()

def texttranslate(inputtxt,lbl):
    inp = inputtxt.get(1.0, "end-1c")
    if lang.get()==1:
        oup = translate.translateEnglish(inp, app)
    else:
        oup = translate.translateTulu(inp, app)
    lbl.config(text = "Translated text: "+oup, font = "Verdana 27 bold")  #have to pass inp as the actual translated text

#main page
tk.Button(window, text="Start",fg = "white",bg='blue',font = "Verdana 26 bold",  activebackground="#67DAFF", activeforeground="#fff",command=start_button).pack(pady= 70)
tk.Button(window, text="Quit",fg = "white",bg='blue',font = "Verdana 26 bold",  activebackground="#67DAFF", activeforeground="#fff",command=quit_button).pack()
info=Image.open('info.png')
info=info.resize((50,50))
info=ImageTk.PhotoImage(info)
tk.Button(window, text="   Info",font='Helvetica 25 bold',fg = "black",bg='white',image=info,compound=LEFT, command=info_button).pack(anchor='e',side='bottom')
window.mainloop() #this is reqd for the tkinter window to open
