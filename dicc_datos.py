import itertools

caracteres = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ0123456789"

combinaciones = itertools.product(caracteres, repeat=4)

nombre_archivo = input("Por favor, ingresa el nombre del archivo para guardar las combinaciones: ")

try:
    with open(nombre_archivo, "w") as archivo:
        for combinacion in combinaciones:
            archivo.write("".join(combinacion) + "\n")
    print("Se han guardado todas las combinaciones en", nombre_archivo)
except Exception as e:
    print("Ocurrió un error al intentar guardar el archivo:", e)
