import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from colorama import Fore ,Style
from textblob import TextBlob
import time
import sys
import colorama
colorama.init(autoreset=True)
def load_data(filepath='imdb_top_100.csv'):
    try:
        df=pd.read_csv(filepath)
        df['combined_features']=df['Genre'].fillna('')+''+df['overview'].fillna('')
        return df
    except FileNotFoundError:
        print("ERROR, FILE NOT FOUND{filepath}")
        exit()
movies_df=load_data()
tfidf=TfidfVectorizer(stop_words='english')
tfidf_matrix=tfidf.fit_transform(movies_df['combined_features'])
cosine_sim=cosine_similarity(tfidf_matrix,tfidf_matrix)