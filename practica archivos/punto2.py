import os

folder_path = input("Ingrese la ruta de la carpeta")
txt_files = []
try:
    for item in os.listdir(folder_path):
        item_path = os.path.join(folder_path, item)
        if os.path.isfile(item_path) and item.lower().endswith(".txt"):
            txt_files.append(item_path)

    if txt_files:
        confirmation = input(f"Se encontraron {len(txt_files)} archivos .txt. ¿Eliminar? (s/n): ")
        if confirmation.lower() == 's':
            for file_path in txt_files:
                os.remove(file_path)
                print(f"Eliminado: {file_path}")
        else:
            print("Operación cancelada.")
    else:
        print("No se encontraron archivos .txt en la carpeta.")

except FileNotFoundError:
    print(f"La carpeta '{folder_path}' no fue encontrada.")
except Exception as e:
    print(f"Ocurrió un error: {e}")
