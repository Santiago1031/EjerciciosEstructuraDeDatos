# Programa Python3 para imprimir tod
# secuencias crecientes de longitud
# 'k' tal que los elementos en
# todas las secuencias son desde el principio
# 'n' números naturales.

# Una función de utilidad para
# imprime el contenido de arr[0..k-1]
def printArr(arr, k):
    for i in range(k):
        print(arr[i], end=" ");
    print();


# Una función recursiva para imprimir
# todas las secuencias crecientes de
# primeros n números naturales. Cada
# la secuencia debe tener una longitud k.
# La matriz arr[] se usa para
# almacenar la secuencia actual.
def printSeqUtil(n, k, len1, arr):
    # Si la longitud de la corriente
    # secuencia creciente
    # se convierte en k, imprímelo
    if (len1 == k):
        printArr(arr, k);
        return;

    # Decide el número inicial
    # para poner en la posición actual:
    # Si la longitud es 0, entonces hay
    # no hay elementos anteriores
    # en arr[]. Así que empieza a poner
    # números nuevos con 1. Si la longitud
    # no es 0, luego comienza desde el valor
    # del elemento anterior más 1.
    i = 1 if (len1 == 0) else (arr[len1 - 1] + 1);

    # Aumentar longitud
    len1 += 1;

    # Poner todos los números (los que son mayores
    # que el elemento anterior) en
    # nueva posición.
    while (i <= n):
        arr[len1 - 1] = i;
        printSeqUtil(n, k, len1, arr);
        i += 1;

    # Esto es importante. La variable
    # 'len' se comparte entre todas las funciones
    # llamadas en el árbol de recursividad. Es valioso
    # debe devolverse antes del próximo
    # iteración del ciclo while
    len1 -= 1;


# Esta funcion imprime todos los crecientes
# secuencias de primeros n números naturales.
# La longitud de cada secuencia debe ser
# k. Esta función utiliza principalmente printSeqUtil()
def printSeq(n, k):
    arr = [0] * k;  # Una matriz para almacenar
    # secuencias individuales
    len1 = 0;  # Longitud inicial de
    # secuencia actual
    printSeqUtil(n, k, len1, arr);


# Código conductor
k = 2;
n = 4;
printSeq(n, k);

