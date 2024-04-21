import pandas as pd

dataset_path = "/Users/adrianvalera/git/personal/llamarec-rag/dataset/ml-25m-reduced/"
tags_dict = pd.read_csv(dataset_path+'genome-tags.csv')
tags_dict = tags_dict.set_index('tagId')['tag'].to_dict()

# Adds tags to the movies
movies = pd.read_csv(dataset_path+'movies.csv')
movies['tags'] = ""
movies['rated_tags'] = ""

scores = pd.read_csv(dataset_path+'genome-scores.csv')
rated_movies_with_tag = pd.read_csv(dataset_path+'tags_movies_rated.csv')

# Para cada pelicula
for index, row in movies.iterrows():
    movie_id = row['movieId']
    # For genome
    tag_ids = scores[scores['movieId'] == movie_id]['tagId'].values
    tag_ids = [tags_dict[tag_id] for tag_id in tag_ids]
    movies.at[index, 'tags'] = " ".join(tag_ids)
    # For rated tags
    t = rated_movies_with_tag[rated_movies_with_tag['movieId'] == movie_id]['tag'].values
    movies.at[index, 'rated_tags'] = t

# Obtenemos los Tags que le pusieron los usuarios a la hora de valorarlas

movies.to_csv(dataset_path+'movies_enrich.csv', index=False)