from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image #pip install Pillow for this
import audio
import os
import translate
from graph import App
if __name__ == "__main__":
    print("Started app.")
    uri = "neo4j+s://2eadc3dc.databases.neo4j.io"
    user = "neo4j"
    password = "Wvkgl4wC8yQD8HrHJCrUWhAbs1RJ4EkWYfT8BsIGDIo"
    app = App(uri, user, password)


window = tk.Tk()

bgcolour=("ivory2")
bgcolour2 = ("snow2")
window.configure(background=bgcolour)
window.geometry("1500x900+10+10")
window.title("Tulu Translator")

tk.Label(window, text="WELCOME TO TULU-ENGLISH TRANSLATOR!",fg = "tomato",bg='white',font = "Verdana 32 bold").pack(pady=20)


img = ImageTk.PhotoImage(Image.open("translator.jpeg"))
label = Label(window, image = img).pack()

mode = tk.IntVar()
lang = tk.IntVar()

def enterSent_submit():

    eng=eng_var.get()
    tulu=tulu_var.get()

    print("English entry : " + eng)
    print("Tulu entry : " + tulu)

    eng_var.set("")
    tulu_var.set("")

def enterSent_button():
    enterSent_window = Toplevel(window)
    enterSent_window.title("Button Window")
    enterSent_window.geometry("1500x900+10+10")
    tk.Label(enterSent_window).pack()

    tk.Label(enterSent_window, text="WELCOME TO TULU-ENGLISH TRANSLATOR!",fg = "tomato",bg='white',font = "Verdana 32 bold").pack(pady=20)
    tk.Label(enterSent_window, text="Enter Sentence",fg = "black",font = "Verdana 27 bold").pack(pady=20, side=TOP, anchor='w')
    eng_label = tk.Label(enterSent_window, text = 'English:', font=('Verdana',20, 'bold')).pack(pady=30)
    eng_entry = tk.Entry(enterSent_window,textvariable = eng_var, font=('Verdana',20,'normal')).pack(pady=35)
    tulu_label = tk.Label(enterSent_window, text = 'Tulu:', font = ('Verdana',20,'bold')).pack(pady=45)
    tulu_entry=tk.Entry(enterSent_window,textvariable = tulu_var, font=('Verdana',20,'normal')).pack(pady=50)
    sub_btn=tk.Button(enterSent_window,text = 'Submit',fg = "blue",bg='white',font = "Verdana 20 bold", command = enterSent_submit).pack(pady=60)


    enterSent_window.mainloop()

def translateSentAudio_button():
    translateSentAudio_window = Toplevel(window)
    translateSentAudio_window.title("Button Window")
    translateSentAudio_window.geometry("1500x900+10+10")
    tk.Label(translateSentAudio_window).pack()

    if lang.get()==1:
        l="English"
    else:
        l="Tulu"


    tk.Label(translateSentAudio_window, text="WELCOME TO TULU-ENGLISH TRANSLATOR!",fg = "tomato",bg='white',font = "Verdana 32 bold").pack(pady=20)
    tk.Label(translateSentAudio_window, text="Translate Sentence using Audio",fg = "black",font = "Verdana 27 bold").pack(pady=20, side=TOP, anchor='w')
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
    oup = translate.translateEnglish(inp, app)
    lbl.config(text = "Translated text: "+oup, font = "Verdana 27 bold")  #have to pass inp as the actual translated text
    #return inputtxt



def translateSentText_button():
    translateSentText_window = Toplevel(window)
    translateSentText_window.title("Button Window")
    translateSentText_window.geometry("1500x900+10+10")
    tk.Label(translateSentText_window).pack()

    tk.Label(translateSentText_window, text="WELCOME TO TULU-ENGLISH TRANSLATOR!",fg = "tomato",bg='white',font = "Verdana 32 bold").pack(pady=20)
    tk.Label(translateSentText_window, text="Translate Sentence using Text",fg = "black",font = "Verdana 27 bold").pack(pady=20, side=TOP, anchor='w')

    tk.Label(translateSentText_window, text="Enter your input:",fg = "black",font = "Verdana 27 bold").pack(pady=20, side=TOP, anchor='center')

    inputtxt=Text(translateSentText_window, height = 5, width = 70, font=40)
    inputtxt.pack()

    printButton = tk.Button(translateSentText_window, text = "Translate Text" ,font='Helvetica 25', command=lambda : texttranslate(inputtxt,lbl)).pack()
    lbl = tk.Label(translateSentText_window, text = "")
    lbl.pack()

    translateSentText_window.mainloop()


