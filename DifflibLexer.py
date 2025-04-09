import difflib # Importar libreria difflib

def read_file(path): # Funcion para leer archivos 
    with open(path, 'r', encoding='utf-8') as file:
        return file.readlines() # Crea una lista de lineas de codigo
    
def compare_files(lines1,lines2): # Funcion para comparar lineas de codigo
    matcher = difflib.SequenceMatcher(None, lines1, lines2) # Funcion difflib para comparar lineas
    matches = [block for block in matcher.get_matching_blocks() if block.size > 0] # Metodo para obtener cada bloque similar del comparador siempre y cuando sea mayor a 0 caracteres
    
    similar_sections = [] # Genera lista de similitudes
    for match in matches: # Por cada similitud encontrada...
        if match.size > 0: # Siempre y cuando no sea vacia...
            block = lines1[match.a: match.a + match.size] # En cada bloque se recupera el texto similar completo
            similar_sections.append(''.join(block)) # Se agrega dicho texto a la lista

    return matches, matcher.ratio(), similar_sections # Crea los bloques de similitud, el porcentae de similitud y lista de simulitudes

if __name__ == "__main__":
    # Cambia estos nombres de archivo por los que desees comparar
    path1 = 'files/sudoku.py'
    path2 = 'files/password_manager.py'
    
    file1_lines = read_file(path1)
    file2_lines = read_file(path2)

    matches, ratio, similar_sections = compare_files(file1_lines, file2_lines)
    
    print(f'Comparando los archivos: {path1[6:]} vs {path2[6:]}')
    print(f"Porcentaje de similitud: {ratio * 100:.2f}%")
    print("\nSecciones similares:")

    for i, section in enumerate(similar_sections, 1):
        print(f"Seccion {i}: \n{section}")

