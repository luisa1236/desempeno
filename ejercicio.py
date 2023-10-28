# Ejercio isando diccionarios y funciones en el que creemos un producto con las sigueintes claves

#id,nombre,costo, cantidad, margen de ganancia 

# se deben almacenar los productos con dos campos adicionales 
#formula calculados precio de venta = costo /(1-margen de ganancia) y valor de invertarios = cantidad * costo
#almacenar los productos creados en un diccionario de diccionario 

#la aplicacion debe permitir :
#1. iniciar un menu
#2. agregar producto
#3. escoger que quiere comprar 
#4. poder tener factura 
#5. con el total mas el iva del 7%




def calcular_precio_venta(costo, margen_ganancia):
    return costo / (1 - margen_ganancia)

def calcular_valor_inventario(cantidad, costo):
    return cantidad * costo


productos = {}


def agregar_producto():
    id_producto = input("Ingrese el ID del producto: ")
    nombre = input("Ingrese el nombre del producto: ")
    costo = float(input("Ingrese el costo del producto: "))
    cantidad = int(input("Ingrese la cantidad en inventario: "))
    margen_ganancia = float(input("Ingrese el margen de ganancia (en decimal): "))
    
    precio_venta = calcular_precio_venta(costo, margen_ganancia)
    valor_inventario = calcular_valor_inventario(cantidad, costo)
    
    productos[id_producto] = {
        'nombre': nombre,
        'costo': costo,
        'cantidad': cantidad,
        'margen_ganancia': margen_ganancia,
        'precio_venta': precio_venta,
        'valor_inventario': valor_inventario
    }


def realizar_compra():
    id_producto = input("Ingrese el ID del producto que desea comprar: ")
    if id_producto in productos:
        cantidad_comprada = int(input(f"Ingrese la cantidad de '{productos[id_producto]['nombre']}' que desea comprar: "))
        if cantidad_comprada <= productos[id_producto]['cantidad']:
            productos[id_producto]['cantidad'] -= cantidad_comprada
            print(f"Compra exitosa de {cantidad_comprada} unidades de '{productos[id_producto]['nombre']}'")
        else:
            print(f"No hay suficiente inventario de '{productos[id_producto]['nombre']}'")
    else:
        print("El producto no existe en el inventario.")

# Función para generar una factura con IVA
def generar_factura():
    total_sin_iva = 0
    for id_producto, producto in productos.items():
        total_sin_iva += producto['precio_venta'] * producto['cantidad']
    
    iva = total_sin_iva * 0.07
    total_con_iva = total_sin_iva + iva
    
    print("\nFactura:")
    for id_producto, producto in productos.items():
        print(f"{producto['nombre']} ({producto['cantidad']} unidades): ${producto['precio_venta'] * producto['cantidad']:.2f}")
    print(f"Total sin IVA: ${total_sin_iva:.2f}")
    print(f"IVA (7%): ${iva:.2f}")
    print(f"Total con IVA: ${total_con_iva:.2f}")


while True:
    print("\nMenú:")
    print("1. Agregar producto")
    print("2. Realizar compra")
    print("3. Generar factura")
    print("4. Salir")
    
    opcion = input("Seleccione una opción: ")
    
    if opcion == "1":
        agregar_producto()
    elif opcion == "2":
        realizar_compra()
    elif opcion == "3":
        generar_factura()
    elif opcion == "4":
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")

