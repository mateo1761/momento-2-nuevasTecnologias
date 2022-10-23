num1 = int(input('Ingrese el primer numero: '))
num2 = int(input('Ingrese el segundo numero: '))


def numeros(num1, num2): return 1 if num1 > num2 else -1


def numeroMayor(): return print(f'El primer número {num1} es mayor que el segundo ') if numeros(
    num1, num2) == 1 else print(f'El segundo número {num2} es mayor que el primero')


numeroMayor()
