class GFG:
    def solve(self, arr):
        self.res.add(tuple(arr))  # agregar partición actual al resultado
        if len(arr)<=1:  # Caso base cuando no hay nada que fusionar
            return
        for i in range(1,len(arr)):
            if arr[i-1]==arr[i][::-1]: # Cuando dos adyacentes tales que uno es el reverso de otro
                brr = arr[:i-1] + [arr[i-1]+arr[i]] + arr[i+1:]
                self.solve(brr)
            if i+1<len(arr) and arr[i-1]==arr[i+1][::-1]:  # Todos son individualmente palíndromos,
              # cuando uno a la izquierda y uno a la derecha de i están invertidos, entonces podemos fusionarnos
              # los tres para formar una nueva forma de partición
                brr = arr[:i-1] + [arr[i-1]+arr[i]+arr[i+1]] + arr[i+2:]
                self.solve(brr)
    def getGray(self, S):
        self.res = set()  # el resultado es un conjunto de tuplas para evitar la misma partición varias veces
        self.solve(list(S)) # Llamar a la función recursiva para resolver S
        return sorted(list(self.res))

# código de conductor
ob = GFG()
allPart = ob.getGray("kakaroto")
for i in range(len(allPart)):
    for j in range(len(allPart[i])):
        print(allPart[i][j], end = " ")
    print()
