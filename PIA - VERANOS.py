VALOR_UMA = 103.74
LIMITE_DE_PAGO_EN_EFECTIVO_ANTES_DE_IVA = 3210 * VALOR_UMA
LIMITE_DE_PAGO_TOTAL_EN_EFECTIVO_ANTES_DE_IVA = 6420 * VALOR_UMA

def selecciona_opcion(mensaje):
    while True:
        try:
            vvalor = int(input(mensaje))
            return vvalor
        except ValueError:
            print("Error: Ingresa un valor entero válido.")

def obtener_input_float(mensaje):
    while True:
        try:
            vvalor = float(input(mensaje))
            return vvalor
        except ValueError:
            print("Error: Ingresa un valor numérico válido.")
            
            
            
            
print("︻┳═一⊗  ︻┳═一⊗  ︻┳═一⊗ ︻┳═一⊗  BIENVENIDO  ︻┳═一⊗  ︻┳═一 ⊗  ︻┳═一 ⊗ ︻┳═一⊗")            

def obtener_rfc():
    while True:
        vrfc = input("Ingresa el RFC del cliente: ")
        vrfc = vrfc.strip()
        if len(vrfc) not in [12, 13] or vrfc == "XAXX010101000":
            print("Error: El RFC no es válido.")
        else:
            return vrfc

def obtener_nombre():
    while True:
        vnombre = input("Ingresa el nombre del cliente: ")
        if vnombre.strip() == "":
            print("Error: El nombre no puede estar en blanco.")
        else:
            return vnombre

def obtener_marca():
    while True:
        vmarca = input("Ingresa la marca del automóvil: ")
        if vmarca.strip() == "":
            print("Error: La marca no puede estar en blanco.")
        else:
            return vmarca

def obtener_linea():
    while True:
        vlinea = input("Ingresa la línea del automóvil: ")
        if vlinea.strip() == "":
            print("Error: La línea no puede estar en blanco.")
        else:
            return vlinea

def obtener_precio_venta():
    while True:
        try:
            vprecio = obtener_input_float("Ingresa el precio de venta del automóvil: ")
            if vprecio <= 0:
                print("Error: El precio debe ser mayor a cero.")
            else:
                return vprecio
        except (TypeError, ZeroDivisionError):
            print("Error: Carácter inválido. Ingresa un número válido.")

def obtener_clave_pago():
    while True:
        try:
            clave = "Clave de Pago"
            print(clave.center(50, "$"))
            print("|-------------------------------------------------|")
            print("1.Efectivo")
            print("|-------------------------------------------------|")
            print("2. Cheque")
            print("|-------------------------------------------------|")
            print("3. Tarjeta de Crédito")
            print("|-------------------------------------------------|")
            print("4. Tarjeta de Débito")
            print("|-------------------------------------------------|")
            print("5. Transferencia bancaria")
            print("|-------------------------------------------------|")
            print("6. Depósito bancario")
            print("|-------------------------------------------------|")
            print("7. Depósito en efectivo")
            print("|-------------------------------------------------|")
            print("8. Condonación")
            print("|-------------------------------------------------|")
            
            vclave = selecciona_opcion("Selecciona la clave de pago: ")
            if vclave in range(1, 9):
                return vclave
            else:
                print("Error: Selecciona una clave válida.")
        except (TypeError, ZeroDivisionError):
            print("Error: Carácter inválido. Ingresa un número válido.")

def obtener_monto_pago(max_monto, num_pago_str):
    while True:
        try:
            vmonto = obtener_input_float(f"Ingresa el monto del {num_pago_str} pago: ")
            if vmonto <= 0:
                print("Error: El monto del pago debe ser mayor a cero.")
            elif vmonto > max_monto:
                print(f"Error: El monto del pago no puede ser mayor a {max_monto}.")
            else:
                return vmonto
        except (TypeError, ZeroDivisionError):
            print("Error: Carácter inválido. Ingresa un número válido.")

def evaluar_aviso(monto_efectivo_unidad, monto_total_unidad):
    vmotivo = None
    if monto_efectivo_unidad > LIMITE_DE_PAGO_EN_EFECTIVO_ANTES_DE_IVA:
        vmotivo = "Monto en efectivo"
    elif monto_total_unidad > LIMITE_DE_PAGO_TOTAL_EN_EFECTIVO_ANTES_DE_IVA or LIMITE_DE_PAGO_EN_EFECTIVO_ANTES_DE_IVA :
        vmotivo = "Monto total"

    return vmotivo

