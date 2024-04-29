from datetime import date
from abc import ABC , abstractmethod
import sys, os, platform

sistema = platform.system()

linux = 'Linux'

if sistema == linux:
    def limpiar():
        os.system("clear")
else:
    def limpiar():
         os.system("cls")


def recibir():
    print('''
    ================================================
          CUENTAS BANCARIAS - JAVIER RAMIREZ
          soii.xavii@gmail.com DNI: 28445575
    ================================================
    ''')

def salir():
    recibir()
    print('''
                Está seguro de salir?
    ''')
    seguro = input('                       (s/n): ').upper()

    limpiar()

    if seguro == 'S':
        sys.exit()
    else:
        recibir()
    

def continuar():
    seguir = input('          Desea ejecutar otro ejercicio? (s/n): ').upper()

    limpiar()

    if seguir == 'S':
        recibir()
        operaciones()
    else:
        salir()


class CuentaBancaria(ABC):
    def __init__(self,nombre_titular,dni_titular, fecha_nacimiento, saldo=0):
        self._nombre_titular = nombre_titular
        self._dni_titular = dni_titular
        self._fecha_nacimiento = fecha_nacimiento
        self._saldo = saldo

    def obtener_saldo(self):
        return self._saldo
    
    @abstractmethod
    def depositar(self):
        pass

    @abstractmethod
    def extraer(self):
        pass

    def _caclular_edad(self):
        fecha_actual = date.today()
        edad = fecha_actual - self._fecha_nacimiento
        return edad.days // 365
    
    def obtener_edad(self):
        return self._caclular_edad()



class Movimientos(CuentaBancaria):
    def __init__(self, nombre_titular, dni_titular, fecha_nacimiento, saldo=0, limite_extraccion = 10000):
        super().__init__(nombre_titular, dni_titular, fecha_nacimiento, saldo)
        self._limite_extraccion = limite_extraccion
    
    def depositar(self,monto):
        if monto > 0:
            self._saldo += monto
            print(f"Se ha depositado {monto} a la cuenta de {self._nombre_titular}, su saldo es de: {self.obtener_saldo()}")
        else:
            print("El monto a depositar debe ser mayor a 0")
    
    def extraer(self,monto):
        if monto <= self.obtener_saldo() and monto <= self._limite_extraccion:
            self._saldo -= monto
            print(f"Se ha extraido {monto} de la cuenta de {self._nombre_titular}, su saldo acutal es de: {self.obtener_saldo()}")
        else:
            if monto > self._limite_extraccion:
                print("Usted no puede extraer ese monto")
            else:
                print("No posee saldo suficiente para esta operación")


class CuentaAhorro(CuentaBancaria):
    def __init__(self, nombre_titular, dni_titular, fecha_nacimiento, saldo=0, tasa_interes=0.001):
        super().__init__(nombre_titular, dni_titular, fecha_nacimiento, saldo)
        self._tasa_interes = tasa_interes
    
    def depositar(self,monto):
        pass
    
    def extraer(self,monto):
        pass
    
    def calcular_interes(self,monto):
        if monto > 0:
            interes = (monto * self._tasa_interes) * 5
            self._saldo = monto + interes
            print(f'{self._nombre_titular}, la suma del total más los intereses serían: {self.obtener_saldo()}')
        else:
            print("El monto a depositar debe ser mayor a 0")


def operacion1():
    cuenta3 = Movimientos("Sebastian",48569541,date(1990,3,2),0)

    ingreso = int(input("Ingrese el monto a depositar: "))

    cuenta3.depositar(ingreso)

    ingreso = int(input("Ingrese el monto a depositar: "))

    cuenta3.depositar(ingreso)

    ingreso = int(input("Ingrese el monto a depositar: "))

    cuenta3.depositar(ingreso)


def operacion2():
    cuenta3 = Movimientos("Gabriel",41879236,date(1981,12,25),500000)
    
    ingreso = int(input("Ingrese el monto a extraer: "))

    cuenta3.extraer(ingreso)


def operacion3():
    cuenta4 = CuentaAhorro("Gabriel",37895651,date(1975,5,16),0,0.355)

    ingreso = int(input("Ingrese el monto para calcular el interés: "))

    cuenta4.calcular_interes(ingreso)


def operaciones():
    limpiar()
    recibir()
    print('''
    1 - Ejecutar operación 1
    2 - Ejecutar operación 2
    3 - Ejecutar operación 3
    4 - Salir
    ''')
    
    opcion = input('               Elija una opción: ')

    limpiar()

    if opcion == '1':
        limpiar()
        recibir()
        operacion1()
        continuar()
    elif opcion == '2':
        limpiar()
        recibir()
        operacion2()
        continuar()
    elif opcion == '3':
        limpiar()
        recibir()
        operacion3()
        continuar()
    elif opcion == '4':
        salir()
    else:
        recibir()
        print('''
              
              
              Opción seleccionada no válida.
              
              
        ''')
        seguir = input('          Desea continuar? (s/n): ').upper()

        limpiar()

        if seguir == 'S':
            recibir()
            operaciones()
        else:
            salir()

operaciones()



