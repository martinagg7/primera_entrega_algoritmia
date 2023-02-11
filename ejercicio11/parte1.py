def funcion_decoradora(funcion_parametro):
    def funcion_interior(*args):
        print("Calcularemos lo que hemos ganado en horas extra")
        funcion_interior(*args)
        print("Esto es lo que hemos ganado en horas extra")
    return funcion_interior





@funcion_decoradora
def horas(salario_fijado_mes,horas_trabajadas_extra):
    paga_hora=salario_fijado_mes/420
    horas_entre_36_43=max(0,min(horas_trabajadas_extra,43))-35
    ganancia_horas_entre_36_43=horas_entre_36_43*paga_hora*1.5
    horas_mas_44=max(0,horas_trabajadas_extra-43)
    ganancia_horas_mas_44=horas_mas_44*paga_hora*1.75
    ganancia_total=ganancia_horas_entre_36_43+ganancia_horas_mas_44

    print(ganancia_total)

salario_fijado_mes = int(input("Introduce el salario fijado al mes: "))
horas_trabajadas_extra = int(input("Introduce las horas trabajadas extra: "))

horas(salario_fijado_mes,horas_trabajadas_extra)
