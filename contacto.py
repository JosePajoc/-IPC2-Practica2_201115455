#Nodo para cada contacto y sus respectivos apuntadores
class contacto():
    def __init__(self, nombre, apellido, telefono):
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.anterior = None
        self.siguiente = None