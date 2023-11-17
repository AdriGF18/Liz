class Persona:
    def inicializar(self, nombre):
        self.nombre = nombre

    def mostrar(self):
        print("Nombre:", self.nombre)

#bloque principal
persona1 = Persona()
persona1.inicializar("Adriana")
persona1.mostrar()

persona2 = Persona()
persona2.inicializar("Lizeth")
persona2.mostrar()