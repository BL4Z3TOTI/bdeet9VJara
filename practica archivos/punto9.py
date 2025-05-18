input_file = input("Ingrese el nombre del archivo que desea invertir")
output_file = (input("Ingrese solo el nombre que desea llamar al nuevo archivo invertido")+".txt")

try:
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            outfile.write(line.rstrip()[::-1] + '\n')
    print(f"Contenido de '{input_file}' invertido y guardado en '{output_file}'")
except FileNotFoundError:
    print(f"Error: El archivo '{input_file}' no fue encontrado.")
