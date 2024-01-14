import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title('Tkinter Variables')

string_var = tk.StringVar()

label = ttk.Label(master = window, text = 'label', textvariable = string_var)
label.pack()

entry = ttk.Entry(master = window, textvariable = string_var)
entry.pack()

window.mainloop()