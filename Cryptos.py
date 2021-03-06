import tkinter as tk
from tkinter import ttk
from tkinter import *
import json
 
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
    with open(getTextInput(), 'r', encoding='utf-8') as f:
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
    with open('Log.json', 'r') as f:
        log_object = json.loads(f.read())
        f.close
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
        counter += c * int(key[c])
        counter -= c
        counter += num
        c += 1
        out += chr(ord(i) + counter)
    TextInput.delete(0, END)
    global UseFile
    log_object["Logs"] += [{"key":key, "text_input":msg, "text_output":out,"Encoding": True,"UseFile": UseFile}]    
    log_object_out = json.dumps(log_object, indent=1)
    with open('Log.json', 'w') as f:
            f.write(log_object_out)
            f.close()
    if not UseFile:
        TextInput.insert(tk.END, out)
    if UseFile:
        with open('Export.txt', 'w', encoding='utf-8') as f:
            f.write(out)
            f.close()       
def Encode():
    Encode_Com(text)
def Decode_Com(msg):
    with open('Log.json', 'r') as f:
        log_object = json.loads(f.read())
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
        counter += c * int(key[c])
        counter -= c
        counter += num
        out += chr(ord(i)- counter)
        c += 1
    TextInput.delete(0, END)
    global UseFile
    log_object["Logs"] += [{"key":key, "text_input":msg, "text_output":out,"Encoding": False,"UseFile": UseFile}]    
    log_object_out = json.dumps(log_object, indent=1)
    with open('Log.json', 'w') as f:
            f.write(log_object_out)
            f.close()
    if not UseFile:
        TextInput.insert(tk.END, out)
    if UseFile:
        with open('Export.txt', 'w', encoding='utf-8') as f:
            f.write(out)
            f.close()
def Decode():
    Decode_Com(text)
#Tkinter
root = Tk()

root.geometry('300x250')
root.title('Cryptos')

Button(root, text='Decode', command=Decode).place(x=50, y=200)

Button(root, text='Encode', command=Encode).place(x=150, y=200)

Button(root, text='File', command=File).place(x=250, y=100)
Button(root, text='File_Of', command=File_Of).place(x=250, y=150)

Button(root, text='Exit', command=root.destroy).place(x=0, y=0)

Label(root, text='Cryptos').place(x=120, y=20)

TextInput=Entry(root)
TextInput.place(x=90, y=140)

Key=Entry(root)
Key.place(x=90, y=80)

Label(root, text='key:').place(x=135, y=50)

Label(root, text='text:').place(x=135, y=110)

root.iconbitmap('Logo.ico')

root.mainloop()
