a = "admin"
b = 1234
c = str(input("Ingrese su usuario: "))
if (a == c):
    d = int(input("Ingrese su clave: "))
    if(d == b):
        print("Bienvenido")
    else:
        print("Clave errada")
else:
    print("usuario incorrecto")