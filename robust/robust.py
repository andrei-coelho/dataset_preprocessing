import math

dataset = [
    ["altura_cm", "peso_kg", "idade"],
    [165, 60, 25],
    [160, 55, 22],
    [162, 58, 24],
    [250, 500, 120],
    [170, 65, 30],
    [180, 80, 40],
    [190, 90, 45],
    [175, 70, 35],
]

def calcular_medianas(lista):
    
    n = len(lista)

    Q1 = None
    Q3 = None
    medianaQ2 = 0

    if n % 2 == 0:
        max = math.floor((n / 2))
        min = max - 1
        medianaQ2 = (lista[min] + lista[max]) / 2
        Q1 = lista[0:max]
        Q3 = lista[max:n]
    else:
        mid = math.floor(n / 2)
        medianaQ2 = lista[mid]
        Q1 = lista[0:mid]
        Q3 = lista[mid + 1:n]

    # Calcula mediana de Q1
    lenQ1 = len(Q1)
    if lenQ1 % 2 == 0:
        maxQ1 = math.floor((lenQ1 / 2))
        minQ1 = maxQ1 - 1
        medianaQ1 = (Q1[minQ1] + Q1[maxQ1]) / 2
    else:
        midQ1 = math.floor(lenQ1 / 2)
        medianaQ1 = Q1[midQ1]

    # Calcula mediana de Q3
    lenQ3 = len(Q3)
    if lenQ3 % 2 == 0:
        maxQ3 = math.floor((lenQ3 / 2))
        minQ3 = maxQ3 - 1
        medianaQ3 = (Q3[minQ3] + Q3[maxQ3]) / 2
    else:
        midQ3 = math.floor(lenQ3 / 2)
        medianaQ3 = Q3[midQ3]

    IQR = medianaQ3 - medianaQ1

    return medianaQ2, IQR



def robust_scaling(dataset):

    values = dataset[1:]  # Exclui o cabeçalho
    valores_ordenados = list(zip(*values))
    newlist = []
    
    for i in range(len(valores_ordenados)):
        
        lista = list(sorted(valores_ordenados[i]))
        temp_list = []
        medianaQ2,IQR = calcular_medianas(lista)

        for l in range(len(lista)):
            val = (lista[l] - medianaQ2) / IQR
            temp_list.append(val)

        newlist.append(temp_list)

    joinlist = [dataset[0][:]]
    while True:
        try:
            row = []
            for i in range(len(newlist)):
                row.append(newlist[i].pop(0))
            joinlist.append(row)
        except IndexError:
            break

    print("Data após robust scaling:")
    print("-------------------------")
    print(joinlist)



robust_scaling(dataset)