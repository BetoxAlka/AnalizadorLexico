import difflib # Importar libreria difflib

def read_file(path): # Funcion para leer archivos 
    with open(path, 'r', encoding='utf-8') as file:
        return file.readlines() # Crea una lista de lineas de codigo
    
def compare_files(lines1, lines2): # Funcion para comparar lineas de codigo
    matcher = difflib.SequenceMatcher(None, lines1, lines2) # Funcion difflib para comparar lineas
    opcodes = matcher.get_opcodes() # Metodo para obtener bloques de similitud

    detailed_sections = [] # Genera lista de similitudes
    block = 1 # Numero de bloque
    for i, (tag, i1, i2, j1, j2) in enumerate(opcodes): # Por cada similitud encontrada, se enumera el inicio y final de cada linea...
        block1 = lines1[i1:i2] # Bloque del primer archivo
        block2 = lines2[j1:j2] # Bloque del segundo archivo

        # Filtramos solo bloques donde haya algo relevante
        if not any(line.strip() for line in block1 + block2):
            continue

        section_text = ( # Se muestra la seccion con similitudes en lineas de codigo
            f"[Bloque {block}] Tipo: {tag.upper()}\n"
            f"Archivo 1 (líneas {i1} a {i2}):\n{''.join(block1) or '[VACÍO]'}\n"
            f"Archivo 2 (líneas {j1} a {j2}):\n{''.join(block2) or '[VACÍO]'}"
        )

        detailed_sections.append(section_text) # Se agrega el texto a la lista

        block += 1

    return matcher.ratio(), detailed_sections # Crea el porcentae de similitud y lista de simulitudes
    
if __name__ == "__main__":
    # Cambia estos nombres de archivo por los que desees comparar
    path1 = 'files/sudoku.py'
    path2 = 'files/password_manager.py'
    
    file1_lines = read_file(path1)
    file2_lines = read_file(path2)

    ratio, detailed_sections = compare_files(file1_lines, file2_lines)
    
    print(f'Comparando los archivos: {path1[6:]} vs {path2[6:]}')
    print(f"Porcentaje de similitud: {ratio * 100:.2f}%")
    print("\nSecciones similares:")

    if not detailed_sections:
        print("No se encontraron secciones similares.")
    else:
        for section in detailed_sections:
            print(section)

