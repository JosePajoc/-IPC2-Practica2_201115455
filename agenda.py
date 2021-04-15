from contacto import contacto

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
        
