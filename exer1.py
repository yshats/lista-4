def reverter_caracteres(s):
    if len(s) == 0:
        return s
    else:
        return reverter_caracteres(s[1:]) + s[0]

print(reverter_caracteres("Python"))