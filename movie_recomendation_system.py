import numpy as np
import pandas as pd
import ast 

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

movies.dropna(inplace=True) # dropna removes rows with atleast one NaN and inplace modifies the movies instead of giving a new one

# Now to just get the tags instead of a list 
# for example in genre
# instead of {[id = , name = ], [id = , name = ]} we want [name, name, name] i.e. [adventure, fantasy, scifi]

# the function wont work as the list is a string 
    # need to use ast module
        # will convert the string into a list 
        
def convert(obj):
    list_names = []
    for i in ast.literal_eval(obj):
        list_names.append(i['name'])
    return list_names

#print(movies['genres'].apply(convert))



