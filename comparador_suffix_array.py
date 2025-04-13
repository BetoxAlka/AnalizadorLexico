from io import BytesIO
import tokenize

def obtener_componentes_py(contenido):
    partes = []
    flujo = BytesIO(contenido.encode("utf-8")).readline
    for elemento in tokenize.tokenize(flujo):
        if elemento.type in (tokenize.NAME, tokenize.NUMBER, tokenize.STRING, tokenize.OP):
            partes.append(elemento.string)
    return partes

def construir_suffix_array_lista(tokens):
    n = len(tokens)
    sufijos = [(tokens[i:], i) for i in range(n)]
    sufijos.sort()
    return [indice for _, indice in sufijos]

def construir_lcp_lista(tokens, sufijos):
    n = len(tokens)
    rank = [0] * n
    for i in range(n):
        rank[sufijos[i]] = i
    lcp = [0] * (n - 1)
    h = 0
    for i in range(n):
        if rank[i] > 0:
            j = sufijos[rank[i] - 1]
            while i + h < n and j + h < n and tokens[i + h] == tokens[j + h]:
                h += 1
            lcp[rank[i] - 1] = h
            if h > 0:
                h -= 1
    return lcp

def comparador_suffix_array_lexico(ruta1, ruta2, salida="resultado_suffix.txt"):
    with open(ruta1, encoding="utf-8") as f1, open(ruta2, encoding="utf-8") as f2:
        contenido1 = f1.read()
        contenido2 = f2.read()

    tokens1 = obtener_componentes_py(contenido1)
    tokens2 = obtener_componentes_py(contenido2)

    combinado = tokens1 + ['#'] + tokens2 + ['$']
    sufijos = construir_suffix_array_lista(combinado)
    lcp = construir_lcp_lista(combinado, sufijos)

    with open(salida, "w", encoding="utf-8") as f:
        f.write("Tokens combinados:\n")
        f.write(" ".join(combinado) + "\n\n")
        f.write("Suffix Array:\n")
        f.write(str(sufijos) + "\n\n")
        f.write("LCP Array:\n")
        f.write(str(lcp) + "\n")

    print(f"Resultado guardado en {salida}")

if __name__ == "__main__":
    comparador_suffix_array_lexico("ejemplo1.c", "ejemplo2.c")
