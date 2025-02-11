from tkinter import *
from tkinter import ttk
import random
import pandas as pd


root = Tk()
root.geometry('400x400+600+200')
root.title('Язык жестов')
root.config(background='#FFFFD3')
image = PhotoImage(file='./icon.png')
root.iconphoto(True, image)


text = StringVar()
input_digit = IntVar()
data = StringVar(value='ВСЕ')
for_cod = ""
test = True

file_path = "C:/Users/Maria/Documents/Gesticule_word.xlsx"
df = pd.read_excel(file_path)

book = {'ВСЕ': []}
common_len = 0
for column_data in df.columns:
    book[column_data] = df[column_data].dropna().tolist()
    book['ВСЕ'].extend(book[column_data])
choice = list(book.keys())


def form_sentence():
    global for_cod
    n = input_digit.get()
    name = data.get()
    rand = [random.randint(0, len(book[name]) - 1) for _ in range(n)]
    output_text = ""
    for i in rand:
        output_text += book[name][i] + " "
    text.set(output_text.strip())
    for_cod = text.get()


def decoding():
    global test
    if test:
        text.set("HELLO")
        test = False
    else:
        text.set(for_cod)
        test = True


lbl1 = ttk.Label(textvariable=text, background='white', border=10, relief=SOLID, font=("Book Antiqua", 11),
                 anchor="center", wraplength=350)
lbl1.place(relheight=0.37, relwidth=0.94, relx=0.03, rely=0.03)
lbl2 = ttk.Label(text='КОЛИЧЕСТВО СЛОВ В ПРЕДЛОЖЕНИИ', background='#FFFFD3', font=("Book Antiqua", 11), anchor="center")
lbl2.place(relheight=0.07, relwidth=0.8, relx=0.1, rely=0.75)

ent = ttk.Spinbox(textvariable=input_digit, from_=1.0, to=20,background='white', font=("Book Antiqua", 11),
                  state="readonly")
ent.place(relheight=0.07, relwidth=0.2, relx=0.4, rely=0.83)

btn1 = ttk.Button(text='РАСШИФРОВКА', command=decoding)
btn1.place(relheight=0.07, relwidth=0.94, relx=0.03, rely=0.37)
btn2 = ttk.Button(text='СФОРМИРОВАТЬ', command=form_sentence)
btn2.place(relheight=0.2, relwidth=0.5, relx=0.25, rely=0.49)

offset = 0
style = ttk.Style()
style.configure("TRadiobutton", background='#FFFFD3')
for i in range(len(choice)):
    ttk.Radiobutton(text=choice[i], value=choice[i], variable=data).place(relheight=0.05, relwidth=0.12, relx=offset,
                                                                          rely=0.93)
    offset += 0.13


root.mainloop()


