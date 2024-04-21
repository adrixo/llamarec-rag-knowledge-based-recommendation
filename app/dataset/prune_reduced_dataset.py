import pandas as pd

dataset_path = "/Users/adrianvalera/git/personal/llamarec-rag/dataset/ml-25m-reduced/"
full_dataset_path = "/Users/adrianvalera/git/personal/llamarec-rag/dataset/ml-25m/"


def prune_movies():
    # maintain only movies rated by users 1,2,6
    movies = pd.read_csv(dataset_path+'movies.csv')
    movies.set_index('movieId', inplace=True)

    ratings = pd.read_csv(dataset_path+'ratings.csv')

    # iterate all rows in ratings
    new_movies = movies[movies.index.isin(ratings['movieId'])].copy()

    new_movies.to_csv(dataset_path+'movies.csv', index=True)

def prune_links():
    links = pd.read_csv(dataset_path+'links.csv')
    links.set_index('movieId', inplace=True)

    movies = pd.read_csv(dataset_path+'movies.csv')

    # iterate all rows in ratings
    new_links = links[links.index.isin(movies['movieId'])].copy()

    new_links.to_csv(dataset_path+'links.csv', index=True)


def prune_tags():
    users = pd.read_csv(dataset_path+'ratings.csv')

    tags = pd.read_csv(full_dataset_path+'tags.csv')
    print(tags.columns)

    # iterate all rows in ratings
    #new_tags = tags[tags.index.isin(users['movieId'])].copy()
    new_tags = tags[tags.index.isin(users['userId'])].copy()

    new_tags.to_csv(dataset_path+'tags.csv', index=True)

def prune_genome_scores():
    genomes = pd.read_csv(full_dataset_path+'genome-scores.csv')

    filtered = genomes[genomes['relevance'] > 0.8]

    filtered.to_csv(dataset_path+'genome-scores.csv', index=False)

prune_movies()
prune_links()