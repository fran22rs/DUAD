def canciones_ordenadas(path):
    with open(path, "r", encoding="utf-8") as file:
        lineas = file.readlines()
    
    lineas_ordenadas = sorted(lineas)
    
   
    with open(path, "w", encoding="utf-8") as file2:
        file2.writelines(lineas_ordenadas)