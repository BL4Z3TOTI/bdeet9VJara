import os
base_dir = "proyecto"
sub_dirs = ["datos", "scripts", "resultados"]

os.makedirs(base_dir, exist_ok=True)
for sub_dir in sub_dirs:
    os.makedirs(os.path.join(base_dir, sub_dir), exist_ok=True)
print(f"Estructura de carpetas creada en: {base_dir}")