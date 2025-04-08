import difflib

textoA = ['Hola', 'Mundo', 'soy', 'un', 'loco', 'negro','sasuke','dios']
textoB = ['Asios', 'loco', 'mundo', 'no', 'lo', 'pienses', 'negro','naruto','dios']

matcher = difflib.SequenceMatcher(None, textoA,textoB)
matches = [block for block in matcher.get_matching_blocks() if block.size > 0]

print(matches)
print("Porcentaje de similitud:", matcher.ratio())

similar_sections = []
for match in matches:
    if match.size > 0:
        block = textoA[match.a: match.a + match.size]
        similar_sections.append(''.join(block))

print(similar_sections)