def display_input():
    translateSent_window = Toplevel(window)

    if mode.get()==2:
        print("text var 1")
        #translateSentText_button=
        tk.Button(translateSent_window, text="OK",fg = "blue",bg='white',font = "Verdana 26 bold", command=translateSentText_button).pack(side=RIGHT, anchor='nw', padx=25, pady=5)
        #ok_button.config(translateSent_window,command=translateSentText_button).pack()
        #ok_text.pack()
    elif mode.get()==1:
        print("audio var 1")
        tk.Button(translateSent_window, text="OK",fg = "blue",bg='white',font = "Verdana 26 bold", command=translateSentAudio_button).pack(side=RIGHT, anchor='nw', padx=25, pady=5)
        #ok_button.config(translateSent_window,command=translateSentAudio_button).pack()
        #ok_audio.pack()

def translateSent_button():
    translateSent_window = Toplevel(window)
    translateSent_window.title("Button Window")
    translateSent_window.geometry("1500x900+10+10")
    tk.Label(translateSent_window).pack()
    tk.Label(translateSent_window, text="WELCOME TO TULU-ENGLISH TRANSLATOR!",fg = "tomato",bg='white',font = "Verdana 32 bold").pack(pady=20)
    tk.Label(translateSent_window, text="Translate Sentence",fg = "black",font = "Verdana 27 bold").pack(pady=20, side=TOP, anchor='w')

    tk.Label(translateSent_window, text="Language preference:",fg = "black",font = "Verdana 27 bold").pack(pady=20, side=TOP, anchor='center')
    tk.Radiobutton(translateSent_window, text="English",variable=lang,fg = "black",bg='white',indicatoron = 0, font = "Verdana 26 bold",value=1).pack(side=TOP, anchor='center', padx=25, pady=15)
    tk.Radiobutton(translateSent_window, text="Tulu",variable=lang,fg = "black",bg='white',indicatoron = 0, font = "Verdana 26 bold",value=2).pack(side=TOP, anchor='center', padx=25, pady=15)

    tk.Label(translateSent_window, text="Input Format:",fg = "black",font = "Verdana 27 bold").pack(pady=20, side=TOP, anchor='center')
    t1 = tk.Radiobutton(translateSent_window, text="Audio input", variable=mode, indicatoron = 0, command=display_input,fg = "black",bg='white',font = "Verdana 26 bold",value=1)
    t1.pack(side=TOP, anchor='center', padx=25, pady=5)
    t2 = tk.Radiobutton(translateSent_window, text="Text input", variable=mode, indicatoron = 0, command=display_input,fg = "black",bg='white',font = "Verdana 26 bold", value=2)
    t2.pack(side=TOP, anchor='center', padx=25, pady=5)


    tk.Button(translateSent_window, text="OK",fg = "blue",bg='white',font = "Verdana 26 bold").pack(side=RIGHT, anchor='nw', padx=25, pady=5)
    print('mode of translation:',mode.get())
    print('language:',lang.get())
    translateSent_window.mainloop()



def which_button(button_press): #dispays on the terminal which button - correct/question mark/incorrect was clicked
    print(button_press)


