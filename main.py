from openpyxl import load_workbook
from tkinter import *
from tkinter import ttk
import random


root = Tk()
root.geometry('400x400+600+200')
root.title('Язык жестов')
root.config(background='#FFFFD3')
image = PhotoImage(file='./icon.png')
root.iconphoto(True, image)


text = StringVar()
input_digit = IntVar()

wb = load_workbook(filename='C:/Users/Maria/Documents/Gesticule_word.xlsx')
sheet = wb.active

book = []
for row in sheet.iter_rows(values_only=True):
    book.append(row[0])

len_book = len(book)


def form_sentence():
    n = input_digit.get()
    rand = [random.randint(0, len_book - 1) for _ in range(n)]
    output_text = ""
    for i in rand:
        output_text += book[i] + " "
    text.set(output_text.strip())


lbl1 = ttk.Label(textvariable=text, background='white', border=10, relief=SOLID, font=("Book Antiqua", 11),
                 anchor="center", wraplength=350)
lbl1.place(relheight=0.37, relwidth=0.94, relx=0.03, rely=0.03)
lbl2 = ttk.Label(text='КОЛИЧЕСТВО СЛОВ В ПРЕДЛОЖЕНИИ', background='#FFFFD3', font=("Book Antiqua", 11), anchor="center")
lbl2.place(relheight=0.07, relwidth=0.8, relx=0.1, rely=0.75)

ent = ttk.Spinbox(textvariable=input_digit, from_=1.0, to=20,background='white', font=("Book Antiqua", 11),
                  state="readonly")
ent.place(relheight=0.07, relwidth=0.2, relx=0.4, rely=0.83)

btn2 = ttk.Button(text='СФОРМИРОВАТЬ', command=form_sentence)
btn2.place(relheight=0.2, relwidth=0.5, relx=0.25, rely=0.49)


root.mainloop()


