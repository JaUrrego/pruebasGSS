
from ast import Lambda
from tkinter import *
from tkinter import ttk
from conexion import DataBase


ventana=Tk()
ventana.title("Pruebas GSS")
ventana.geometry("1600x1500")

marco=LabelFrame(ventana )
marco.place(x=50, y=50, width=1500, height=1400)

db=DataBase()

tabla= ttk.Treeview(marco)
tabla.grid(column=0, row=3,columnspan=4)
tabla["columns"]=("CEDULA","NOMBRE", "FECHA ALQUILER", "TIEMPO ALQUILADO", "SALDO", "PLACA", "MARCA")
tabla.column("#0", width=0, stretch=NO)
tabla.column("CEDULA", width=150, anchor=CENTER)
tabla.column("NOMBRE", width=150, anchor=CENTER)
tabla.column("FECHA ALQUILER", width=150, anchor=CENTER)
tabla.column("TIEMPO ALQUILADO", width=150, anchor=CENTER)
tabla.column("SALDO", width=150, anchor=CENTER)
tabla.column("PLACA", width=150, anchor=CENTER)
tabla.column("MARCA", width=150, anchor=CENTER)
tabla.heading("#0",text="")
tabla.heading("CEDULA",text="CEDULA", anchor=CENTER)
tabla.heading("NOMBRE",text="NOMBRE", anchor=CENTER)
tabla.heading("FECHA ALQUILER",text="FECHA ALQUILER", anchor=CENTER)
tabla.heading("TIEMPO ALQUILADO",text="TIEMPO ALQUILADO", anchor=CENTER)
tabla.heading("SALDO",text="SALDO", anchor=CENTER)
tabla.heading("PLACA",text="PLACA", anchor=CENTER)
tabla.heading("MARCA",text="MARCA", anchor=CENTER)

btnConsultar=Button(marco,text="Consultar" )
btnConsultar.grid(column=1,row=4)
btnConsultar=Button(marco,text="Filtrar")
btnConsultar.grid(column=2,row=4)

def vaciarTabla():
    filas=tabla.get_children()
    for fila in filas:
      tabla.delete(fila)  


def consulta():
    vaciarTabla()
    sql="select cliente.cedula, cliente.nombre, alquiler.fecha, alquiler.timpo_en_dias, alquiler.saldo, carro.placa, carro.marcafrom cliente, alquiler, carro"
    db.cursor.execute(sql)
    filas=db.cursor.fetchall()
    for fila in filas:
        tabla.insert("", END, text="",values=fila)


consulta()
ventana.mainloop()