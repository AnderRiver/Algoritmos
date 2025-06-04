def mostrar_menu():
    print("--- Menu Carrito de Compras ---")
    print("1. Agregar un nuevo elemento")
    print("2. Mostrar el contenido de la cesta de la compra")
    print("3. Eliminar un elemento")
    print("4. Calcular el total")
    print("5. Renunciar (Salir)")

def agregar_elemento(carrito):
    nombre = input("Nombre del producto: ")
    try:
        precio = float(input("Precio del producto: "))
        carrito.append({'nombre': nombre, 'precio': precio})
        print(f"'{nombre}' agregado al carrito.")
    except ValueError:
        print("Precio invalido. Intenta de nuevo.")

def mostrar_carrito(carrito):
    if not carrito:
        print("El carrito esta vacio.")
    else:
        print("\nContenido del carrito:")
        for idx, item in enumerate(carrito, 1):
            print(f"{idx}. {item['nombre']} - ${item['precio']:.2f}")

def eliminar_elemento(carrito):
    mostrar_carrito(carrito)
    if carrito:
        try:
            idx = int(input("Numero del elemento a eliminar: "))
            if 1 <= idx <= len(carrito):
                eliminado = carrito.pop(idx - 1)
                print(f"'{eliminado['nombre']}' eliminado del carrito.")
            else:
                print("Indice fuera de rango.")
        except ValueError:
            print("Entrada invalida.")

def calcular_total(carrito):
    total = sum(item['precio'] for item in carrito)
    print(f"Total a pagar: ${total:.2f}")

def main():
    carrito = []
    while True:
        mostrar_menu()
        opcion = input("Elige una opcion (1-5): ")
        if opcion == '1':
            agregar_elemento(carrito)
        elif opcion == '2':
            mostrar_carrito(carrito)
        elif opcion == '3':
            eliminar_elemento(carrito)
        elif opcion == '4':
            calcular_total(carrito)
        elif opcion == '5':
            print("Gracias por usar el carrito de compras!")
            break
        else:
            print("Opcion no valida. Intenta de nuevo.")

if __name__ == "__main__":
    main()
