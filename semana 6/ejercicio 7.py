def verificar_numero_primos(numero):
    if numero <= 1:
        return False
    for i in range(2, numero//2 +1):
        if numero %i==0:
            return False 
    return True
    


def agregar_a_la_lista(lista):
    lista_numeros_primos=[]
    for numero in lista:
        if verificar_numero_primos(numero):
            lista_numeros_primos.append(numero)
    return lista_numeros_primos
        

        
lista_por_revisar= [3,5,8,6,90,2,34]
revision_y_listado_final= agregar_a_la_lista(lista_por_revisar)         
print(revision_y_listado_final)