from funciones import *
from tkinter import *
from io import open
from tkinter import messagebox

#------------Raiz y Frame------------------
root = Tk()
root.title("Calculadora")
root.resizable(False,False)

colorfondo=["grey",0] #Variable de fondo de calculadora

frame=Frame()
frame.pack(fill="both", expand=True)
frame.config(cursor='crosshair',bg=colorfondo[0])

#------------Variables ------------------
valoractual=StringVar()
valoractual.set("0")
operacionesyvalores=[]
resultado_anterior=0
colornumeros="black"
hubounerror=False

#------------Pantallas------------------
pantalla_prin=Entry(frame,textvariable=valoractual)
pantalla_prin.config(width=35,justify="right",fg=colornumeros,state="readonly")
pantalla_prin.grid(row=0,column=0,pady=6,columnspan=5)

fin=Label(frame,height=1,width=48,bg=colorfondo[0])
fin.grid(row=8,column=0,padx=4,columnspan=5)

#------------Menu----------
barmenu=Menu(frame)
root.config(menu=barmenu)
opciones=Menu(barmenu,tearoff=0)
barmenu.add_cascade(label="Opciones",menu=opciones)
opciones.add_command(label="Cerrar",command=lambda: funcerrar(root))
opciones.add_command(label="Cambiar color fondo",command=lambda: funfondo(frame,fin,colorfondo))

ayuda=Menu(barmenu,tearoff=0)
barmenu.add_cascade(label="Ayuda",menu=ayuda)
ayuda.add_command(label="Acerca de..",command=lambda: ayuda())

#------------Funciones----------
def ayuda():
        messagebox.showinfo("Calculadora","Primera versión de proyecto simple de python para utilizar interfaz gráfica.")

def resultado():
    operacionesyvalores.append(float(valoractual.get()))
    arrayaux=[]
    arrayaux=operacionesyvalores.copy()
    global hubounerror
    global resultado_anterior
    if len(operacionesyvalores)==1:
        resultado_anterior = operacionesyvalores[0]
        fin.config(text="Resultado: " + str(resultado_anterior))
        operacionesyvalores.clear()
        valoractual.set("0")
    else:
        i=0
        while i < len(operacionesyvalores):
            if operacionesyvalores[i] == '^':
                operacionesyvalores[i-1] = operacionesyvalores[i-1] ** operacionesyvalores[i+1]
                del operacionesyvalores[i:i+2]
            elif operacionesyvalores[i] == '^1/n':
                if operacionesyvalores[i+1] != 0 and float(operacionesyvalores[i-1])>=0:
                    operacionesyvalores[i-1] = operacionesyvalores[i-1] ** (1/operacionesyvalores[i+1])
                    del operacionesyvalores[i:i+2]
                else:
                    messagebox.showerror("Error","No se puede calcular la raiz")
                    fin.config(text="Error de sintaxis")
                    hubounerror=True
                    valoractual.set("0")
                    operacionesyvalores.clear()
                    return
            else:
                i += 1
        i = 0
        while i < len(operacionesyvalores):
            if operacionesyvalores[i] == 'x':
                    operacionesyvalores[i-1] = operacionesyvalores[i-1] * operacionesyvalores[i+1]
                    del operacionesyvalores[i:i+2]
            elif operacionesyvalores[i] == '/':
                    if operacionesyvalores[i+1] != 0:
                        operacionesyvalores[i-1] = operacionesyvalores[i-1] / operacionesyvalores[i+1]
                        del operacionesyvalores[i:i+2]
                    else:
                        messagebox.showerror("Error","No se puede dividir por cero")
                        fin.config(text="Error de sintaxis")
                        hubounerror=True
                        valoractual.set("0")
                        operacionesyvalores.clear()
                        return
            else:
                i += 1
        i = 0
        while i < len(operacionesyvalores):
            if operacionesyvalores[i] == '+':
                operacionesyvalores[i-1] = operacionesyvalores[i-1] + operacionesyvalores[i+1]
                del operacionesyvalores[i:i+2]
            elif operacionesyvalores[i] == '-':
                operacionesyvalores[i-1] = operacionesyvalores[i-1] - operacionesyvalores[i+1]
                del operacionesyvalores[i:i+2]
            else:
                i += 1

        resultado_anterior = operacionesyvalores[0]
        hacerhistorial(arrayaux,resultado_anterior,hubounerror)
        fin.config(text="Resultado: " + str(resultado_anterior))
        operacionesyvalores.clear()
        arrayaux.clear()
        valoractual.set("0")
        return


