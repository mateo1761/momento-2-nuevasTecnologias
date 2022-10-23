print('1. Agregar ciclista')
print('2. Ver resultados')
print('0. salir')

opcion = 100

ciclistas = []

while (opcion != 0):

    datos = {}

    menu = int(input('Digite una opcion: '))

    if (menu == 1):
        datos['nombre'] = input('Digite el nombre: ')
        datos['edad'] = int(input('Digite la edad: '))
        datos['pais'] = input('Digite el pais: ')
        datos['equipo'] = input('Digite el equipo: ')
        datos['tiempo'] = int(input('Digite el tiempo (en minutos): '))
        ciclistas.append(datos)
        print(ciclistas)

    elif (menu == 2):

        tiempo = 100
        for ciclista in ciclistas:
            if ciclista['tiempo'] < tiempo and ciclista['nombre']:
                tiempo = ciclista['tiempo']
        print(
            f"El ciclista con mejor tiempo es {ciclista['nombre']} con el tiempo: {tiempo} min")

    elif (menu == 0):
        opcion = 0
        print("Saliste del programa")
