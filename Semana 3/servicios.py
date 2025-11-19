
inventario = []

def agregar(nombre,precio,cantidad):
    inventario.append({"nombre": nombre,"precio":precio,"cantidad":cantidad})
    return inventario

def mostar(inventario):
    print(f"""Este es el inventario: \n
{inventario}""")
    return

def buscar(inventario,busqueda):
    for producto in inventario:
        if producto["nombre"] == busqueda:
            print(f"{busqueda} Si esta en el inventario\n")
            return True
        else:
            print(f"{busqueda} No esta en el inventario")
            return False

def actulizar(inventario,producto,nuevoPrecio,nuevoCantidad):
    for i in inventario:
        if i["nombre"] == producto:
            i["precio"] = nuevoPrecio
            i["cantidad"] = nuevoCantidad

nombre = input("Ingrese el nombre del producto: \n")
precio = float(input(f"Ingrese el precio del {nombre}: \n"))
cantidad = int(input(f"Ingresa la cantidad de {nombre} \n"))
agregar(nombre,precio,cantidad)

busqueda = input("Ingrese el dato que quiere buscsar: \n")
buscar(inventario,busqueda)

producto = input("Ingresa el producto que quieres cambiarle el precio y cantida:\n")
nuevoPrecio = float(input("Ingresa el nuevo precio: \n"))
nuevoCantidad = int(input("Ingresa la nueva cantida: \n"))
actulizar(inventario,producto,nuevoPrecio,nuevoCantidad)

mostar(inventario)