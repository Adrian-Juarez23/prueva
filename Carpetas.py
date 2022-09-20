from distutils.command.sdist import sdist
import os
os.mkdir('D:\{}'.format("Adios mundo"))
materiasUnidades = {}

def guardarNombres (nombreCarpetas, unidades):
    materiasUnidades[nombreCarpetas] = unidades

def crearCarpetas():
    for nombreMateria in materiasUnidades:
        os.mkdir('D:{}'.format(nombreMateria))
        for unidad in range(1, int(materiasUnidades.get(nombreMateria))+1):
            os.mkdir('D:\\{}\\Unidad {}'.format(nombreMateria, unidad))
            os.mkdir('D:\\{}\\Unidad {}\\Saber'.format(nombreMateria, unidad))
            os.mkdir('D:\\{}\\Unidad {}\\Saber Hacer'.format(nombreMateria, unidad))

while True:
    # print(materiasUnidades)
    nombre = input('Ingresa el nombre de la carpeta: ')
        
    while True:
        try:
            unidades = int(input('Ingresa el numero de unidades o ingresa 0 para terminar: '))
            break
        
        except ValueError:
            print('Introduce un valor entero.')
                
    try:    
        if nombre == '' and unidades == 0 or nombre != '' and unidades == 0:
            break
        elif nombre == '' and unidades > 0:
            pass  
        else:
            guardarNombres(nombre, unidades)
    except (NameError, FileNotFoundError) as error:
        print(error)

if materiasUnidades != {}:
    crearCarpetas()
