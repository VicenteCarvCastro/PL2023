import json

# Abrir o arquivo de texto e ler as linhas
with open('processos.txt', 'r') as file:
    linhas = file.readlines()

# Dicionários para armazenar as frequências
freq_processos = {}
freq_nomes = {}
freq_apelidos = {}
freq_relacoes = {}

# Loop pelas linhas do arquivo
for linha in linhas:
    # Dividir a linha em campos
    campos = linha.strip().split(':: ')
    numero = campos[0]
    data = campos[1]
    nomes = campos[2].split(' ')
    tipo_relacao = campos[3]

    # Frequência de processos por ano
    ano = data.split('-')[0]
    if ano in freq_processos:
        freq_processos[ano] += 1
    else:
        freq_processos[ano] = 1

    # Frequência de nomes próprios e apelidos
    primeiro_nome = nomes[0]
    ultimo_nome = nom