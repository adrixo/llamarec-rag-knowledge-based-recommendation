import pandas as pd

dataset_path = "dataset/ml-25m-reduced/"

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

    new_links.to_csv(dataset_path+'links.csv', index=False)

prune_movies()
prune_links()