#------------Botones----------
#-----------Fila 1-----------
b7=Button(frame,text="7",width=5,command=lambda:darvalor("7",valoractual,fin),fg=colornumeros)
b7.grid(row=2,column=0)
b8=Button(frame,text="8",width=5,command=lambda:darvalor("8",valoractual,fin),fg=colornumeros)
b8.grid(row=2,column=1)
b9=Button(frame,text="9",width=5,command=lambda:darvalor("9",valoractual,fin),fg=colornumeros)
b9.grid(row=2,column=2)
bmult=Button(frame,text="x",width=5,command=lambda:operacion("x",operacionesyvalores,valoractual),fg=colornumeros)
bmult.grid(row=2,column=3)

#-----------Fila 2-----------
b4=Button(frame,text="4",width=5,command=lambda:darvalor("4",valoractual,fin),fg=colornumeros)
b4.grid(row=3,column=0)
b5=Button(frame,text="5",width=5,command=lambda:darvalor("5",valoractual,fin),fg=colornumeros)
b5.grid(row=3,column=1)
b6=Button(frame,text="6",width=5,command=lambda:darvalor("6",valoractual,fin),fg=colornumeros)
b6.grid(row=3,column=2)
bres=Button(frame,text="-",width=5,command=lambda:resta("-",operacionesyvalores,valoractual),fg=colornumeros)
bres.grid(row=3,column=3)

#-----------Fila 3-----------
b1=Button(frame,text="1",width=5,command=lambda:darvalor("1",valoractual,fin),fg=colornumeros)
b1.grid(row=4,column=0)
b2=Button(frame,text="2",width=5,command=lambda:darvalor("2",valoractual,fin),fg=colornumeros)
b2.grid(row=4,column=1)
b3=Button(frame,text="3",width=5,command=lambda:darvalor("3",valoractual,fin),fg=colornumeros)
b3.grid(row=4,column=2)
bsum=Button(frame,text="+",width=5,command=lambda:operacion("+",operacionesyvalores,valoractual),fg=colornumeros)
bsum.grid(row=4,column=3)

#-----------Fila 4-----------
b0=Button(frame,text="0",width=5,command=lambda:darvalor("0",valoractual,fin),fg=colornumeros)
b0.grid(row=5,column=0)
bdiv=Button(frame,text="/",width=5,command=lambda:operacion("/",operacionesyvalores,valoractual),fg=colornumeros)
bdiv.grid(row=5,column=2)
bdot = Button(frame, text=".", width=5, command=lambda: darvalor(".",valoractual,fin),fg=colornumeros)
bdot.grid(row=5, column=1)
bigual=Button(frame,text="=",width=5,command=lambda:resultado())
bigual.grid(row=5,column=3)

#-----------Fila 5-----------
bpot=Button(frame,text="^",width=5,command=lambda:operacion("^",operacionesyvalores,valoractual),fg=colornumeros)
bpot.grid(row=6,column=0)
braiz=Button(frame,text="^1/n",width=5,command=lambda:operacion("^1/n",operacionesyvalores,valoractual),fg=colornumeros)
braiz.grid(row=6,column=1)
braiz=Button(frame,text="<-",width=5,command=lambda:borrar(valoractual),fg=colornumeros)
braiz.grid(row=6,column=2)
bansw=Button(frame,text="Res",width=5,command=lambda:usaranterior(valoractual,resultado_anterior),fg=colornumeros)
bansw.grid(row=6,column=3)

root.mainloop()