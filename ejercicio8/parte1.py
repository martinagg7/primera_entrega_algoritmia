def funcion_decoradora(funcion_parametro):
    def funcion_interior(*args):
        #Acciones para decorar
        print("Vamos a calcular el precio total con IVA :")
        funcion_parametro(*args)
        #Acciones adicionales
        print("Aqui tiene el  precio total con IVA")
    return funcion_interior



@funcion_decoradora
def precio_TII(precio_sin_impuestos,porcentaje_IVA):
    IVA=precio_sin_impuestos*porcentaje_IVA/100
    precio_TII=precio_sin_impuestos+IVA
    print(precio_TII)

precio_sin_impuestos = int(input("Introduce el precio sin impuestos: "))
porcentaje_IVA = int(input("Introduce el porcentaje de IVA: "))

precio_TII(precio_sin_impuestos,porcentaje_IVA)



    