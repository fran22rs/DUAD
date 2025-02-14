def menu_calculadora():
    print("calculadora, ingrese un numero")
    print("1: suma")
    print("2: resta")
    print("3: multiplicacion") 
    print("4: division")
    print("5: borrar resultado")
  


def operaciones():
 numero_inicial=0

 while True:

    try:
        opcion= int(input("escoja una opcion:"))
        
        if opcion < 1 or opcion > 5:
            print("opcion invalida")
            continue

        elif opcion == 5:
            numero_inicial=0
            print(numero_inicial)

        try:
            nuevo_numero= float(input("ingrese nuevo numero:"))
        except ValueError as ex :
         print(f"error:{ex}")
         continue 

        if opcion == 1:
            numero_inicial+=nuevo_numero
            print(numero_inicial)

        elif opcion ==2:
            numero_inicial-=nuevo_numero
            print(numero_inicial)   

        elif opcion ==3:
            numero_inicial*=nuevo_numero
            print(numero_inicial)

        elif opcion ==4:
            if nuevo_numero==0:
                print("no se puede dividir")
            else: 
                numero_inicial/=nuevo_numero
                print(numero_inicial)   

    except ValueError as ex:
        print(f"error:{ex}")          

def main():
    try:
        menu_calculadora()
        operaciones()      
    except Exception as ex:
        print(ex)

if __name__ == "__main__":
    main()