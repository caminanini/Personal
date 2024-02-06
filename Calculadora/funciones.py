from tkinter import messagebox

#Sobre el formato:
def funfondo(frameparam,finparam,arrayparam):
    arrayparam[1]=arrayparam[1]+1
    if arrayparam[1]== 1:
        arrayparam[0]="black"
    elif arrayparam[1]== 2:
        arrayparam[0]="pink"
    elif arrayparam[1]== 3:
        arrayparam[0]="light blue"
    elif arrayparam[1]== 4:
        arrayparam[0]="green"
    else:
        arrayparam[0]="grey"
        arrayparam[1]=0

    frameparam.config(bg=arrayparam[0])
    finparam.config(bg=arrayparam[0])

def funcerrar(rootparam):
    respuesta=messagebox.askquestion("Cerrar","¿Seguro que quiere salir?")
    if respuesta=="yes":
        rootparam.destroy()

def hacerhistorial(array,resultadodeoperaciones,existeerror):
    if not existeerror:
        historial=open("Historial de cuentas","a")
        for i in array:
            historial.write(str(i))
        historial.write("\n")
        historial.write("Esta cuenta da:{}".format(resultadodeoperaciones))
        historial.write("\n")
        historial.close()

#Sobre la funcionalidad:
def borrar(valorpantalla):
    valor=valorpantalla.get()
    valor=valor[:-1]
    valorpantalla.set(valor)
    return

def operacion(ops,resultadodeoperaciones2,valorpantalla2):
    resultadodeoperaciones2.append(float(valorpantalla2.get()))
    resultadodeoperaciones2.append(ops)
    valorpantalla2.set("0")

def resta(ops,resultadodeoperaciones3,valorpantalla3):
    if valorpantalla3.get()=="0":
        valorpantalla3.set("-")
    else:
        resultadodeoperaciones3.append(float(valorpantalla3.get()))
        resultadodeoperaciones3.append(ops)
        valorpantalla3.set("0")

def usaranterior(valorpantalla4,resanterior):
    valorpantalla4.set(str(resanterior))
    return

def darvalor(numero,valorpantalla5,finparam2):
    existecoma = "." in valorpantalla5.get()
    if numero == "." and existecoma:
        finparam2.config(text="Error de sintaxis")
        valorpantalla5.set("0")
        return
    if valorpantalla5.get() == "0" and numero == "0":
        pass
    elif valorpantalla5.get() == "0" and numero != "0":
        valorpantalla5.set("{}".format(numero))
    elif valorpantalla5.get() == "0" and numero == "." and not existecoma:
        valorpantalla5.set("0" + numero)
    else:
        valorpantalla5.set(valorpantalla5.get() + numero)
