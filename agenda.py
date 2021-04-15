from contacto import contacto
from io import open                          #Importando módulo para crear archivo plano
from graphviz import render                  #Importando módulo para renderizar desde python, agregar con pip graphviz
import webbrowser                            #Módulo para abrir automaticamente el navegador

class agenda():
    def __init__(self):
        self.inicio = None
        self.fin = None
    
    def verVacio(self):                                             #Verificar que existan datos en la lista
        return self.inicio == None
    
    def agregarContacto(self, nuevoContacto):                       #Método para ordenar según el número de teléfono
        if self.verVacio():
            self.inicio = nuevoContacto
            self.fin = nuevoContacto
        elif nuevoContacto.telefono < self.inicio.telefono:
            self.insertarInicio(nuevoContacto)
        elif nuevoContacto.telefono > self.fin.telefono:
            self.insertarFinal(nuevoContacto)
        else:
            self.insertarMedio(nuevoContacto)

    def insertarInicio(self, nuevoContacto):
        self.inicio.anterior = nuevoContacto
        nuevoContacto.siguiente = self.inicio
        self.inicio = nuevoContacto
    
    def insertarFinal(self, contacto):
        self.fin.siguiente = contacto
        contacto.anterior = self.fin
        self.fin = contacto
    
    def insertarMedio(self, nuevoContacto):
        temporal1 = self.inicio
        while temporal1.telefono < nuevoContacto.telefono:
            temporal1 = temporal1.siguiente
        temporal2 = temporal1.anterior
        temporal2.siguiente = nuevoContacto
        temporal1.anterior = nuevoContacto
        nuevoContacto.anterior = temporal2
        nuevoContacto.siguiente = temporal1
    
    def verAgenda(self):                                            #Ver agenda por consola
        temporal = self.inicio
        if temporal == None:
            print('No hay contactos registrados')
        while temporal != None:
            print('Nombre: ', temporal.nombre, ' Apellido: ', temporal.apellido, ' Teléfono', temporal.telefono)
            temporal = temporal.siguiente

    def buscarTelefono(self, buscTelefono):                         #Buscar contacto por numéro de teléfono
        temporal = self.inicio
        while temporal != None:
            if temporal.telefono == buscTelefono:
                return temporal
            else:
                temporal = temporal.siguiente
        return None
    
    def verCantidad(self):                                            #Ver agenda por consola
        temporal = self.inicio
        cantidad = 0
        while temporal != None:
            cantidad = cantidad + 1
            temporal = temporal.siguiente
        return cantidad

    def crearImagen(self):
        nombreImagen = 'miAgenda.dot'
        salidaImagen = open(nombreImagen, 'w')
        salidaImagen.write('digraph G { \n')
        salidaImagen.write('node [shape=plaintext] \n')
        salidaImagen.write('a [label=<<table border="0" cellborder="1" cellspacing="0"> \n')
        cantidad = self.verCantidad()
        salidaImagen.write('<tr><td colspan="3"> Contactos de mi agenda </td></tr>\n')
        salidaImagen.write('<tr> \n')
        salidaImagen.write('\t <td> Nombre </td>')
        salidaImagen.write('<td> Apellido </td>')
        salidaImagen.write('<td> Telefono </td>')
        salidaImagen.write('</tr> \n')
        temporal = self.inicio
        while temporal != None:
            salidaImagen.write('<tr> \n')
            salidaImagen.write('\t <td>' + temporal.nombre + '</td> <td>' + temporal.apellido + '</td> <td>' + str(temporal.telefono) + '</td>')
            salidaImagen.write('</tr> \n')
            temporal = temporal.siguiente

        salidaImagen.write('</table>>]; \n')
        salidaImagen.write('}')
        salidaImagen.close()
        render('dot', 'png', nombreImagen)                                #Renderizar el archivo DOT escrito

        webbrowser.open_new_tab("miAgenda.dot.png")                       #Abrir navegador para visualizar agenda

