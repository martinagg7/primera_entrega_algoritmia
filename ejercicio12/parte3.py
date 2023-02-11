class Cuenta_bancaria:
    def __init__(self,nombre_usuario,saldo,descubierto=0):
        self.nombre = nombre_usuario
        self.saldo = saldo
        self.descubierto = descubierto


    def depositar(self, cantidad):
        self.salfo=self.saldo+cantidad
        return self.saldo
    
    def retirar(self, cantidad):
        if self.saldo >=0:
            self.saldo =self.saldo - cantidad
            return self.saldo
        else:
            print("Esta en numeros rojos")

    def mostrar_saldo(self):
        return self.saldo


    def cambio_descubierto(self,nuevo_descubierto):
        self.descubierto=nuevo_descubierto