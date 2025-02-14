lista_1= ["nombre","apellidos", "edad"]
lista_2= ["francisco","rodriguez", "31"]

diccionario={}

for index in range(len(lista_1)):
    diccionario[lista_1[index]]= lista_2[index]

print(diccionario)