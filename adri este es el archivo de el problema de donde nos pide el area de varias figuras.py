def vcalcular_area_cuadrado():
    lado=float(input("ingresa la longitud del lado del cuadrado:"))
    areac= lado **2
    print("el area es:", areac)

def vcalcular_area_triangulo():
    base=float(input("ingresa la longitud de la base del triangulo:"))
    altura=float(input("ingresa la altura del triangulo:"))
    areat=(base*altura)/2
    print("el area del triangulo es:", areat)
    
def vcalcular_area_rectangulo():
    base=float(input("ingresa la longitud de la base del rectangulo:"))
    altura=float(input("ingrese la altura del rectangulo:"))
    arear=(base * altura)
    print("el area rectangulo es:" , arear)
    
def vcalcular_area_circulo():
    pi=3.1416
    diametro=float(input("ingrese el valor del diametro"))
    areaculo=(pi * diametro)
    print("el area del circulo es:", areaculo)
    
    
while True:
  print("selecciona una opcion:")
  print("1. calcular area cuadrado")
  print("2. calcular area triangulo")
  print("3. calcular area rectangulo")
  print("4. calcular area circulo")
  print("5. salir")
  opcion=input("que quieres realizar:?")

  if opcion == "1":

    vcalcular_area_cuadrado()


  elif opcion == "2":
     
     vcalcular_area_triangulo()
    
    
  elif opcion == "3":
      
       vcalcular_area_rectangulo()
       
  elif opcion == "4":
      
        vcalcular_area_circulo()
     
  elif opcion == "5":
       print("adios")
       break
       
  else:
     print("opcion invalida")