lista_por_eliminar = ["nombre", "altura","peso"]

estudiante1= {"apellido":"rodriguez", "edad":"31 años", "nombre": "francisco", "altura": "173cm"}



for key in lista_por_eliminar:
    if estudiante1.get(key):
        estudiante1.pop(key)


        
print(estudiante1)