import json

def cargar_pokemon_desde_archivo(path):

        with open(path, 'r') as file:
            data = json.load(file)
        return data


def agregar_pokemon(path):
 

 try:
     nombre = input("Ingrese el nombre del nuevo Pokémon: ")
     tipo = input("Ingrese el tipo : ")
     hp = int(input("Ingrese el HP: "))
     ataque = int(input("Ingrese el ataque: "))
     defensa = int(input("Ingrese la defensa: "))
     sp_ataque = int(input("Ingrese el ataque: "))
     sp_defensa = int(input("Ingrese la defensa: "))
     velocidad = int(input("Ingrese la velocidad: "))
 except ValueError as ex:
        return print(f"ingrese uncaracter valido:{ex}")
    
 nuevo_pokemon = {
        "name": {
            "english": nombre
        },
        "type": tipo,
        "base": {
            "HP": hp,
            "Attack": ataque,
            "Defense": defensa,
            "Sp. Attack": sp_ataque,
            "Sp. Defense": sp_defensa,
            "Speed": velocidad
        }
    }
    
 pokemon_data = cargar_pokemon_desde_archivo(path)
  
 pokemon_data.append(nuevo_pokemon)
    
 with open(path, 'w') as file:
        json.dump(pokemon_data, file, indent=2)
        print(f"se ha agregado {nombre} al archivo {path}")


if __name__ == "__main__":
    archivo_json = "pokemon.json"
    agregar_pokemon(archivo_json)