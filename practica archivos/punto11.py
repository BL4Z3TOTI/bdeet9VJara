def calcular_costo_telegrafo(mensaje):
    costo = 0
    letras_castellano = "ñáéíóú"
    for caracter in mensaje:
        if 'a' <= caracter.lower() <= 'z' and caracter.lower() not in letras_castellano:
            costo += 10
        elif caracter.isdigit():
            costo += 20
        elif not caracter.isspace():
            costo += 30
    return costo

mensaje = input("Ingrese un mensaje de prueba para calcular: ")
costo_total = calcular_costo_telegrafo(mensaje)
print(f"El costo del mensaje es: ${costo_total}")