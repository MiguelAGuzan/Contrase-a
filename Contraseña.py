import random
import string

# Función para generar la contraseña
def generar_contraseña(longitud, incluir_simbolos=False):
    caracteres = string.ascii_letters + string.digits  # Letras y números
    if incluir_simbolos:
        caracteres += string.punctuation  # Añadir símbolos

    # Generar la contraseña de manera aleatoria
    contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contraseña

# Función para guardar la contraseña en un archivo
def guardar_contraseña(contraseña):
    with open("contraseñas_guardadas.txt", "a") as archivo:
        archivo.write(contraseña + "\n")  # Guardar la contraseña con un salto de línea
    print("Contraseña guardada en 'contraseñas_guardadas.txt'.")

# Pedir al usuario la longitud de la contraseña
longitud = int(input("Ingrese la longitud de la contraseña: "))

# Preguntar si se desea incluir símbolos
incluir_simbolos_input = input("¿Incluir símbolos? (sí/no): ").strip().lower()
incluir_simbolos = incluir_simbolos_input == "sí"

# Generar la contraseña
contraseña = generar_contraseña(longitud, incluir_simbolos)
print("Contraseña generada:", contraseña)

# Guardar la contraseña en un archivo
guardar_contraseña(contraseña)
