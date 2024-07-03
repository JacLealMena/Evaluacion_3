import os, csv, msvcrt

#Utilidad
def limpiar():
    os.system("cls")
def esperar_tecla():
    print("\n\t>>> Presione una tecla para continuar <<<")
    msvcrt.getch()

#Menú


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
            opc = int(input("Opción: "))
            if opc in (1,2,3,4,5):
                break
            else:
                print("\t>>> Opción Inválida! Ingrese un número de la lista! <<<")
        except:
            print("\t>>> ERROR! Debe ingresar un número entero! <<<")
    return opc
