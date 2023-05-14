#Creamos la funcion programa y ponemos de parametro el array que convertiremos en palabra
def Ejercicio5_Programa(array):
    #Creamo la variable 'var_Fila', 'var_Columnas' y usamos la funcion len para obtener cantidad de
    # elementos del array
    var_Fila = len(array)
    var_Columnas = len(array[0])
    #Creamos una lista vacia que la llenaremos con el array
    palabras = []
    #Iteramos la variable var_Columnas
    for i in range(var_Columnas):
        #Creamos la variable palabra para llenar mediante la lista var_Fila
        palabra = ''
        for a in range (var_Fila):
            if array[a][i] != '':
                palabra += array[a][i]
        #Utilizamos la funcion append para agregar a los arrays de la variable palabra a palabras
        palabras.append(palabra)
        #Retornamos un espacio entre palabras y unimos el array
    return ' '.join(palabras)
#El array donde pondremos las letras para convertir a palabras
array = [
    ['J', 'L', 'L', 'M'],
    ['u', 'i', 'i', 'a'],
    ['s', 'v', 'f', 'n'],
    ['t', 'e', 'e', '']
]
#Cremoas la variable "var_palabra" para almacenar la funcion del programa
var_palabra = Ejercicio5_Programa(array)
#Imprimos la variable "var_palabra"
print(var_palabra)