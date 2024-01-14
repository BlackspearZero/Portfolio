import tkinter as tk
from tkinter import ttk

def button_func():
    print('Hello World!')

def ex_func():
    print('Hello')

# window
window = tk.Tk()
window.title('Windows and Widgets')
window.geometry('800x500')

# ttk label
label = ttk.Label(master = window, text = 'This is a test')
label.pack()

# tk.text
text = tk.Text(master = window)
text.pack()

# ttk entry
entry = ttk.Entry(master = window)
entry.pack()

ex_label =  ttk.Label(master = window, text = 'my label' )
ex_label.pack()

my_button = ttk.Button(master = window, text= 'excercise button', command = ex_func)
my_button.pack()

# ttk button
button = ttk.Button(master = window, text = 'A VButton', command = button_func)
button.pack()

# run
window.mainloop()