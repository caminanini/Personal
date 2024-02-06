
def resolver_funcion(funcion, valor):
    try:
        resultado = eval(funcion, {'x': valor})
        return resultado
    except (NameError, SyntaxError):
        print("Error al evaluar la expresión. Asegúrate de que la función sea válida.")
        return None


def biseccion():
    fun = input("Dar la funcion (en términos de x):")
    extizq = float(input("Dar extremo izquierdo:"))
    extder = float(input("Dar extremo derecho:"))
    iteraciones = int(input("Dar máximo número de iteraciones (entero):"))
    tolerror = float(input("Dar la tolerancia para el error:"))
    tolvalores = float(input("Dar la tolerancia para los valores funcionales:"))
    
    u = resolver_funcion(fun, extizq)
    if u is None:
            print("No se pudo resolver la funcion")
            return
    v = resolver_funcion(fun, extder)
    if v is None:
            print("No se pudo resolver la funcion")
            return
    
    if (u > 0 and v > 0) or (u < 0 and v < 0) or (u == 0 and v == 0):
        print("La función no cumple con el criterio de cambio de signo en el intervalo dado.")
        return
    
    for k in range(iteraciones):
        e = (extder - extizq) / 2
        mid = extizq + e
        w = resolver_funcion(fun, mid)
        
        if abs(w) < tolerror and abs(e) < tolvalores:
            print(f"La raíz aproximada es: {mid}")
            return
        
        if (w > 0 and u < 0) or (w < 0 and u > 0) or (w == 0 and u > 0) or (w == 0 and u < 0) or (w < 0 and u == 0) or (w > 0 and u == 0):
            extder = mid
            v = w
        else:
            extizq = mid
            u = w

def newton():
    fun = input("Dar la funcion (en términos de x):")
    derifun = input("Dar la funcion derivada (en términos de x):") #Corregir para que se calcule automáticamente
    x0 = float(input("Dar aproximación inicial:"))
    iteraciones = int(input("Dar máximo número de iteraciones (entero):"))
    tolerror = float(input("Dar la tolerancia para el error:"))
    tolvalores = float(input("Dar la tolerancia para los valores funcionales:"))

    v = resolver_funcion(fun, x0)
    if v is None:
            print("No se pudo resolver la funcion")
            return

    if abs(v) < tolvalores:
            print(f"La raíz aproximada es: {x0}")
            return
    for k in range(iteraciones):

        f_derivada_value = resolver_funcion(derifun, x0)
        x1 = x0 - v / f_derivada_value
        v = resolver_funcion(fun, x1)
        
        if abs(x1 - x0) < tolerror or abs(v) < tolvalores:
            print(f"La raíz aproximada es: {x1}")
            return
        
        x0 = x1
    print("El método de Newton no convergió después de las iteraciones especificadas.")

def puntofijo():
    fung = input("Dar la funcion de punto fijo (en términos de x):")
    p0 = float(input("Dar aproximación inicial:"))
    iteraciones = int(input("Dar máximo número de iteraciones (entero):"))
    tolerror = float(input("Dar la tolerancia para el error:"))
    i=1
    while i <= iteraciones:
        p=resolver_funcion(fung,p0)
        if p is None:
            print("No se pudo resolver la funcion")
            return
        if abs(p-p0)<tolerror:
            print(f"La aproximación de punto fijo es: {p}")
            return
        i=i+1
        p0=p
print("El método de punto fijo no convergió después de las iteraciones especificadas.")

print("Calculadora de ecuaciones no lineales\n")
print("¿Qué método usar? (Biseccion, Newton, Punto fijo)\n")
opcion = input().capitalize()

while True:
    if opcion in ["Biseccion", "Newton", "Punto fijo"]:
        break
    else:
        print("Opción no válida\n")
        opcion = input().capitalize()

if opcion == "Biseccion": 
    biseccion()
elif opcion == "Newton": 
    newton()
elif opcion == "Punto fijo":
    puntofijo()
