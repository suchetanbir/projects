import numpy as np
import pandas as pd

# Importing movies and credit file
movies = pd.read_csv('tmdb_5000_movies.csv')
movie_credits = pd.read_csv('tmdb_5000_credits.csv')

# Merging Movies with the credit file
movies = movies.merge(movie_credits, on='title')


# Tags that are usefull
    # title
    # overviews
    # ID (for poster)
    # Genres
    # language 
    # keywords
    # cast
movies = movies[['movie_id','title','overview','genres','keywords','cast']]

# Data pre-processing   
    # 1. removing missing data
    # 2. removing duplicate data
    # 3. joining genres, keywords, cast to creates tags 
movies.dropna(inplace=True)
print(movies.isnull().sum())
