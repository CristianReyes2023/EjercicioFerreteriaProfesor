import clientes
import compras
import ventas
import productos
import proveedores
import os
if __name__ == "__main__":
    isActivate = True
    while isActivate:
        os.system("clear")
        print('+','-'*55,'+')
        print("|{:^20}{}{:^24}|".format(' ','MENU PRINCIPAL',' '))
        print('+','-'*55,'+')
        print("1. Gestion de clientes")
        print("2. Gestion de producto")
        print("3. Gestion de Proveedores")
        print("4. Gestion de Compras")
        print("5. Gestion de ventas")
        print("6. Terminar")
        opcion = int(input(":)_"))
        if (opcion == 1):
            clientes.LoadInfoCliente()
            clientes.MainMenu()
        elif (opcion == 2):
            productos.LoadInfoProductos()
            productos.MainMenu()
        elif (opcion == 3):
            proveedores.LoadInfoProveedore()
            proveedores.MainMenu()
        elif (opcion == 4):
            compras.MainMenu()
        elif (opcion == 5):
            ventas.MainMenu()
        elif (opcion == 6):
            isActivate = False
        else:
            print("Opcion no valida....")
            os.system("pause")