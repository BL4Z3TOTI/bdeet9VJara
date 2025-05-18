file_path = input("Ingrese la ruta al archivo: ")
try:
    with open(file_path, 'r') as f:
        content = f.read()
        line_count = content.count('\n') + 1
        word_count = len(content.split())
        char_count = len(content)
        print(f"Líneas: {line_count}")
        print(f"Palabras: {word_count}")
        print(f"Caracteres: {char_count}")
except FileNotFoundError:
    print(f"Error: El archivo '{file_path}' no fue encontrado.")
