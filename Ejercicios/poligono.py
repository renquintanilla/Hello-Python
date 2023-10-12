def area_poligono(a,b):
  triangulo = a * b/2
  cuadrado = a * a
  rectangulo = a * b
  print(f"Al área del triángulo es {triangulo}")  
  print(f"Al área del cuadrado es {cuadrado}")   
  print(f"Al área del rectángulo es {rectangulo}")  

tipo_poligono = ""
while tipo_poligono != "4":
    print("******************************************************")
    print("********* MENÚ CÁLCULO DE ÁREA DE POLÍGONOS **********")
    print("******************************************************")
    print("1. Triángulo")
    print("2. Cuadrado")
    print("3. Rectángulo")
    print("4. Salir")
    print("******************************************************")
    tipo_poligono = int(input("Qué área de polígono quiere calcular? ")) 
    if tipo_poligono == 1:
        print("Seleccionó un Triángulo")
        base = int(input("Base? "))
        altura= int(input("Altura? "))
        area_poligono(base,altura)
        break
    elif tipo_poligono == 2:
        print("Seleccionó un Cuadrado")
        lado1 = int(input("Lado? "))
        lado2 = lado1
        area_poligono(lado1, lado2)
        break
    elif tipo_poligono == 3:
        print("Seleccionó un Rectángulo")
        largo = int(input("Largo? "))
        ancho= int(input("Ancho? "))
        area_poligono(largo,ancho)
        break
    elif tipo_poligono == 4:
        break
