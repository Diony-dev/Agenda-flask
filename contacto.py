class Contacto:
    def __init__(self, nombre, telefono, email):
        self.nombre = nombre
        self.telefono = telefono
        self.email = email

    def __str__(self):
        return f"Nombre: {self.nombre}, Teléfono: {self.telefono}, Email: {self.email}"
    


class Agenda:
    def __init__(self):
        self.contactos = []

    def agregar_contacto(self, contacto):
        self.contactos.append(contacto)

    def mostrar_contactos(self):
        for contacto in self.contactos:
            print(contacto)

    def eliminar_contacto(self, nombre):
        for contacto in self.contactos:
            if contacto.nombre == nombre:
                self.contactos.remove(contacto)
                return True
        return False

    def buscar_contacto(self, nombre):
        for contacto in self.contactos:
            if contacto.nombre == nombre:
                return contacto
        return None