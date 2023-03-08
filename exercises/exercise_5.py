# Programa Python3 para crear un triángulo especial.
# Función para generar Triángulo Especial.
def printTriangle(A):
    # Caso base
    if (len(A) < 1):
        return

    # Creando una nueva matriz que contiene el
    # Suma de elementos consecutivos en
    # la matriz pasa como parámetro.
    temp = [0] * (len(A) - 1)
    for i in range(0, len(A) - 1):
        x = A[i] + A[i + 1]
        temp[i] = x

    # Haz una llamada recursiva y pasa
    # la matriz recién creada
    printTriangle(temp)

    # Imprime la matriz actual al final para que
    # que las matrices más pequeñas se imprimen primero
    print(A)


# Función de controlador
A = [1, 3, 5, 7]
printTriangle(A)
