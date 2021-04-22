import pyttsx3
import PyPDF2
from tkinter import *
from PIL import Image
from PIL import ImageTk
from tkinter import filedialog

bg = '#ffdab9'
app = Tk()
app.geometry('300x400')
app.title('Book Reader')
app.configure(bg=bg)
path = None

def click():
    global path
    path = filedialog.askopenfilename()
    print(path)
def talk():
    page_n = page_number_box.get()
    if path and page_n:
        speaker = pyttsx3.init()
        book = open(path, 'rb')
        read_file = PyPDF2.PdfFileReader(book)
        page = read_file.getPage(int(page_n))
        text = page.extractText()
        speaker.say(text)
        speaker.runAndWait()


image = Image.open('Audiobook.png')
imageResized = image.resize((70,70), Image.ANTIALIAS)
image1 = ImageTk.PhotoImage(imageResized)

logo = Label(app, image=image1, bg=bg)
logo.pack()

title = Label(app, text='Let listen to the book', bg=bg, font='none 20')
title.pack()

page_number = Label(app,text='Please enter the Page number', bg=bg)
page_number.pack(pady=(50,0))

page_number_box = Entry(app, bg=bg)
page_number_box.pack()

open_PDF = Button(app, text='Open', width=20, command=click)
open_PDF.pack(pady=(40,0))

say_PDF = Button(app, text='Talk', width=20, command=talk)
say_PDF.pack(pady=(20.0))
app.mainloop()

