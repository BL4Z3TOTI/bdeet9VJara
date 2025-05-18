numeros = [5, 15, 8, 25, 10, 12]
cuentamayoradiez = sum(1 for numero in numeros if numero > 10)
print(f"Cantidad de números mayores que 10: {cuentamayoradiez}")