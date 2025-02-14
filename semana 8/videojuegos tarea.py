import csv 

def caracteristicas_juegos():
    
    nombre =input("nombre del juego:")
    genero =input("genero del juego:")
    desarrollador =input("su desarrollador:")
    clasificacion=input("clasificacion:")
    return {"nombre": nombre, "genero": genero, "desarrollador": desarrollador, "clasificacion": clasificacion}

def guardarlo_en_csv(path, data,):

    fieldnames= ["nombre" ,"genero", "desarrollador", "clasificacion"]

    with open(path, "w", encoding="utf-8") as file:
        writer= csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)


def main():
  juegos= []

  cantidad_juegos= int(input("ingrese el numero de juegos:"))
 

  for i in range(cantidad_juegos):
        videojuego= caracteristicas_juegos()
        juegos.append(videojuego)

  nombre_del_archivo= "mis_juegos_favoritos.csv"

  guardarlo_en_csv(nombre_del_archivo, juegos)

  print(f"se ha guardado con el nombre de:{nombre_del_archivo}")

if __name__=="__main__":
    main()

####################################################################################################################

import csv 

def caracteristicas_juegos():
    
    nombre =input("nombre del juego:")
    genero =input("genero del juego:")
    desarrollador =input("su desarrollador:")
    clasificacion=input("clasificacion:")
    return {"nombre": nombre, "genero": genero, "desarrollador": desarrollador, "clasificacion": clasificacion}

def guardarlo_en_csv(path, data,):

    fieldnames= ["nombre" ,"genero", "desarrollador", "clasificacion"]

    with open(path, "w", encoding="utf-8") as file:
        writer= csv.DictWriter(file, fieldnames=fieldnames, delimiter="\t")
        writer.writeheader()
        writer.writerows(data)


def main():
  juegos= []

  cantidad_juegos= int(input("ingrese el numero de juegos:"))
 

  for i in range(cantidad_juegos):
        videojuego= caracteristicas_juegos()
        juegos.append(videojuego)

  nombre_del_archivo= "mis_juegos_favoritos.csv"

  guardarlo_en_csv(nombre_del_archivo, juegos)

  print(f"se ha guardado con el nombre de:{nombre_del_archivo}")

if __name__=="__main__":
    main()





