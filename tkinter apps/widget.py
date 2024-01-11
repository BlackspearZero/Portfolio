import tkinter as tk
from tkinter import ttk

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

# run
window.mainloop()