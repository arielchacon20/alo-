import tkinter as tk
from tkinter import *
from tkinter import messagebox 
from login import Login

class Window (Tk):
    def __init__(self):
        super().__init__()
        self.title('DISHOP')
        self.geometry("800x500")
        self.resizable(False, False)
        self.config(bg= 'white')
        self.panel_login = Login(self)

ventana = Window()
ventana.mainloop()        

