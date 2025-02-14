print("por favor ingrese 3 numeros para determinar el mayor")
numero1=float(input("numero uno"))
numero2=float(input("numero dos"))
numero3=float(input("numero tres"))
if (numero1>numero2 and numero1> numero3):
 print(f"el mayor es {numero1}")
elif(numero2> numero1 and numero2 >numero3):
 print(f"el mayor es {numero2}") 
else:
 print(f"el mayor es {numero3}")

