
import string

caracteres_ascii = string.ascii_letters
print(caracteres_ascii)

def verificar(cadena):
    
 return all(caracter in caracteres_ascii for caracter in cadena)
 
cadena1 = "Esto es un a cadena$"
print(verificar(cadena1))

cadena2 = "Sololetras"
print(verificar(cadena2))