# Resto del código...

def obtener_monto_efectivo(vclave, precio_venta, monto_efectivo_unidad, monto_total_unidad):
    if vclave == 1 or vclave == 7:
        return precio_venta - monto_efectivo_unidad
    elif vclave in (2, 3, 4, 5, 6, 8):
        return precio_venta - monto_total_unidad
    else:
        return precio_venta

# Ciclo principal del programa
while True:
    vrfc = obtener_rfc()
    vnombre = obtener_nombre()
    vmarca = obtener_marca()
    vlinea = obtener_linea()
    precio_venta = obtener_precio_venta()

    monto_efectivo_unidad = 0.0
    monto_total_unidad = 0.0

    cantidad_pagos = 0
    monto_total_pagos = 0.0

    while monto_total_pagos < precio_venta:
        vclave = obtener_clave_pago()
        max_monto = obtener_monto_efectivo(vclave, precio_venta, monto_efectivo_unidad, monto_total_unidad)

        num_pago_str = "1er" if cantidad_pagos == 0 else f"{cantidad_pagos + 1}°"
        vmonto = obtener_monto_pago(max_monto, num_pago_str)
        cantidad_pagos += 1

        try:
            if vclave == 1 or vclave == 7:
                monto_efectivo_unidad += vmonto
            else:
                monto_total_unidad += vmonto

            monto_total_pagos += vmonto

        except ZeroDivisionError:
            print("|-------------------------------------------------------------|")
            print("Error: No se puede dividir entre cero. Ingresa un monto válido.")
            print("|-------------------------------------------------------------|")
            break

    if monto_total_pagos != precio_venta:
        print("|----------------------------------------------------------------------------------------------------|")
        print(f"Error: La suma de los pagos ({monto_total_pagos}) no coincide con el precio de venta ({precio_venta}).")
        print("|----------------------------------------------------------------------------------------------------|")
        continue

    vaviso = evaluar_aviso(monto_efectivo_unidad / 1.16, monto_total_unidad / 1.16)

    # Mostrar información
    print("|-------------------------------------------------------------|")
    print("   OBTENIENDO INFORMACION   ")
    print("|-------------------------------------------------------------|")
    print("RFC:", vrfc.strip().upper()),
    print("|-------------------------------------------------------------|")
    print("Nombre:", vnombre.title().strip()),
    print("|-------------------------------------------------------------|")
    print("Marca:", vmarca.strip().upper()),
    print("|-------------------------------------------------------------|")
    print("Línea:", vlinea.strip().upper()),
    print("|-------------------------------------------------------------|")
    print("Precio de la unidad:", format(precio_venta, ".2f"))
    print("|-------------------------------------------------------------|")
    print("Límite de pagos en efectivo:", format(LIMITE_DE_PAGO_EN_EFECTIVO_ANTES_DE_IVA, ".2f"))
    print("|-------------------------------------------------------------|")
    print("Monto de pagos en efectivo de la unidad:", format(monto_efectivo_unidad, ".2f"))
    print("|-------------------------------------------------------------|")
    print("Monto de pagos en efectivo de la unidad antes de IVA:", format(monto_efectivo_unidad / 1.16, ".2f"))
    print("|-------------------------------------------------------------|")
    print("Límite de pagos totales:", format(LIMITE_DE_PAGO_TOTAL_EN_EFECTIVO_ANTES_DE_IVA, ".2f"))
    print("|-------------------------------------------------------------|")
    print("Monto de pagos totales de la unidad:", format(monto_total_unidad, ".2f"))
    print("|-------------------------------------------------------------|")
    print("Monto de pagos totales de la unidad antes de IVA:", format(monto_total_unidad / 1.16, ".2f"))
    

    if vaviso:
        print("|-------------------------------------------------------------|")
        print("La unidad es objetivo de aviso por:", vaviso)
        print("|-------------------------------------------------------------|")
    else:
        print("|-------------------------------------------------------------|")
        print("La unidad no es objetivo de aviso.")
        print("|-------------------------------------------------------------|")

    vopcion = input("¿Deseas evaluar otra operación? (s/n): ")
    if vopcion.lower().strip() != "s":
        print("|-------------------------------------------------------------|")
        print("¡Hasta luego!")
        print("|-------------------------------------------------------------|")
        break