import pandas as pd

dataset_path = "/Users/adrianvalera/git/personal/llamarec-rag/dataset/ml-25m-reduced/"
tags_dict = pd.read_csv(dataset_path+'genome-tags.csv')
tags_dict = tags_dict.set_index('tagId')['tag'].to_dict()

# Adds tags to the movies
movies = pd.read_csv(dataset_path+'movies.csv')
movies['tags'] = ""

scores = pd.read_csv(dataset_path+'genome-scores.csv')
scores['tags'] = ""

# Para cada pelicula
for index, row in movies.iterrows():
    movie_id = row['movieId']
    tag_ids = scores[scores['movieId'] == movie_id]['tagId'].values
    tag_ids = [tags_dict[tag_id] for tag_id in tag_ids]
    movies.at[index, 'tags'] = " ".join(tag_ids)

# Obtenemos los Tags que le pusieron los usuarios a la hora de valorarlas

movies.to_csv(dataset_path+'movies_enrich.csv', index=False)