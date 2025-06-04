print("Calculadora de descueto")
a = int(input("Ingrese el costo de su producto: "))
b = a * 0.15
c = a - b
if(a>100):
    print(f"su producto es valido para el descuento y el valor total es {c}")
else:
      print(f"su producto no es valido para el descuento.")
    