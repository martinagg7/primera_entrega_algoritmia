class Cuenta_bancaria:
    def __init__(self,nombre_usuario,saldo):
        self.nombre = nombre_usuario
        self.saldo = saldo
    
    def depositar(self, cantidad):
        self.saldo =self.saldo + cantidad
        return self.saldo
    
    def retirar(self, cantidad):
        if self.saldo >=0:
            self.saldo =self.saldo - cantidad
            return self.saldo
        else:
            print("Esta en numeros rojos")
    