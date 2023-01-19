import os
import subprocess
from tkinter import *

root = Tk()

def open_terminal():
    if os.name == 'nt':
        subprocess.run('cmd')
    elif os.name == 'posix':
        subprocess.run(['open', '-a', 'Terminal'])
    else:
        subprocess.run(['gnome-terminal'])

button = Button(root, text="Run Terminal", command=open_terminal)
button.pack()

root.mainloop()
