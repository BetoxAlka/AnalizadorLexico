import re

def obtener_componentes_c(contenido, archivo_tokens="tokens_validos.txt", archivo_log="elementos_ignorados.txt"):
    patrones = [
        (r'\b(?:int|float|return|if|else|while|for|void|char)\b', 'K'),
        (r'"[^"]*"', 'STR'),
        (r'\d+', 'NUM'),
        (r'==|!=|<=|>=|<|>|=|\+|\-|\*|/|\(|\)|\{|\}|;', 'OP'),
        (r'[a-zA-Z_][a-zA-Z0-9_]*', 'ID'),
    ]
    expresion = '|'.join(f'(?P<{n}>{p})' for p, n in patrones)

    tokens_validos = []
    ignorados = []

    lineas = contenido.splitlines()

    for num_linea, linea in enumerate(lineas, start=1):
        for match in re.finditer(expresion, linea):
            tipo = match.lastgroup
            valor = match.group()
            columna = match.start() + 1
            tokens_validos.append((tipo, valor, num_linea, columna))

        # Buscar tokens no reconocidos
        for palabra in re.finditer(r'\S+', linea):
            if not re.match(expresion, palabra.group()):
                ignorados.append((palabra.group(), num_linea, palabra.start() + 1))

    # Guardar tokens válidos
    with open(archivo_tokens, "w", encoding="utf-8") as f:
        for tipo, valor, linea, columna in tokens_validos:
            f.write(f"{tipo}\t{valor}\tLínea: {linea}, Columna: {columna}\n")

    # Guardar tokens no reconocidos
    with open(archivo_log, "w", encoding="utf-8") as f:
        for palabra, linea, columna in ignorados:
            f.write(f"{palabra} - No reconocido. Línea: {linea}, Columna: {columna}\n")

    return tokens_validos

if __name__ == "__main__":
    with open("codigo_c.c", "r", encoding="utf-8") as f:
        contenido = f.read()
    obtener_componentes_c(contenido)