import pandas as pd

# Tomamos el dataset de las peliculas
dataset_path = "/Users/adrianvalera/git/personal/llamarec-rag/dataset/ml-25m-reduced/"
movies = pd.read_csv(dataset_path+'movies-enriched.csv')

# para cada elemento
for index, row in movies.iterrows():
    # Hacemos un embedding
    pass
    # Lo guardamos en Milvus