# la estructura se usa para devolver dos valores de minMax()
class pair:
    def __init__(self):
        self.min = 0
        self.max = 0


def getMinMax(arr: list, n: int) -> pair:
    minmax = pair()

    # Si solo hay un elemento, devuélvalo como min y max ambos
    if n == 1:
        minmax.max = arr[0]
        minmax.min = arr[0]
        return minmax

    # Si hay más de un elemento, inicialice min
    # y máximo
    if arr[0] > arr[1]:
        minmax.max = arr[0]
        minmax.min = arr[1]
    else:
        minmax.max = arr[1]
        minmax.min = arr[0]

    for i in range(2, n):
        if arr[i] > minmax.max:
            minmax.max = arr[i]
        elif arr[i] < minmax.min:
            minmax.min = arr[i]

    return minmax


# código de conductor
if __name__ == "__main__":
    arr = [1000, 1001, 999, 992]
    arr_size = 4
    minmax = getMinMax(arr, arr_size)
    print("Minimum element is", minmax.min)
    print("Maximum element is", minmax.max)
