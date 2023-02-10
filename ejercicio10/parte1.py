#AREA TRIÁNGULO
def funcion_decoradora(funcion_parametro):
    def funcion_interior(*args):
        #Acciones para decorar
        print("Vamos a calcular el area del triangulo :")
        funcion_parametro(*args) #introducimos los argumentos
        #Acciones adicionales
        print("Ya hemos calculado el area del triangulo")
    return funcion_interior


@funcion_decoradora
def area_triangulo(base,altura):
    print((base*altura)/2)

base = int(input("Introduce la base del triangulo: "))
altura = int(input("Introduce la altura del triangulo: "))

area_triangulo(base,altura)










