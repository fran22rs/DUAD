contador_de_nota= 1
cantidad_de_notas_aprobadas= 0 
cantidad_de_notas_desaprobadas= 0 
promedio_de_notas_total= 0
nota_actual= 0
promedio_de_notas_aprobadas= 0
promedio_de_notas_desaprobadas= 0
total_de_notas= int(input("ingrese la cantidad de notas:"))
while(contador_de_nota<= total_de_notas):
    print("ingrese la nota numero")
    print(contador_de_nota)
    nota_actual= float(input("ingrese la nota actual:"))
    if (nota_actual<70):
        cantidad_de_notas_desaprobadas= cantidad_de_notas_desaprobadas + 1
        promedio_de_notas_desaprobadas= promedio_de_notas_desaprobadas + nota_actual
    else:
        cantidad_de_notas_aprobadas= cantidad_de_notas_aprobadas + 1
        promedio_de_notas_aprobadas= promedio_de_notas_aprobadas + nota_actual
    promedio_de_notas_total=  promedio_de_notas_total + (nota_actual/total_de_notas)
    contador_de_nota= contador_de_nota + 1

if(promedio_de_notas_desaprobadas>0):
    promedio_de_notas_desaprobadas= promedio_de_notas_desaprobadas/cantidad_de_notas_desaprobadas
else:
    promedio_de_notas_desaprobadas= 0

if(promedio_de_notas_aprobadas>0):
    promedio_de_notas_aprobadas= promedio_de_notas_aprobadas/cantidad_de_notas_aprobadas
else:
    promedio_de_notas_aprobadas= 0

print("el estudiante tiene esta cantidad de notas aprobadas") 
print(cantidad_de_notas_aprobadas)
print("este es el promedio de notas aprobadas")
print(promedio_de_notas_aprobadas)
print("el estudiante tiene esta cantidad de notas desaprobadas") 
print(cantidad_de_notas_desaprobadas) 
print("este es el promedio de notas desaporbadas") 
print(promedio_de_notas_desaprobadas) 
print("este es el promedio total de notas")
print(promedio_de_notas_total)