def generateSent_button():
    generateSent_window = Toplevel(window)
    generateSent_window.title("Button Window")
    generateSent_window.geometry("1500x900+10+10")
    tk.Label(generateSent_window).pack()

    tk.Label(generateSent_window, text="WELCOME TO TULU-ENGLISH TRANSLATOR!",fg = "tomato",bg='white',font = "Verdana 32 bold").pack(pady=20)
    tk.Label(generateSent_window, text="Generate Sentence",fg = "black",font = "Verdana 27 bold").pack(pady=20, side=TOP, anchor='w')

    text = Text(generateSent_window, height = 5, width = 70, font=40, bg='black', fg='white')
    tk.Label(generateSent_window, text="generated some sentence....",fg = "tomato",bg='white',font = "Verdana 32 bold").pack(pady=20, anchor='center')
    sentGenerated="a man is flying"
    text.insert(END, sentGenerated)
    text.pack()

    #insert 3 images of correct, incorrect, questionmark
    correct=Image.open('correct.png')
    correct=correct.resize((150,150))
    correct=ImageTk.PhotoImage(correct)

    incorrect=Image.open('incorrect.png')
    incorrect=incorrect.resize((150,150))
    incorrect=ImageTk.PhotoImage(incorrect)

    questionmark=Image.open('questionmark.png')
    questionmark=questionmark.resize((150,150))
    questionmark=ImageTk.PhotoImage(questionmark)


    tk.Label(image=correct)
    cbuttton=tk.Button(generateSent_window,image=correct,borderwidth=0,command=lambda m='correct': which_button((m))).pack(padx= 70, pady= 80, side=LEFT, anchor='w')
    tk.Label(image=questionmark)
    qbutton=tk.Button(generateSent_window,image=questionmark,borderwidth=0,command=lambda m='questionmark': which_button((m))).pack(padx= 70, pady= 80, side=LEFT, anchor='center')
    tk.Label(image=incorrect)
    ibutton=tk.Button(generateSent_window,image=incorrect,borderwidth=0,command=lambda m='incorrect': which_button((m))).pack(padx= 70, pady= 80, side=LEFT, anchor='e')

    generateSent_window.mainloop()



def info_button():
    info_window = Toplevel(window)
    info_window.title("Info Window")
    info_window.geometry("1100x150")
    tk.Label(info_window).pack()

    font_tuple = ("Comic Sans Ms", 15, "bold")
    tk.Label(info_window, text="generate sentence - model generates a sentence and you can determine if the sentence is correct or not!",font=font_tuple).pack()
    tk.Label(info_window, text="translate sentence - model helps you translate a sentence using either audio or text!",font=font_tuple).pack()
    tk.Label(info_window, text="enter sentence - you can feed in new sentences into the model to help it learn!",font=font_tuple).pack()

    info_window.mainloop()


def start_button():
    start_window = Toplevel(window)
    start_window.title("Button Window")
    start_window.geometry("1500x900+10+10")
    tk.Label(start_window).pack()

    tk.Label(start_window, text="WELCOME TO TULU-ENGLISH TRANSLATOR!",fg = "tomato",bg='white',font = "Verdana 32 bold").pack(pady=20)
    tk.Button(start_window, text="Generate Sentence",fg = "black",bg='white',font = "Verdana 26 bold", command=generateSent_button).pack(side=LEFT, anchor='ne', padx=25, pady=5)
    tk.Button(start_window, text="Translate Sentence",fg = "black",bg='white',font = "Verdana 26 bold", command=translateSent_button).pack(side=LEFT, anchor='nw', padx=25, pady=5)
    tk.Button(start_window, text="Enter Sentence",fg = "black",bg='white',font = "Verdana 26 bold", command=enterSent_button).pack(side=LEFT, anchor='n', padx=25, pady=5)
    #tk.Button(start_window, text="Enter Sentence",fg = "black",bg='white',font = "Verdana 26 bold").pack(side=TOP, anchor='n', padx=25, pady=5)

    start_window.mainloop()

audio_var = tk.IntVar() #variable under translateSent_button
text_var = tk.IntVar()  #variable under translateSent_button

eng_var=tk.StringVar() #variable under generateSent_button
tulu_var=tk.StringVar()#variable under generateSent_button

tk.Button(window, text="Start",fg = "blue",bg='white',font = "Verdana 26 bold", command=start_button).pack(pady= 70)
info=Image.open('info.png')
info=info.resize((50,50))
info=ImageTk.PhotoImage(info)
tk.Button(window, text="   Info",font='Helvetica 25 bold',fg = "black",bg='white',image=info,compound=LEFT, command=info_button).pack(anchor='e',side='bottom')

window.mainloop() #this is reqd for the tkinter window to open
