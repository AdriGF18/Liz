class Alumno:
    def inicializar(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def mostrar(self):
        print("Nombre:",self.nombre)
        print("Nota:",self.nota)

    def mayor(self):
        if self.nota>=4:
            print("Eegular")
        else:
            print("No regular")

#bloque principal
alumno1 = Alumno()
alumno1.inicializar("Adriana",5)
alumno1.mostrar()
alumno1.mayor()
print("")
alumno2 = Alumno()
alumno2.inicializar("Lizeth", 9)
alumno2.mostrar()
alumno2.mayor()