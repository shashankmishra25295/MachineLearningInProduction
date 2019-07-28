import re
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns
import string
import nltk
import warnings 
import nltk
nltk.download('punkt')
from nltk.tokenize import sent_tokenize, word_tokenize, TreebankWordTokenizer
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
from nltk.tokenize import TreebankWordTokenizer
from collections import Counter
from wordcloud import WordCloud,ImageColorGenerator
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.multiclass import OneVsRestClassifier


class Training:
    
    def __init__(self):
        self.classifierObject=''
        
    @app.route('/twitterDataAnalysis')
    def trainingTheModel(self):
        df = pd.read_csv('train.csv')
        df = self.dataCleaning(df)
        tokenized_tweet = self.tokenizeTweet(df)
        df = self.tidyTweet(df,tokenized_tweet)
        X_train = self.applyCountVectorizer(df)
        y_train = df['sentiment']
        self.classifierObject = self.fittingModel(X_train,y_train)

          
    def dataCleaning(df):
        df['tidy_tweet'] = df['tweet'].str.replace("@[A-Za-z]*", "")
        df['tidy_tweet'] = df['tidy_tweet'].str.replace("{link}", " ")
        df['tidy_tweet'] = df['tidy_tweet'].str.replace("&[\w]*", "")
        df['tidy_tweet'] = df['tidy_tweet'].str.replace("[^a-zA-Z#]", " ")   
        return df
    
    def tokenizeTweet(df):
        tokenized_tweet = df['tidy_tweet'].astype('str').apply(lambda x: x.split())
        return tokenized_tweet
        
    
    def tidyTweet(df,tokenized_tweet):
        for i in range(len(tokenized_tweet)):
            tokenized_tweet[i] = ' '.join(tokenized_tweet[i])
        df['tidy_tweet'] = tokenized_tweet  
        return df
    
    def applyCountVectorizer(df):
        vectorizer_train = CountVectorizer(max_df=0.90, min_df=2, max_features=3926,stop_words='english')
        X_train = vectorizer_train.fit_transform(df['tidy_tweet'])
        return X_train
    
    def fittingModel(X_train,y_train):
        classifierObject = OneVsRestClassifier(RandomForestClassifier(random_state=0, n_jobs=-1))
        classifierObject.fit(X_train,y_train)
        return classifierObject
    
    @app.route('/predict',method='Post')
    def predict(self,data):
        self.classifierObject.predict(data)
        return self.classifierObject.score()
        
if __name__ =="__main__":
   app.run('localhost',port=5000) 