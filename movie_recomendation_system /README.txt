Recomended Systems 
    1. Content-based -> Tags
    2. Collaborating-filtering 
        recomending content based on user similarities
            if A and B both like movie C
                Then A likes movie D
                we can recomend Movie D to B as well
    3. Hybrid
        content-based + collaboarting filtering 


SYSTEM USED:
    Content-based recomending system

PROJECT FLOW:
    1. Data
        pre-processing
            getting data ready for our purpose 
    2. Model building
        machine learning model 

    3. Website 
    4. deployement

DATA SET
    TMDB 5000 movie set


SIMILARITY SCORE 
    1. Vecterization 
       a. convert the tags into vectors 
       b. If a person choses a movie A then the reconmended movie will be the closest vector to the vector of movie A.
    2. Need to do text vecterization 
        convert text to vectors 
    3. famous techniques 
        1. bag of words 
        2. word2vec
        3. tfidf
    4. Technique used 
        1. bag of words 
            1. combine all the tags 
            2. find the most common word in them 
            3. lets say there a 5 most common words 
                1. then we will check how many times each of those 5 words occured in the tags of each movie 
                2.    w1  w2  w3  w4  w5
                   m1 5   0   2    3  1
                   m2 1   3   1   3   5 
                   m3 5   3   2   7   6
                   m4 1   0   0   3   0
                   m5 2   4   4   1   5 

                   Now this is the vector in 5d space 
                   the numbers being the co-ordinates of the movie 
                   let say i chose movie m3
                        then i will find the closest vectors to m3 and reconmend those movies

            4. One thing to do 
                1. Do not consider stop words 
                    words that dont contribute to the sentance
                    for example 
                            are, to, for , and, from 
            
            5. Calculate distance between the vectors using cosine distance instead of euclidian distacne 
                euclidian distance fails in higher dimmensions.
