#*------------------Nota del autor*------------------JeremyEB
#Hay dos manera de resolver el problema de los caracteres comunes
#1-Manera y la correcta ya que contara las palabras comunes exactas

def Eleccion1():
    # Ingresar primera palabra
    palabra1 = str(input("Ingresar la primera palabra: "))
    # Ingresar segunda palabra
    palabra2 = str(input("Ingresar la segunda palabra: "))

    # Se crea la primera funcion siendo los parametros las palabras ingresadas
    def function(palabra1, palabra2):
        # creamos una variables que sera igual a los parametros ingresados pero con la funcion set
        # La funcion set nos ayudara a ver cuantas caracteres SIN repetir habra el lista ej:
        # aabcc y adcaa En esa ocasion los terminos a Y c se repiten mas de una vez la funcion no que solo hay una a Y una c
        terminosComunes = set(palabra1) & set(palabra2)
        # Y aqui imprimimos la variable con la funcion len que nos muestra la longitud
        return len(terminosComunes)

    totales = function(palabra1, palabra2)
    print("El número de caracteres comunes es: ", totales)
    input("Presiona una tecla para terminar el programa: ")

def Eleccion2():
    # Ingresar primera palabra
    palabra1 = str(input("Ingresar la primera palabra: "))
    # Ingresar segunda palabra
    palabra2 = str(input("Ingresar la segunda palabra: "))
    # Se crea la primera funcion siendo los parametros las palabras ingresadas
    def function(palabra1, palabra2):
        # Creamos un contador
        count = 0
        # Creamos un bucle que nos ira recorriendo la primera palabra mediante la funcion set y se iran guardando en la funcion char
        for char in set(palabra1):
            # Creamos aqui un condicion que nos ira comparando la palabra2 con la palabra1 en sus terminos con la funcion char
            if char in palabra2:
                # Y aqui el contador ira aumentando por cada palabra que sea igual y usamos la funcino min para que tambien sume los
                # terminos unicos con el ejemplo de aabcc y adcaa, seria la palabras b y d
                count += min(palabra1.count(char), palabra2.count(char))
        return count

    result = function(palabra1, palabra2)
    print("El número de caracteres comunes es: ", result)
    input("Presiona una tecla para terminar el programa: ")

print("------Elegir las cual de las opciones------------")
print("1-Mostrar la cantidad exacta de caracteres comunes")
print("2-Mostrar la cantidad de caracteres comunes tal cual como pide el ejercicio")
eleccion = str(input("Elegir: "))
if eleccion == "1":
    Eleccion1()
elif eleccion == "2":
    Eleccion2()