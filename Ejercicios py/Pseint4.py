def division():
    a = int(input("Ingrese el numerador (entero): "))
    b = int(input("Ingrese el denominador(entero, distinto de cero): "))
    while b== 0:
        print("El divisor no puede ser cero. Intente de nuevo.")
        b = int(input("Ingrese el denominador (entero, distinto de cero): "))
    print("El cociente es:", a / b)
