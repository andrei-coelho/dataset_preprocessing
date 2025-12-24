import math

def escalar_pela_variancia(data):
    total_rows = len(data) - 1
    total_fields = len(data[0])

    # calcular variância por coluna
    variancias = [0.0] * total_fields

    for j in range(total_fields):
        soma = 0.0
        for i in range(1, total_rows + 1):
            soma += data[i][j] ** 2   # QUADRADO
        variancias[j] = soma / total_rows

    # desvio padrão
    desvios_padrao = [math.sqrt(v) for v in variancias]

    # escalar
    newData = [data[0][:]]

    for i in range(1, total_rows + 1):
        temp = []
        for j in range(total_fields):
            temp.append(data[i][j] / desvios_padrao[j])
        newData.append(temp)

    return newData


def transformar_zscore(data):
    total_fields = len(data[0])
    total_rows = len(data) - 1

    # calcular médias
    medias = [0.0] * total_fields

    for j in range(total_fields):
        soma = 0.0
        for i in range(1, total_rows + 1):
            soma += data[i][j]
        medias[j] = soma / total_rows

    # centralizar
    newData = [data[0][:]]

    for i in range(1, total_rows + 1):
        temp = []
        for j in range(total_fields):
            temp.append(data[i][j] - medias[j])
        newData.append(temp)

    return escalar_pela_variancia(newData)


def get_data():
    data = []
    header = True

    with open('dataset.txt', 'r') as file:
        for linha in file:
            linha = linha.strip()
            values = linha.split(';')

            if header:
                data.append(values)
                header = False
            else:
                data.append([float(v) for v in values])

    return data


def main():
    data = get_data()
    print("Data sem z-score:")
    print(data)

    newData = transformar_zscore(data)
    print("\nData com z-score:")
    print(newData)


main()
