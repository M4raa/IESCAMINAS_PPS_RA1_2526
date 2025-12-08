import random
import string

## extraemos la funcion y la probamos fuera del programa real para no llamar a la ui.
def generar_password(longitud, usar_mayus, usar_minus, usar_numeros, usar_simbolos):
    
    caracteres = ""

    if usar_mayus:
        caracteres += string.ascii_uppercase
    if usar_minus:
        caracteres += string.ascii_lowercase
    if usar_numeros:
        caracteres += string.digits
    if usar_simbolos:
        caracteres += string.punctuation

    if not caracteres:
        raise ValueError("Debe seleccionarse al menos un tipo de carácter.")

    password = []

    if usar_mayus:
        password.append(random.choice(string.ascii_uppercase))
    if usar_minus:
        password.append(random.choice(string.ascii_lowercase))
    if usar_numeros:
        password.append(random.choice(string.digits))
    if usar_simbolos:
        password.append(random.choice(string.punctuation))

    while len(password) < longitud:
        password.append(random.choice(caracteres))

    random.shuffle(password)

    return "".join(password)
