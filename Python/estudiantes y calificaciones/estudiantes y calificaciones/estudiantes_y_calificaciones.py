estudiantes = [("ana", 85), ("Luis", 90), ("Marta", 75), ("Juan", 92)]

suma_calificaciones = 0
for estudiante, calificacion in estudiantes:
    print(f"estudiante: {estudiante}, calificacion: {calificacion}")
    suma_calificaciones += calificacion

promedio = suma_calificaciones / len(estudiantes)
print(f"promedio de calificaciones: {promedio}")