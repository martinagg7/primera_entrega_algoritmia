#MEDIA

def funcion_decoradora(funcion_parametro):
    def funcion_interior(*args):
        #Acciones para decorar
        print("Vamos a realizar la media de los tres numeros :")
        funcion_parametro(*args) #introducimos los argumentos
        #Acciones adicionales
        print("Fin de la media")
    return funcion_interior


@funcion_decoradora
def media(num1,num2,num3):
    print ((num1+num2+num3)/3)

num1 = int(input("Introduce el primer numero: "))
num2 = int(input("Introduce el segundo numero: "))
num3 = int(input("Introduce el tercer numero: "))

media(num1,num2,num3)