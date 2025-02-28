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
movies = movies[['movie_id','title','overview','genres','keywords','cast', 'crew']]

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


movies['genres'] = movies['genres'].apply(convert)
movies['keywords'] = movies['keywords'].apply(convert)

# now for cast 
def convert_cast(obj):
    list_names = []
    counter = 0
    for i in ast.literal_eval(obj):
        if counter != 3:
            list_names.append(i['name'])
            counter+=1
        else:
            break
    return list_names

#print(movies['cast'].apply(convert_cast))

movies['cast'] = movies['cast'].apply(convert_cast)

def fetch_director(obj):
    list_name = []
    for i in ast.literal_eval(obj):
        if i['job'] == 'Director':
            list_name.append(i['name'])
            break
    return list_name

movies['crew'] = movies['crew'].apply(fetch_director)


#converted the overview of the movies to a list 
movies['overview'] = movies['overview'].apply(lambda x:x.split())


# this function will remove spaces between words, making it easier for our model to search
def collapse(L):
    L1 = []
    for i in L:
        L1.append(i.replace(" ",""))
    return L1

movies['cast'] = movies['cast'].apply(collapse)
movies['crew'] = movies['crew'].apply(collapse)
movies['genres'] = movies['genres'].apply(collapse)
movies['keywords'] = movies['keywords'].apply(collapse)


# tags which will have the info related to a movie
movies['tags'] = movies['overview'] + movies['genres'] + movies['keywords'] + movies['cast'] + movies['crew']

# created a new data set for movies with just the required information and converting tags from list to string
new_data_movies = movies[['movie_id', 'title', 'tags']]
new_data_movies['tags'] = new_data_movies['tags'].apply(lambda x: " ".join(x))




