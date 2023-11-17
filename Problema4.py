class Triangulo:
    def inicializar(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
    
    def lado_mayor(self):
        if self.lado1 == self.lado2 and self.lado2 == self.lado3:
            print("Todos los lados equivalen a:",self.lado1)
        elif self.lado1 > self.lado2 and self.lado1 > self.lado3:
            print("El lado 1 es el mayor.")
        elif self.lado2 > self.lado1 and self.lado2 > self.lado3:
            print("El lado 2 es el mayor.")
        else: 
            print("El lado 3 es el mayor.")
def equilatero(self):
    if self.lado1 == self.lado2 and self.lado2 == self.lado3:
        print("El triangulo es equilatero.")
    else: 
        print("No es equilatero")

#bloque principal
triangulo1 = Triangulo()
triangulo1.inicializar(4,5,6)
triangulo1.lado_mayor()
triangulo1.equilatero()
print("")

triangulo2 = Triangulo()
triangulo2.inicializar(4,4,4)
triangulo2.lado_mayor()
triangulo2.equilatero()

