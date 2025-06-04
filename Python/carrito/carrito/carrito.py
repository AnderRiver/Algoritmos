a = 1
def mostrar_menu():
    print("\n---Bienvenido al carrito de compras---")
    print("1. Agregar producto al carrito")
    print("2. Ver carrito")
    print("3. Eliminar producto del carrito")
    print("4. Calcular total del carrito")
    print("5. Salir")

def agregar_producto(carrito):
    nombre = input("Ingrese el nombre del producto: ")
    try:
        precio = float(input("Ingrese el precio del producto: "))
        carrito.append({"nombre": nombre, "precio": precio})
        print(f"'Producto {nombre}' agregado al carrito.")
    except ValueError:
        print("El precio no puede ser negativo. Intente nuevamente.")
            
def ver_carrito(carrito):
    if not carrito:
        print("El carrito esta vacio.")
    else:
        print("Productos en el carrito:")
        for i, producto in enumerate(carrito, start=1):
            print(f"{i}. {producto['nombre']} - ${producto['precio']:.2f}")

def eliminar_producto(carrito):
    ver_carrito(carrito)
    if carrito:
        try:
            indice = int(input("Ingrese el numero del producto a eliminar: ")) -1
            if 0 <= indice < len(carrito):
                producto_eliminado = carrito.pop(indice)
                print(f"'Producto {producto_eliminado['nombre']}' eliminado del carrito.")
            else:
                print("Numero de producto invalido.")
        except ValueError:
            print("Entrada invalida. Debe ingresar un numero.")

def calcular_total(carrito):
    total = sum(producto['precio'] for producto in carrito)
    print(f"El total del carrito es: ${total:.2f}")
    
def main():
        carrito = []
        while True:
            mostrar_menu()
            opcion = input("Seleccione una opcion: ")
            if opcion == "1":
                agregar_producto(carrito)
            elif opcion == "2":
                ver_carrito(carrito)
            elif opcion == "3":
                eliminar_producto(carrito)
            elif opcion == "4":
                calcular_total(carrito)
            elif opcion == "5":
                print("Gracias por usar el carrito de compras. Hasta luego!")
                break
            else:
                print("Opcion invalida. Intente nuevamente.")
if a == 1:
    main()