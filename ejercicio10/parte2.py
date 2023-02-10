#AREA DEL TRIANGULO RECTANGULO
def  funcion_decoradora(funcion_parametro):
    def funcion_interior(*args):
        #Acciones para decorar
        print("Vamos a calcular el area del triangulo con los lados perpendiculares:")
        funcion_parametro(*args)
        print("Ya hemos calculado el area del triangulo")
    return funcion_interior













@funcion_decoradora
def area_triangulo_rectangulo(lado1,lado2):
    print((lado1*lado2)/2)

lado1 = int(input("Introduce el primer lado del triangulo: "))
lado2 = int(input("Introduce el segundo lado del triangulo: "))

area_triangulo_rectangulo(lado1,lado2)