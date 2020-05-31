import os

# Recibe un código postal y lo compara con una lista en un archivo externo
def es_valido(cp):
    cp_correcto = False
    fichero_cp = open(os.getcwd() + "\AutoTest\static\CP", "r")
    while not cp_correcto: 
        linea = fichero_cp.readline().rstrip("\n")
        if linea == cp: 
            cp_correcto = True 
            break 
        if not linea: 
            break 
    fichero_cp.close()

    # Retorna True/False dependiendo de si existe el código postal o no
    return cp_correcto