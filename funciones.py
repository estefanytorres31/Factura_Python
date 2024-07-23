# funciones_factura.py y generar_factura.py

# Función para calcular el subtotal
def calcular_subtotal(productos):
    subtotal = sum(producto["precio"] * producto["cantidad"] for producto in productos)
    return subtotal

# Función para calcular el IGV (Impuesto General a las Ventas)
def calcular_igv(subtotal):
    porcentaje_igv = 0.18  # 18% de IGV
    igv = subtotal * porcentaje_igv
    return igv

# Función para calcular el total (subtotal + IGV)
def calcular_total(subtotal, igv):
    total = subtotal + igv
    return total
