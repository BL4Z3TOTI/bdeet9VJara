import os
name = input("Ingresa tu nombre: ")
file_path = os.path.join("nombre.txt")
with open(file_path, 'a') as f:
    f.write(name + '\n')
print(f"Nombre guardado en {file_path}")
