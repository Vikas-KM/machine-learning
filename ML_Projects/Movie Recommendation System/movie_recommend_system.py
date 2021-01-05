import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

df = pd.read_csv('./movie_metadata.csv')

df['genres'] = df['genres'].apply(lambda x: x.split('|'))
df['plot_keywords'].fillna(' ', inplace=True)


def listtostr(s):
    return ' '.join(map(str, s))

df['genres'] = df['genres'].apply(listtostr)

df['plot_keywords'] = df['plot_keywords'].apply(lambda x: x.split('|'))
df['plot_keywords'] = df['plot_keywords'].apply(listtostr)
df['movie_title'] = df['movie_title'].apply(lambda a:a[:-1])


df1 = df[['director_name','actor_2_name','genres', 'actor_1_name','movie_title','plot_keywords']].copy()

features = list(df1.columns)

for feature in features:
    df1[feature] = df1[feature].fillna('unknown')
    df1[feature] = df1[feature].apply(lambda x: x.lower())

def combine_features(row):
    return row['director_name']+' '+row['actor_2_name']+' '+row['genres']+' '+row['actor_1_name']+' '+row['movie_title']

df1['combined_features'] = df1.apply(combine_features, axis=1)

cv = CountVectorizer()
count_matrix = cv.fit_transform(df1["combined_features"]) 
cosine_sim = cosine_similarity(count_matrix)

def recommend(movie):
    movie = movie.lower()
    if movie not in df1['movie_title'].unique():
        return('Sorry! The movie you requested is not in our database. Please check the spelling or try with some other movies')
    else:
        i = df1.loc[df1['movie_title']==movie].index[0]
        lst = list(enumerate(cosine_sim[i]))
        lst = sorted(lst, key = lambda x:x[1] ,reverse=True)
        lst = lst[1:] # excluding self from the list
        l = []
        
        for i in range(len(lst)):
            a = lst[i][0]
            if df1['movie_title'][a] not in l: 
                l.append(df1['movie_title'][a])
                if len(l) == 10: # recommending 10 movies
                    break
        plt.bar(l, [i[1] for i in l])
        plt.xticks(rotation=90)
        plt.xlabel('similar movies to---> '+movie)
        plt.ylabel('cosine scores')
        plt.savefig('movies_recommended.jpg', bbox_inches='tight')
        return l


