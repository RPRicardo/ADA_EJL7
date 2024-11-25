def compressWord(word):
    comp = []  # Lista para construir el resultado
    i = 0  # Índice inicial
    n = len(word)  # Longitud de la cadena
    
    while i < n:
        char = word[i]  # Caracter actual
        count = 1  # Contamos la primera aparición del carácter
        
        # Contar repeticiones mientras sean consecutivas y no superen 9
        while i + count < n and word[i + count] == char and count < 9:
            count += 1
        
        # Agregar el bloque comprimido al resultado
        comp.append(f"{count}{char}")
        
        # Mover el puntero al siguiente bloque
        i += count
    
    # Unir y devolver el resultado
    return ''.join(comp)


word = "aabbbccccddddd"
print(compressWord(word)) 
