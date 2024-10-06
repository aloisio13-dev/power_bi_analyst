import pandas as pd

# Criando a tabela com os atos infracionais, artigos e penalidades
dados = {
    "Ato Infracional": [
        "Furto e Roubo", 
        "Tráfico de Drogas", 
        "Porte de Drogas", 
        "Homicídio", 
        "Lesão Corporal", 
        "Ato de Violência Sexual", 
        "Participação em Organização Criminosa", 
        "Desacato à Autoridade", 
        "Vandalismo/Depredação de Patrimônio"
    ],
    "Artigo": [
        "Art. 103", 
        "Art. 112", 
        "Art. 112", 
        "Art. 112", 
        "Art. 112", 
        "Art. 112", 
        "Art. 112", 
        "Art. 103", 
        "Art. 112"
    ],
    "Penalidades/Medidas Socioeducativas": [
        "Advertência, obrigação de reparar o dano, prestação de serviços à comunidade, liberdade assistida, internação.",
        "Liberdade assistida, inserção em regime de semiliberdade, internação em estabelecimento educacional.",
        "Advertência, liberdade assistida, prestação de serviços à comunidade.",
        "Internação em estabelecimento educacional, semiliberdade.",
        "Advertência, reparação do dano, prestação de serviços à comunidade, internação.",
        "Internação em estabelecimento educacional, semiliberdade, liberdade assistida.",
        "Internação, semiliberdade, liberdade assistida.",
        "Advertência, liberdade assistida.",
        "Reparação do dano, prestação de serviços à comunidade, liberdade assistida."
    ]
}

# Criando o DataFrame
df = pd.DataFrame(dados)

# Salvando em um arquivo Excel
file_path = "/mnt/data/atos_infracionais_eca.xlsx"
df.to_excel(file_path, index=False)

file_path