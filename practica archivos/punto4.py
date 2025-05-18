import os

folder_path = input("ingrese la ruta de la carpeta")
files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
files.sort()
for index, file_name in enumerate(files):
    old_path = os.path.join(folder_path, file_name)
    new_name = f"{index + 1}_{file_name}"
    new_path = os.path.join(folder_path, new_name)
    os.rename(old_path, new_path)
    print(f"Renombrado: {file_name} -> {new_name}")
