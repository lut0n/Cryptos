import tkinter as tk
from tkinter import ttk
from tkinter import *
 
text = ''
UseFile = False

#Getting input
def getTextInput():
	userInput = TextInput.get()
	return userInput
def getkey():
	userInput = Key.get()
	return userInput
#File system
def File():
    with open(getTextInput(), 'r') as f:
        global text
        global UseFile
        UseFile = True
        text = f.read()
        f.close()
def File_Of():
    global text
    global UseFile
    UseFile = False
    text = getTextInput()
#Encoding funcitons
def Encode_Com(msg):
    key = getkey()
    num = 1
    counter = 0
    c = 0
    out = ''
    for i in key:
        num += int(i)
    for i in msg:
        if c == len(key):
            c = 0
        counter += 1
        counter += int(key[c])
        c += 1
        out += chr(ord(i) + counter)
    TextInput.delete('0', END)
    global UseFile
    if not UseFile:
        TextInput.insert(tk.END, out)
    if UseFile:
        with open('Export.txt', 'w', encoding='utf-8') as f:
            f.write(out)
            f.close()
def Encode():
    Encode_Com(text)
def Decode_Com(msg):
    out = ''
    key = getkey()
    num = 1
    counter = 0
    c = 0
    for i in key:
        num += int(i)
    for i in msg:
        if c == len(key):
            c = 0
        counter += 1
        counter += int(key[c])
        out += chr(ord(i)- counter)
        c += 1
    TextInput.delete('0', END)
    global UseFile
    if not UseFile:
        TextInput.insert(tk.END, out)
    if UseFile:
        with open('Export.txt', 'w', encodeing='utf-8') as f:
            f.write(out)
            f.close()
def Decode():
    Decode_Com(text)
#Tkinter
root = Tk()

root.geometry('300x250')
root.configure(background='#fa0000')
root.title('Cryptos')

Button(root, text='Decode', command=Decode,bg='#750000').place(x=50, y=200)

Button(root, text='Encode', command=Encode,bg='#750000').place(x=150, y=200)

Button(root, text='File', command=File, bg='#750000').place(x=250, y=100)
Button(root, text='File_Of', command=File_Of, bg='#750000').place(x=250, y=150)

Button(root, text='Exit', command=root.destroy, bg='#ff4d4d').place(x=0, y=0)

Label(root, text='Cryptos', bg='#750000').place(x=120, y=20)

TextInput=Entry(root, bg='#ffcccc')
TextInput.place(x=90, y=140)

Key=Entry(root, bg='#ffcccc')
Key.place(x=90, y=80)

Label(root, text='key:', bg='#750000').place(x=120, y=50)

Label(root, text='text:', bg='#750000').place(x=120, y=100)
root.iconbitmap('Logo.ico')
root.mainloop()
