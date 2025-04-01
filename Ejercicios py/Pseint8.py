def conversion_cordobas_a_dolares():
    cordobas = float((input/"Ingrese la cantidad en cordobas"))
    tipo_cambio = float(input("Ingrese el tipo de cambio: "))
    dolares = cordobas / tipo_cambio
    print("El equivalente en dolares es:", dolares)