def conversion_dolares_a_cordobas():
    dolares = float(input("Ingrese la cantidad en dolares: "))
    tipo_cambio = float(input("Ingrese el tipo de cambio: "))
    cordobas = dolares * tipo_cambio
    print("El equivalente en cordobas es:", cordobas)