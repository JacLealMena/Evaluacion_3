import os, csv, msvcrt

#Valores

cil_5 = 12500
cil_15 = 25500


#Listas



#Utilidad
def limpiar():
    os.system("cls")
def esperar_tecla():
    print("\n\t>>> Presione una tecla para continuar <<<")
    msvcrt.getch()


#Menú
def menu_comuna():
    limpiar()
    print("""
_COMUNAS DISPONIBLES_
1. Santiago
2. Colina
3. Puente ALto
4. Pirque
5. La Florida
""")
    while True:
        try:
            opc = int(input("\n> Opción: "))
            if opc not in (1,2,3,4,5):
                print("\t>>> Opción Inválida! Ingrese un número de la lista! <<<")
            else:
                break            
        except:
            print("\t>>> ERROR! Debe ingresar un número entero! <<<")
    if opc == 1:
        comuna_elegida = "Santiago"
    elif opc == 2:
        comuna_elegida = "Colina"
    elif opc == 3:
        comuna_elegida = "Puente Alto"
    elif opc == 4:
        comuna_elegida = "Pirque"
    else:
        comuna_elegida = "La Florida"
def menu():
    limpiar()
    print("""
Menú
1. Registrar Pedido
2. Listar Pedidos
3. Buscar Pedido por RUT
4. Imprimir Hoja de Ruta
5. Salir del Programa
""")
    while True:
        try:
            opc = int(input("\n> Opción: "))
            if opc not in (1,2,3,4,5):
                print("\t>>> Opción Inválida! Ingrese un número de la lista! <<<")            
        except:
            print("\t>>> ERROR! Debe ingresar un número entero! <<<")
        return opc
#Opción 1
def registrar_pedido():
    limpiar()
    print("_REGISTRANDO PEDIDO_\n")

    rut = RUT()
    nombre = val_nombre()
    direccion = val_direccion()
    comuna = menu_comuna()
    detalle = detalle_compra()


#Opción 2
def listar_pedidos():
    pass

#Opción 3
def buscar_pedido():
    pass

#Opción 4
def imprimir_hoja():
    pass

#Validaciones
def opcion():
    while True:
        try:
            opc = int(input("\n> Opción: "))
            if opc not in (1,2,3,4,5):
                print("\t>>> Opción Inválida! Ingrese un número de la lista! <<<")            
        except:
            print("\t>>> ERROR! Debe ingresar un número entero! <<<")
        return opc

def RUT():
    while True:
        rut = input("> Ingrese su RUT (Ej: 12543678-1): ")
        if len(rut) == 10:
            break
        else:
            print(">>> Rut inválido! El ingreso del rut es sin puntos y con guión (Ej: 12543678-1) <<<")
def val_nombre():
    while True:
        nombre = input("> Ingrese su nombre (sin apellido): ")
        if len(nombre) <= 2:
            print(">>> Nombre inválido! Debe contener al menos 3 carácteres <<<")
        else:
            break
    return nombre
def val_direccion():
    direccion = input("> Ingrese su dirección: ")
    while True:
        if len(direccion) == 0:
            print(">>> Dirección inválida! No puede ser un espacio en blanco! <<<")
        else:
            break
    return direccion


#Detalle de Opción 1
def detalle_compra():
    while True:
        print("""\n_CILINDROS_
1. Cilindro de 5kg -> $12500
2. Cilindro de 15kg -> $25500""")
        while True:
            try:
                opc = int(input("\n> Opción: "))
                if opc in (1,2):
                    break
                else:
                    print("\t>>> Opción Inválida! Ingrese un número de la lista! <<<")
            except:
                print("\t>>> ERROR! Debe ingresar un número entero! <<<")
        if opc == 1:
            print("_¿Cuántas unidades desea?_\n")
            while True:
                try:
                    cant_cil_5 = int(input("> R: "))
                    if cant_cil_5 < 0:
                        print(">>> Número inválido! Debe ingresar un número mayor o igual a 0! <<<")
                    else:
                        break
                except:
                    print(">>> ERROR! Debe ingresar un número!")
            total_cil_5 = 0
            total_cil_5 = total_cil_5 + cant_cil_5
        else:
            print(">> ¿Cuántas unidades desea?\n")
            while True:
                try:
                    cant_cil_15 = int(input("> R: "))
                    if cant_cil_15 < 0:
                        print(">>> Número inválido! Debe ingresar un número mayor o igual a 0! <<<")
                    else:
                        break
                except:
                    print(">>> ERROR! Debe ingresar un número!")
            total_cil_15 = 0
            total_cil_15 = total_cil_15 + cant_cil_15
            #cantidad de cilindros guardados
        s_n = input("¿Desea agregar otro(s) cilindro(s)? [Si / No]\n")
        if s_n.lower in("si","sí"):
            continue
        elif s_n.lower == "no":
            TotalPrecio_cil5 = total_cil_5*cil_5
            TotalPrecio_cil15 = total_cil_15*cil_15
            Precio_total = TotalPrecio_cil5 + TotalPrecio_cil15
            print(">> Datos ingresados correctamente <<")
            break
        else:
            print(">>> Ingreso inválido! Debe ingresar [Si] o [No]! <<<")