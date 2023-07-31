

import re
# En esta línea, estamos importando el módulo re, que proporciona soporte para expresiones regulares en Python.
# Las expresiones regulares son patrones que se utilizan para buscar y manipular texto. En nuestro caso,
# utilizaremos expresiones regulares para verificar ciertas condiciones en la contraseña ingresada.


def verificar_fortaleza_contrasena(contrasena):
    longitud_minima = 8
    longitud_maxima = 16
    contiene_mayuscula = bool(re.search(r'[A-Z]', contrasena))
    contiene_minuscula = bool(re.search(r'[a-z]', contrasena))
    contiene_numero = bool(re.search(r'\d', contrasena))
    contiene_caracter_especial = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', contrasena))

    # La función re.search() toma un patrón de expresión regular y un texto (en este caso, la contraseña)
    # y busca si el patrón está presente en el texto. La función bool() convierte el resultado de re.search()
    # en un valor booleano True o False para que podamos utilizarlo en nuestras comprobaciones.

    if len(contrasena) < longitud_minima:
        return "La contraseña debe tener al menos 8 caracteres."

    # longitud_minima: Es un valor entero que representa la longitud mínima que debe tener la contraseña
    # (en este caso, 8 caracteres).

    if len(contrasena) > longitud_maxima:
        return "La contraseña debe tener maximo 16 caracteres."
    # longitud_maxima: Es un valor entero que representa la longitud maxima que debe tener la contraseña
    # (un maximo de 16 caracteres).

    elif not contiene_mayuscula:
        return "La contraseña debe contener al menos una letra mayúscula."

    # contiene_mayuscula: Es una variable booleana que se establecerá en True si la contraseña
    # contiene al menos una letra mayúscula (A-Z).

    elif not contiene_minuscula:
        return "La contraseña debe contener al menos una letra minúscula."

    # contiene_minuscula: Es una variable booleana que se establecerá en True si la contraseña
    # contiene al menos una letra minúscula (a-z).

    elif not contiene_numero:
        return "La contraseña debe contener al menos un número."



    # contiene_numero: Es una variable booleana que se establecerá en True si la contraseña
    # contiene al menos un número (0-9).

    elif not contiene_caracter_especial:
        return "La contraseña debe contener al menos un carácter especial (por ejemplo, !@#$%^&*(),.?\:{}|<>)."

    # contiene_caracter_especial: Es una variable booleana que se establecerá en True si la contraseña
    # contiene al menos un carácter especial, que es cualquier carácter que no sea letra o número

    else:
        return "La contraseña es lo suficientemente fuerte."
    # La contraeña ingresa es lo suficientemente fuerte: OK


print("UNIVERSIDAD INTERNACIONAL UIDE")
print("MAESTRIA EN CIBERSEGURIDAD")
print("CURSO DE PYTHON")
print("EXAMEN FINAL")
print("APICACION DE CONTRAEÑAS SEGURAS")
print()

print("INDIACIONES ACERCA DEL PROGRAMA")
print("Este programa verificará si la contraseña ingresada cumple con ciertas condiciones mínimas" )
print("para considerarse fuerte. Esas condiciones incluyen:" )
print("1.	Debe tener minimo 8 caracteres y maximo 16 caracteres de longitud")
print("2.	Debe contener al menos una letra mayúscula.")
print("3.	Debe contener al menos una letra minúscula.")
print("4.	Debe contener al menos un número.")
print("5.	Debe contener al menos un carácter especial (por ejemplo, "" !@#$%^&*(),.?:{}|<>).) "" ")


if __name__ == "__main__":
    contrasena = input("Ingrese una contraseña: ")
    resultado = verificar_fortaleza_contrasena(contrasena)
    print(resultado)
