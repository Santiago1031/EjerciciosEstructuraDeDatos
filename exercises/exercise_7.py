
# Una función de utilidad para imprimir una matriz
def printArr(arr, n):
    for i in range(n):
        print(arr[i], " ", end="")
    print()


''' Función para generar e imprimir todos
    matrices ordenadas de elementos alternativos de
   'A[i..m-1]' y 'B[j..n-1]'
   Si 'flag' es verdadero, entonces el elemento actual
   debe incluirse desde A de lo contrario
   desde B.
   'len' es el índice en la matriz de salida C[].
    Imprimimos la matriz de salida cada vez
   antes de incluir un carácter de A
   solo si la longitud de la matriz de salida es
   mayor que 0. Intentamos que todas las combinaciones posibles '''


def generateUtil(A, B, C, i, j, m, n, len, flag):
    if (flag):
# Incluir elemento válido de A

# Imprimir salida si hay en
        # menos una 'B' en la matriz de salida 'C'
        if (len):
            printArr(C, len + 1)

# Repetir para todos los elementos de
# A después del índice actual
        for k in range(i, m):

            if (not len):

                ''' este bloque funciona para el
                                    primera llamada para incluir
                                    el primer elemento en la matriz de salida '''
                C[len] = A[k]

                # no incremente el lem
                # ya que B está incluido todavía
                generateUtil(A, B, C, k + 1, j, m, n, len, not flag)

            else:

                # incluir un elemento válido de A y repetir
                if (A[k] > C[len]):
                    C[len + 1] = A[k]
                    generateUtil(A, B, C, k + 1, j, m, n, len + 1, not flag)


    else:

        # Incluir elemento válido de B y repetir
        for l in range(j, n):

            if (B[l] > C[len]):
                C[len + 1] = B[l]
                generateUtil(A, B, C, i, l + 1, m, n, len + 1, not flag)


# Función de envoltorio
def generate(A, B, m, n):
    C = []  # output array
    for i in range(m + n + 1):
        C.append(0)
    generateUtil(A, B, C, 0, 0, m, n, 0, True)



# Programa de controlador

A = [10, 15, 31]
B = [14, 20, 30]
n = len(A)
m = len(B)

generate(A, B, n, m)