def funcion_decoradora(funcion_parametro):
    def funcion_interior(*args):
        #decoramos
        print("Vamos a calcular los intereses")
        funcion_parametro(*args)
        print("Estos son los intereses")
    return funcion_interior



@funcion_decoradora
def intereses(tiempo_en_meses,capital,interes):
    print(capital*interes*tiempo_en_meses/100/12)

tiempo_en_meses = int(input("Introduce el tiempo en meses: "))
capital = int(input("Introduce el capital: "))
interes = int(input("Introduce el interes: "))
intereses(tiempo_en_meses,capital,interes)