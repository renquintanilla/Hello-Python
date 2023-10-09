
def calculadora(num_uno, num_dos,operacion):
    if operacion == "+":
        resultado = num_uno + num_dos
        print(f"La suma de {num_uno} + {num_dos} es {resultado}")
    elif operacion == "-":
        resultado = num_uno - num_dos
        print(f"La resta de {num_uno} - {num_dos} es {resultado}")
    elif operacion == "*":
        resultado = num_uno * num_dos
        print(f"La Multiplicación de {num_uno} * {num_dos} es {resultado}")
    elif operacion  == "/":
        try:
           resultado = num_uno / num_dos
        except ZeroDivisionError:
            print("El segundo número debe ser mayor a cero")
            #num_dos = int(input("Segundo número "))
            #resultado = num_uno / num_dos
            #print(f"La división de {num_uno} / {num_dos} es {resultado}")
            #mejorar si el error es percistente o recursivo. Tarea.
        else:
            print(f"La división de {num_uno} / {num_dos} es {resultado}")
    else:
     print("Incluye un operador válido")
     
     #operador = input("Digite el operador  ")
     #resultado = num_uno / num_dos

     
    
num_uno = int(input("Primer número "))
num_dos = int(input("Segundo número "))
operador = input("Digite el operador ")

while operador != "/"  or operador != "+" or operador != "-" or operador != "*"  :
    operador = input("Digite  un operador válido (+ - * / )  ")

    if operador == "+"  or operador == "-" or operador == "*" or num_dos == 0 :
        break

    if operador == "/" and num_dos == 0  :
        num_dos = int(input("Digite un segundo número mayor que cero "))
        break
    
calculadora(num_uno, num_dos , operador)




