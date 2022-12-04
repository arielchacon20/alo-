import cx_Oracle
import os
import tkinter


os.environ['TNS_ADMIN'] = 'C:\proyectos python\wallet'
conn = cx_Oracle.connect('sveas', '1QAZXSW23edc', 'bdd221_high')
c = conn.cursor()
c.execute('select * from usuarios')
for row in c:
    print(row)

class Ventana():
    def __init__(self):
        self.raiz = tkinter.Tk()
        self.frm= tkinter.Frame(self.raiz)
        self.frm.grid(row=0,column=0)
        self.raiz.title("prueba")
        self.raiz.geometry("300x75")
        self.boton = tkinter.Button(self.frm, text="iniciar sesion ",command=self.destroy)
        self.boton.grid(row=6,column=3)
        self.label = tkinter.Label(self.frm, text="Ingrese Id")
        self.label.grid(row=0,column=0)
        self.entry = tkinter.Entry(self.frm)
        self.entry.grid(row=0,column=3)
        self.label = tkinter.Label(self.frm, text="Ingrese contraseña")
        self.label.grid(row=3,column=0)
        self.contra= tkinter.Entry(self.frm, show="*")
        self.contra.grid(row=3,column=3)
        self.raiz.mainloop()
    def Accion(self):
        print("sesion iniciada, bienvenido "+str(self.entry.get()))
    def destroy(self):
        self.frm.destroy()

screen = Ventana()



conn.commit()
print("cambios guardados con exito.")