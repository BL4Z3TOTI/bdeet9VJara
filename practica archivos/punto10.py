input_file = input("Ingrese el nombre del archivo y extension")
output_file = input("Ingrese el nombre del archivo en el que las lineas vacias van a ser eliminadas")+".txt"

try:
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            if line.strip():
                outfile.write(line)
    print(f"Líneas vacías eliminadas de '{input_file}' y guardado en '{output_file}'")
except FileNotFoundError:
    print(f"Error: El archivo '{input_file}' no fue encontrado.")