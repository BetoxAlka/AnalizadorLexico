import difflib # Importar libreria difflib

def read_file(path): # Funcion para leer archivos 
    with open(path, 'r', encoding='utf-8') as file:
        return file.readlines() # Crea una lista de lineas de codigo
    
def compare_files(lines1, lines2): # Funcion para comparar lineas de codigo
    matcher = difflib.SequenceMatcher(None, lines1, lines2) # Funcion difflib para comparar lineas
    matches = [block for block in matcher.get_matching_blocks() if block.size > 0] # Metodo para obtener cada bloque similar del comparador siempre y cuando sea mayor a 0 caracteres
    
    detailed_sections = [] # Genera lista de similitudes
    for i, match in enumerate(matches): # Por cada similitud encontrada, se enumera...
        a_start, b_start, size = match.a, match.b, match.size # Se establecen el inicio de cada bloque y su tamanio...
        block1 = lines1[a_start:a_start + size] # Bloque del primer archivo
        block2 = lines2[b_start:b_start + size] # Bloque del segundo archivo

        section_text = ( # Se muestra la seccion con similitudes en lineas de codigo
            f"[Bloque {i+1}]\n"
            f"Archivo 1 (líneas {a_start} a {a_start + size}):\n{''.join(block1) if block1 else '[VACÍO]'}\n"
            f"Archivo 2 (líneas {b_start} a {b_start + size}):\n{''.join(block2) if block2 else '[VACÍO]'}"
        )

        detailed_sections.append(section_text) # Se agrega el texto a la lista

    return matches, matcher.ratio(), detailed_sections # Crea los bloques de similitud, el porcentae de similitud y lista de simulitudes
    
if __name__ == "__main__":
    # Cambia estos nombres de archivo por los que desees comparar
    path1 = 'files/sudoku.py'
    path2 = 'files/password_manager.py'
    
    file1_lines = read_file(path1)
    file2_lines = read_file(path2)

    matches, ratio, detailed_sections = compare_files(file1_lines, file2_lines)
    
    print(f'Comparando los archivos: {path1[6:]} vs {path2[6:]}')
    print(f"Porcentaje de similitud: {ratio * 100:.2f}%")
    print("\nSecciones similares:")

    if not detailed_sections:
        print("No se encontraron secciones similares.")
    else:
        for section in detailed_sections:
            print(section)

