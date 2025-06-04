print("Calculadora de calificaciones.")
a = int(input("Ingrese la cantidad de estudiantes: "))
calificaiones = []
for z in range(a):
    b = int(input(f"ingrese la nota de el {z+1} estudiante: "))
    calificaiones.append(b)
    
suma = sum(calificaiones)
promedio = suma / a
minimo = min(calificaiones)
maxima = max(calificaiones)

print(f"la suma de todas las notas es {suma}")
print(f"el promedio de las notas es {promedio}")
print(f"la nota alta fue {maxima}")
print(f"la nota baja fue {minimo}")


