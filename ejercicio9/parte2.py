#MEDIA PONDERADA

def funcion_decoradora(funcion_parametro):
    def funcion_interior(*args):
        #Acciones para decorar
        print("Vamos a realizar la media ponderada de los tres numeros :")
        funcion_parametro(*args) #introducimos los argumentos
        #Acciones adicionales
        print("Fin de la media")
    return funcion_interior


@funcion_decoradora
def media_ponderada(a,b,c,num1,num2,num3):
    media=(a*num1+b*num2+c*num3)/(a+b+c)
    print(media)

a=float(input("Introduce el primer coeficiente de ponderación: "))
b=float(input("Introduce el segundo coeficiente de ponderación: "))
c=float(input("Introduce el tercer coeficiente de ponderación: "))
num1 = int(input("Introduce el primer numero: "))
num2 = int(input("Introduce el segundo numero: "))
num3 = int(input("Introduce el tercer numero: "))

media_ponderada(a,b,c,num1,num2,num3)