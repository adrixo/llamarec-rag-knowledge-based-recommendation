import pandas as pd
from pymilvus import (
    connections,
    utility,
    FieldSchema, CollectionSchema, DataType,
    Collection,
)

###### 
###### 
collection_name = "movies"
num_entities, dim = 10000, 384

connections.connect("default", host="milvus", port="19530")
utility.drop_collection(collection_name)
fields = [
    FieldSchema(name="pk", dtype=DataType.VARCHAR, is_primary=True, auto_id=False, max_length=100),
    FieldSchema(name="content", dtype=DataType.VARCHAR, max_length=5000),
    FieldSchema(name="embeddings", dtype=DataType.FLOAT_VECTOR, dim=dim)
]
schema = CollectionSchema(fields, "Collection with movies and its tags as embeddings")
milvus_db = Collection(collection_name, schema, consistency_level="Strong")
print(f"Collection '{collection_name}' is created: {utility.has_collection(collection_name)}")

###### 
###### 
# Tomamos el dataset de las peliculas
dataset_path = "/Users/adrianvalera/git/personal/llamarec-rag/dataset/ml-25m-reduced/"
movies = pd.read_csv(dataset_path+'movies-enriched.csv')

# para cada elemento
for index, row in movies.iterrows():
    # Hacemos un embedding
    pass
    # Lo guardamos en Milvus