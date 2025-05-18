import os

folder_path = input("Ingrese la ruta de la carpeta: ")
file_count = 0
for item in os.listdir(folder_path):
    item_path = os.path.join(folder_path, item)
    if os.path.isfile(item_path):
        file_count += 1
print(f"Cantidad de archivos en la carpeta: {file_count}")
