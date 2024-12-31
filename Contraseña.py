import random
import string

def generar_contraseña(longitud=12, usar_mayusculas=True, usar_numeros=True, usar_simbolos=True):
    caracteres = string.ascii_lowercase  # letras minúsculas

    if usar_mayusculas:
        caracteres += string.ascii_uppercase  # letras mayúsculas
    if usar_numeros:
        caracteres += string.digits  # números
    if usar_simbolos:
        caracteres += string.punctuation  # caracteres especiales

    # Generar la contraseña
    contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contraseña

# Ejemplo de uso
print(generar_contraseña(longitud=16, usar_mayusculas=True, usar_numeros=True, usar_simbolos=True))
