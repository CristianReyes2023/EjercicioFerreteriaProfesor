import core
import os
diccProducto = {"data":[]}
"""
Metodo para cargar informacion de productos:
Si el archivo de recursos no existe lo crea de forma
automatica con la estructura inicia del diccionario vacio
diccCliente = {"data":[]}
"""
def LoadInfoProductos():
    global diccProducto
    if (core.checkFile("productos.json")):
        diccProducto = core.LoadInfo("productos.json")
    else:
        core.crearInfo("productos.json",diccProducto)

def MainMenu():
    os.system("clear")
    isCliRun = True
    os.system("clear")
    print('+','-'*55,'+')
    print("|{:^14}{}{:^14}|".format(' ','ADMINISTRACION DE PRODUCTOS',' '))
    print('+','-'*55,'+')
    print("1. Registrar")
    print("2. Buscar")
    print("3. Editar")
    print("4. Eliminar")
    print("5. Activar o Inactivar producto")
    print("6. Regresar menu principal")
    opcion =int(input(":)_"))
    if (opcion == 1):
        data ={
            "id":input("Ingrese el Id del producto :"),
            "nombre":input("Ingrese el Nombre del producto :"),
            "cantidad":0,
            'stockMinimo':float(input("Ingresa la cantidad minima: ")),
            'stockMaximo':float(input("Ingresa la cantidad minima: ")),
            "valorCompra":float(input("Ingrese el valor de compra: ")),
            "valorVenta":float(input("Ingrese el valor de venta: ")),
            'estado':True
        }
        diccProducto["data"].append(data)
        core.crearInfo("productos.json",data)        
    elif (opcion == 2):
        id=input("Ingrese el Id del producto: ")
        for i,item in enumerate(diccProducto['data']):
            if id in item["id"]:
                os.system("clear")
                print(f"Numero Id del producto es: {item['id']}")
                print(f"Nombre del producto es: {item['nombre']}")
                print(f"StockMin producto es: {item['stockMinimo']}")
                print(f"StockMax del producto es: {item['stockMaximo']}")
                os.system("sleep 10")
    elif (opcion == 3):
        id = input("Ingrese el Id del producto: ")
        for i,item in enumerate(diccProducto['data']):
            if id in item["id"]:
                item["nombre"] = input("Ingresa nuevo nombre o enter para continuar " or item["nombre"])
                item["stockMinimo"] = float(input("Ingresa nuevo nombre o enter para continuar ")) or item["stockMinimo"]
                item["stockMaximo"] = float(input("Ingresa nuevo nombre o enter para continuar ")) or item["stockMaximo"]
                item["valorCompra"]:float(input("Ingrese nuevo valor compra o enter para continuar ")) or item['valorVenta']
                item["valorVenta"]:float(input("Ingrese nuevo valor venta o enter para continuar")) or item["valorVenta"]
                core.EditarData("productos.json",diccProducto)
    elif (opcion == 4):
        id = input("Ingresa el Id del producto: ")
        for i,item in enumerate(diccProducto["data"]):
            if id in item["id"]:
                diccProducto["data"].pop(i)
                core.EditarData("productos.json",diccProducto)
    elif (opcion == 5):
        id = input("Ingrese el Id del producto: ")
        for i,item in enumerate(diccProducto["data"]):
            if id in item["id"]:
                print("1.Activar\n2.Inactivar")
                diccProducto["data"][i]["estado"] = True if int(input(":")) == 1 else False 
                core.EditarData("productos.json",diccProducto)
                # os.system("pause")
                # core.crearInfo("productos.json",itemDel)
    elif (opcion == 6):
        isCliRun = False
    if (isCliRun):
        MainMenu()
