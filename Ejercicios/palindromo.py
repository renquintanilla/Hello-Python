def palindromo (cadena):
             cadena = cadena.replace(" ", "").lower()
             text_dos = cadena [::-1]    
             print(text_dos)     
             if cadena == text_dos:
                print(f"El texto {cadena} es Palíndromo")
             else: 
                  print(f"El texto {cadena}  no es Palíndromo")

text_uno = input("Ingrese el texo para verificaciòn de Palíndromo: ")

palindromo(text_uno)
