class Banco:
    def __init__(self, nombre, apellido, cedula, numCuenta, saldo, retiro=0, ingreso=0):
        self._nombre = nombre
        self._apellido = apellido
        self._cedula = cedula
        self._numCuenta = numCuenta
        self._saldo = saldo
        self._retiro = retiro
        self._ingreso = ingreso

    @property
    def nombre(self):
        return self._nombre

    @property
    def apellido(self):
        return self._apellido

    @property
    def cedula(self):
        return self._cedula

    @property
    def numCuenta(self):
        return self._numCuenta

    @property
    def saldo(self):
        return self._saldo

    @property
    def retiro(self):
        return self._retiro

    @property
    def ingreso(self):
        return self._ingreso

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido

    @cedula.setter
    def cedula(self, cedula):
        self._cedula = cedula

    @numCuenta.setter
    def numCuenta(self, numCuenta):
        self._numCuenta = numCuenta

    @saldo.setter
    def saldo(self, saldo):
        self._saldo = saldo

    @retiro.setter
    def retiro(self, retiro):
        self._retiro = retiro

    @ingreso.setter
    def ingreso(self, ingreso):
        self._ingreso = ingreso

    def retiroDinero(self):
        return self.saldo - self.retiro

    def agregarDinero(self):
        return self.saldo + self.ingreso


opcion = int(input("Elija una opción: 1. Consultar cliente, 0 salir: "))
cliente = Banco("Mateo", "Quintero", 102838266, 267855, 3500000)

while (opcion != 0):
    consultar = int(input("Ingrese la cedula a consultar: "))
    if consultar == cliente.cedula:
        print(f"La persona es: {cliente.nombre} {cliente.apellido}")
        menu = int(
            input('Ingrese si desea 1 retirar o 2 agregar o 3 consultar saldo: '))
        if menu == 1:
            cliente.retiro = int(input("Ingrese el Valor a retirar: "))
            cliente.retiroDinero()
            print(
                f"El retiro de {cliente.nombre} fue de {cliente.retiro} el saldo restante es: {cliente.retiroDinero()}")
        elif menu == 2:
            cliente.ingreso = int(input("Ingrese el Valor a consignar: "))
            cliente.agregarDinero()
            print(
                f"La consignación de {cliente.nombre} fue de {cliente.ingreso} el saldo total es: {cliente.agregarDinero()}")
        elif menu == 3:
            cliente.saldo
            print(f'Su saldo actual es de: {cliente.saldo}')
        else:
            print("Opcion no válida")
    else:
        print("Usuario no encontrado")
    opcion = int(input("Elija una opción: 1. Consultar cliente, 0 salir: "))
