import pandas as pd
from pymilvus import (
    connections,
    utility,
    FieldSchema, CollectionSchema, DataType,
    Collection,
)
from sentence_transformers import SentenceTransformer
from tqdm.auto import tqdm
tqdm.pandas()

#####
##### Embed model
print("Loading model...")
model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')


###### 
###### Milvus setup
print("Seting up milvus...")
collection_name = "movies"
num_entities, dim = 10000, 384

connections.connect("default", host="localhost", port="19530")
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
###### Populate Milvus
# Tomamos el dataset de las peliculas
dataset_path = "/Users/adrianvalera/git/personal/llamarec-rag/dataset/ml-25m-reduced/"
movies = pd.read_csv(dataset_path+'movies_enrich.csv')

batch_size = 1
page_batch_size = 10


i = 0
for index, row in tqdm(movies.iterrows(), total=movies.shape[0]):
    i+=1
    name = row['title']
    tags = row['tags']
    embed = model.encode(tags)
    milvus_db.insert([[name], [tags],  [embed]])

milvus_db.flush()