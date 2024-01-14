import tkinter as tk
from tkinter import ttk

def button_func():
    entry_text = entry.get()
    label['text'] = entry_text
    entry['state'] = 'disabled'

def reset_func():
    label['text'] = 'some text'
    entry['state'] = 'enabled'


window = tk.Tk()
window.title('Getting and setting widgets')

label = ttk.Label(master = window, text = 'Some text')
label.pack()

entry = ttk.Entry(master = window)
entry.pack()

button = ttk.Button(master = window, text = 'The button', command = button_func)
button.pack()

excercise_button = ttk.Button(master = window, text = 'excercise button', command = reset_func)
excercise_button.pack()

window.mainloop()