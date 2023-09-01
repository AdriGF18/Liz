vini = "bienvenido"
vini = vini.upper()
vfin = "*"
print(vini.center(79,"*"))
print()
print("A continuacion te presentamos las materias que puedes cursar de forma optativa: ")
print("1. Administracion de procesos")
print("2. Aplicacion de TI")
print("3. RH")
print("4. Administracion financiera ")
print("5. Mercadotecnia /n")
print(vfin.center(79,"*"))

1materias = ("Administracion de procesos", "Aplicacion de TI", "RH", "Administracion financiera", "Mercadotecnia")
1lista = (1,2,3,4,5)

voptativa = int(input("¿Cual numero de materia eliges?: "))

if voptativa in 1lista:
    print("Eliges la materia %$" >% (1materias(voptativa - 1))
          
