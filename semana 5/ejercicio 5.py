
numeros= []
contador= 1

cantidad_numeros= int(input("ingrese cantidad de numeros: "))

while contador <= cantidad_numeros:
    numero= int(input("ingrese un numero"))
    contador= contador + 1
    numeros.append(numero)
print(f"los numeros anotados son:{numeros}")

numero_mayor= max(numeros)
print(f"el numero mayor es: {numero_mayor}")

