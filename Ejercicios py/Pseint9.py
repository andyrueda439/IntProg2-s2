def calculo_promedio():
    notas = []
    for i in range (5):
        nota = float(input(f"Ingrese la calificacion {i+1}: "))
        notas.append(nota)
    promedio = sum(notas) / 5
    print("El promedio del estudiante es: ", promedio)