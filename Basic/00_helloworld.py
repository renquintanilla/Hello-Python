# Clase en vídeo: https://youtu.be/Kp4Mvapo5kc

### Hola Mundo ###

# Nuestro hola mundo en Python
print("Hola Pythoncon comillas dobles")
print('Hola Python con comillas simples')

# Esto es un comentario

"""
Este es un
comentario
en varias líneas
"""

'''
Este también es un
comentario
en varias líneas
'''

# Cómo consultar el tipo de dato
print(type("Soy un dato str"))  # Tipo 'str'
print(type(5))  # Tipo 'int'
print(type(1.5))  # Tipo 'float'
print(type(3 + 1j))  # Tipo 'complex'
print(type(True))  # Tipo 'bool'
print(type(print("Mi cadena de texto")))  # Tipo 'NoneType'

print('El tipo de dato es ', type(5)) # Los número se imprimen sin comillas
print(type("Mi cadena de texto"))  # Tipo 'NoneType'