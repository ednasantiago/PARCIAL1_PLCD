import string
import random

minusculas_ascii = string.ascii_lowercase
print(minusculas_ascii)

mayusculas_ascii = string.ascii_uppercase
print(mayusculas_ascii)

numeros = string.digits
print(numeros)


def generarContraseña(n):
    contraseña = [] 
    contraseña.append(random.choice(mayusculas_ascii))
    contraseña.append(random.choice(minusculas_ascii))
    contraseña.append(random.choice(numeros))

    all_characters = minusculas_ascii + mayusculas_ascii + numeros
    
for _ in range ( n - 3):  
    contraseña.append(random.choice(all_characters))  
    
    contraseña=''.join(contraseña)
    contraseña=''.join(random.sample(contraseña,len(contraseña)))   
    
    return contraseña

   
for i in range(10, 20):
    print(generarContraseña(i))