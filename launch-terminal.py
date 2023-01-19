import os
import subprocess
from tkinter import *

root = Tk()

def open_terminal():
    if os.name == 'nt':
        subprocess.run('cmd')
    elif os.name == 'posix':
        uname = os.uname()
        if uname.sysname == 'Linux':
            subprocess.run(['lxterminal'])
        else:
            subprocess.run(['open', '-a', 'Terminal'])
    else:
        subprocess.run(['gnome-terminal'])

button = Button(root, text="Run Terminal", command=open_terminal)
button.pack()

root.mainloop()
