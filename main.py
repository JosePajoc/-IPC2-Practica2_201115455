from contacto import contacto
from agenda import agenda

miAgenda = agenda()
op = 0

def separador():
    print('---------------------------------------------------------------------------------------')

def nuevoContacto():
    try:
        nombre = input('\nNombre: ')
        apellido = input('\nApellido: ')
        telefono = int(input('\nTeléfono: '))
        temporal = miAgenda.buscarTelefono(telefono)
        if temporal == None:
            miAgenda.agregarContacto(contacto(nombre, apellido, telefono))
            print('\nContacto almacenado exitosamente')
        else:
            print('El número de teléfono ya se encuentra registrado...')
    except:
        print('\nTeléfono no valido...')

while op != 4:
    print('1. Ingresar nuevo contacto')
    print('2. Buscar contacto')
    print('3. Visualizar agenda')
    print('4. Salir')
    op = int(input('\nIngrese la opción que desea utilizar: '))
    if op == 1:
        separador()
        nuevoContacto()
        separador()
    elif op == 2:
        separador()
        try:
            telefonoBuscar = int(input('\nIngrese el número: '))
            temporal = miAgenda.buscarTelefono(telefonoBuscar)
            if  temporal == None:
                respuesta = input('\nNo existe el contacto ¿Desea agregarlo si/no? ')
                if respuesta.lower() == 'si':
                    nuevoContacto()
            else:
                print('\tNombre: ', temporal.nombre)    
                print('\tApellido: ', temporal.apellido)
                print('\tTeléfono: ', temporal.telefono)
        except:
                print('\nTeléfono no valido...')
        separador()
    elif op == 3:
        separador()
        miAgenda.verAgenda()
        separador()

    