def validar_dimensiones(filas_a, columnas_a, filas_b, columnas_b):
    if columnas_a != filas_b:
        return False
    return True


def ingresar_matriz(nombre):
    print(f"Ingresando matriz {nombre}:")
    filas = int(input("Ingrese el número de filas: "))
    columnas = int(input("Ingrese el número de columnas: "))
    matriz = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            valor = float(input(f"Ingrese el valor de la posición ({i}, {j}): "))
            fila.append(valor)
        matriz.append(fila)
    return matriz


def multiplicar_matrices(matriz_a, matriz_b):
    filas_a = len(matriz_a)
    columnas_a = len(matriz_a[0])
    filas_b = len(matriz_b)
    columnas_b = len(matriz_b[0])

    if not validar_dimensiones(filas_a, columnas_a, filas_b, columnas_b):
        print(
            "Error: Las matrices no se pueden multiplicar. El número de columnas de la matriz A debe ser igual al número de filas de la matriz B.")
        return None

    resultado = []
    for i in range(filas_a):
        fila_resultado = []
        for j in range(columnas_b):
            suma = 0
            for k in range(columnas_a):
                suma += matriz_a[i][k] * matriz_b[k][j]
            fila_resultado.append(suma)
        resultado.append(fila_resultado)

    return resultado


def mostrar_matriz(matriz, nombre):
    print(f"Matriz {nombre}:")
    for fila in matriz:
        print(fila)


def main():
    print("Multiplicación de matrices")

    matriz_a = ingresar_matriz("A")
    matriz_b = ingresar_matriz("B")

    print()
    mostrar_matriz(matriz_a, "A")
    print()
    mostrar_matriz(matriz_b, "B")
    print()

    resultado = multiplicar_matrices(matriz_a, matriz_b)

    if resultado:
        print("Resultado de la multiplicación:")
        mostrar_matriz(resultado, "Resultado")


if __name__ == "__main__":
    main()