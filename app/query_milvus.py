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
import sys

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
fields = [
    FieldSchema(name="pk", dtype=DataType.VARCHAR, is_primary=True, auto_id=False, max_length=100),
    FieldSchema(name="content", dtype=DataType.VARCHAR, max_length=5000),
    FieldSchema(name="embeddings", dtype=DataType.FLOAT_VECTOR, dim=dim)
]
schema = CollectionSchema(fields, "Collection with movies and its tags as embeddings")
milvus_db = Collection(collection_name, schema, consistency_level="Strong")

######
###### Query

user_input = ' '.join(sys.argv[1:])
vectors_to_search = model.encode(user_input)
search_params = {
    "metric_type": "COSINE",
    "params": {"nprobe": 10}
}
result = milvus_db.search([vectors_to_search], "embeddings", search_params, limit=10, output_fields=["pk"])


try:
    for i in range(10):
        print(i, result[0][i].entity.get('pk'))
        #print(result[0][i].entity.get('content'))
    #print(result[0][1].entity.get('content'))
except Exception as e:
    pass

