dataset = [
    ["altura_cm", "peso_kg", "idade"],
    [160, 55, 22],
    [165, 60, 25],
    [170, 65, 30],
    [175, 70, 35],
    [180, 80, 40],
]

def range_scaling(dataset):

    print("Data com range scaling:")
    print("-------------------------")
    print(dataset) 
    print("-------------------------")

    newData = [dataset[0][:]]  # Copia o cabeçalho
    min_values = []
    max_values = []
    
    for j in range(1, len(dataset)):
        for i in range(len(dataset[0])):
            if j == 1:
                min_values.append(dataset[j][i])
                max_values.append(dataset[j][i])
            else:
                if dataset[j][i] < min_values[i]:
                    min_values[i] = dataset[j][i]
                if dataset[j][i] > max_values[i]:
                    max_values[i] = dataset[j][i]    

    for j in range(1, len(dataset)):
        values = []
        for i in range(len(dataset[0])):
            val = (dataset[j][i] - min_values[i]) / (max_values[i] - min_values[i])
            values.append(val)
        newData.append(values)


    print("Data após range scaling:")
    print("-------------------------")
    print(newData)
    

range_scaling(dataset)