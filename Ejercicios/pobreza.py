# Niveles de Pobreza para MI 
pe = 57
pe2 = 90
pe3 = 97
pe4 = 110
nope = 220

ingresos = int(input("Cuánto es tu ingreso? "))

print(type(ingresos))

print(f"Su ingreso es de {ingresos}")

if ingresos <= pe:
    print("Usted esta en pobreza extrema")

elif ingresos > pe and ingresos <= pe2:
     print("Usted esta en segundo nivel de pobreza")


elif ingresos > pe2  and ingresos <= pe3:
     print("Usted esta en tercer nivel de pobreza")


elif ingresos > pe3 and ingresos <= pe4:
     print("Usted esta en cuarto nivel de pobreza")


else :
     print("Usted no es pobre")


persona = {
    "Nombre": "René",
    "Apellido": "Quintanilla",
    "Edad": 47,
    "Lenguajes": {"Python", "PHP", "Angular"},
    "Antiguedad": 2
}

print(type(persona))

print(persona["Apellido"])