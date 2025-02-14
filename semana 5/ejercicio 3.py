numero= [1,2,3,4,5,6,7]

ultimo_numero= len(numero)-1

numero[0], numero[ultimo_numero]= numero[ultimo_numero], numero[0]
print(numero)