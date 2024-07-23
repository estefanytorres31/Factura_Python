from flask import Flask, render_template, request
import funciones as f
from datetime import datetime  # Importa el módulo datetime

app = Flask(__name__)

codigo_contador = 1

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generar_factura', methods=['POST'])
def generar_factura():
    # Obtener la fecha actual del sistema
    fecha_actual = datetime.now().strftime('%d/%m/%Y %H:%M:%S')  # Formato de fecha

    #Obtener el codigo de factura
    global codigo_contador
    
    # Obtener los datos del formulario HTML
    nombre_cliente = request.form['nombre_cliente']
    dni = request.form['dni']
    telefono_cliente = request.form['telefono_cliente']

    # Obtener los datos de los productos del formulario HTML
    productos = []
    for i in range(1, 11):
        nombre_producto = request.form.get(f"nombre_producto_{i}")
        precio_producto = request.form.get(f"precio_producto_{i}")
        cantidad_producto = request.form.get(f"cantidad_producto_{i}")

        if not nombre_producto or not precio_producto or not cantidad_producto:
            break

        producto = {
            "nombre": nombre_producto,
            "precio": float(precio_producto),
            "cantidad": int(cantidad_producto)
        }
        productos.append(producto)
    print("")
    codigo = codigo_contador
    codigo_contador += 1
    subtotal = f.calcular_subtotal(productos)
    igv = f.calcular_igv(subtotal)
    total = f.calcular_total(subtotal, igv)
    print("\n=============================================")
    print("              FACTURA DE VENTA                ")
    print("=============================================")
    print(f"Número de factura: {codigo}")
    print(f"Fecha: {fecha_actual}")
    print("=============================================")
    print("Datos del cliente.")
    print(f"Nombre: {nombre_cliente}")
    print(f"D.N.I: {dni}")
    print(f"Teléfono: {telefono_cliente}")
    print("=============================================")
    print("Productos.")
    print("{:<20} {:<10} {:<10}".format("Nombre", "Cantidad", "Precio"))
    for producto in productos:
         print("{:<20} {:<10} S/. {:<10.2f}".format(producto["nombre"], producto["cantidad"], producto["precio"]))
    print("=============================================")
    print("Subtotal:          S/. {:.2f}".format(subtotal))
    print("IGV (18%):         S/. {:.2f}".format(igv))
    print("Total a pagar:     S/. {:.2f}".format(total))
    print("=============================================")

    return render_template('factura.html', codigo=codigo, fecha=fecha_actual,
                           cliente={"nombre": nombre_cliente, "dni": dni, "telefono": telefono_cliente},
                           productos=productos, subtotal=subtotal, igv=igv, total=total)

if __name__ == '__main__':
    app.run(debug=True)
