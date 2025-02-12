def contar_caracteres(s, c):
    if len(s) == 0:
        return 0
    else:
        if s[0] == c:
            return 1 + contar_caracteres(s[1:], c)
        else:
            return contar_caracteres(s[1:], c)

print(contar_caracteres("banana", "a"))