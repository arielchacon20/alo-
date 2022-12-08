import tkinter as tk
from tkinter import *
from tkinter import messagebox
import cx_Oracle
import os

os.environ['TNS_ADMIN'] = 'C:\proyectos python\wallet'
conn = cx_Oracle.connect('sveas', '1QAZXSW23edc', 'bdd221_high')
c = conn.cursor()
c.execute('select * from usuarios')
for row in c:
    print(row)

class Login ():
    def __init__(self, master):
        self.login_frame = tk.Frame(master, width= 500, height= 450,
        bg= 'grey',
        highlightbackground= 'black', highlightthickness= 2)
        self.login_frame.place(x = 140, y = 20)
        
        self.login_label = tk.Label(self.login_frame,
        bg= 'white', text= 'Iniciar Sesión', font= ('Arial', 20),
        highlightbackground= 'black', highlightthickness= 2)
        self.login_label.place(x= 170, y= 10)

        self.user_label = tk.Label(self.login_frame,
        bg= 'grey', text= 'Usuario', font= ('Arial', 18))
        self.user_label.place(x= 210, y= 70)

        self.user_entry = tk.Entry(self.login_frame,
        bg= 'white',
        highlightbackground= 'black', highlightthickness= 2,
        width= 30, font= ('Arial', 15))
        self.user_entry.place(x= 80, y= 110)

        self.password_label = tk.Label(self.login_frame,
        bg= 'grey', text= 'Contraseña', font= ('Arial', 18))
        self.password_label.place(x= 190, y= 180)

        self.password_entry = tk.Entry(self.login_frame,
        bg= 'white', show= '*',
        highlightbackground= 'black', highlightthickness= 2,
        width= 30, font= ('Arial', 15))
        self.password_entry.place(x= 80, y= 220)

        self.login_button = tk.Button(self.login_frame,
        bg= 'grey', text= 'Iniciar Sesión', font= ('Arial', 18),
        highlightbackground= 'black', highlightthickness= 2,
        command= self.login)
        self.login_button.place(x= 170, y= 300)

    def login(self):
        self.user = self.user_entry.get()
        self.password = self.password_entry.get()