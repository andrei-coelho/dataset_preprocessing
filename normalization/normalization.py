import math

data = [
    ["produto_A", "visitas", "cliques", "compras"],
    ["A", 100, 10, 1],
    ["B", 200, 20, 2],
    ["C" , 50, 10, 1],
    ["D", 1000, 5, 1],
    ["E", 300, 30, 3]
]

def remove_noise(data):
    dataclean = []
    for d in data:
        dataclean.append(d[1:])
    return dataclean


def calc_tamanho_vetores(data):
    tamanhos_dos_vetores = []  # remove o cabeçalho
    for vector in data:
        tamanho = math.sqrt(sum([x**2 for x in vector]))
        tamanhos_dos_vetores.append(tamanho)
    return tamanhos_dos_vetores

def normalize_data(data):
   
    dataclean = remove_noise(data)
    datasemcabecalho = dataclean[1:]
    tamanhos_dos_vetores = calc_tamanho_vetores(datasemcabecalho)
   
    normalized_data = [dataclean[0]]  # adiciona o cabeçalho de volta
    for i, vector in enumerate(datasemcabecalho):
        tamanho = tamanhos_dos_vetores[i]
        if tamanho == 0:
            normalized_vector = vector
        else:
            normalized_vector = [x / tamanho for x in vector]
        normalized_data.append(normalized_vector)
    
    return normalized_data 


print("Data original:")

print(data)

print("-------------------------")

print("Data após normalização:")

normalized_data = normalize_data(data)

print(normalized_data)