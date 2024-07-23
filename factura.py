# generar_factura.py
import funciones as f

# Datos de la factura (se ingresan al principio)
numero_factura = input("Ingrese el número de factura: ")
fecha = input("Ingrese la fecha (DD/MM/AAAA): ")
cliente = {
    "nombre": input("Ingrese el nombre del cliente: "),
    "direccion": input("Ingrese la dirección del cliente: "),
    "telefono": input("Ingrese el teléfono del cliente: ")
}
productos = []

# Ingresar hasta 10 productos
for i in range(1, 11):
    opcion = input(f"¿Desea ingresar un producto? (Sí/No): ").lower()
    if opcion != 'sí' and opcion != 'si':
        break
    nombre_producto = input(f"Ingrese el nombre del producto {i}: ")
    precio_producto = float(input(f"Ingrese el precio del producto {i}: "))
    cantidad_producto = int(input(f"Ingrese la cantidad del producto {i}: "))
    productos.append({"nombre": nombre_producto, "precio": precio_producto, "cantidad": cantidad_producto})

subtotal = f.calcular_subtotal(productos)
igv = f.calcular_igv(subtotal)
total = f.calcular_total(subtotal, igv)

# Imprimir la factura si se ingresaron productos
if productos:
    print("\n=== FACTURA ===")
    print(f"Número de factura: {numero_factura}")
    print(f"Fecha: {fecha}")
    print("\nDatos del cliente:")
    print(f"Nombre: {cliente['nombre']}")
    print(f"Dirección: {cliente['direccion']}")
    print(f"Teléfono: {cliente['telefono']}")
    print("\nProductos:")
    print("{:<20} {:<10} {:<10}".format("Nombre", "Cantidad", "Precio"))
    for producto in productos:
        print("{:<20} {:<10} {:<10}".format(producto["nombre"], producto["cantidad"], producto["precio"]))
    print("\nSubtotal: S/.{:.2f}".format(subtotal))
    print("IGV (18%): S/.{:.2f}".format(igv))
    print("Total a pagar: S/.{:.2f}".format(total))
else:
    print("No se han ingresado productos. Factura cancelada.")
