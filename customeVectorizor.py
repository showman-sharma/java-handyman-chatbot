import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from sklearn import preprocessing
import numpy as np



from sklearn.feature_extraction.text import TfidfVectorizer

#Build a TF-IDF Vectorizer model

#Custom tokenizer to remove stopwords and use lemmatization
lemmatizer = WordNetLemmatizer()
def customtokenize(str):
            #Split string as tokens
            tokens=nltk.word_tokenize(str)
            #Filter for stopwords
            nostop = list(filter(lambda token: token not in stopwords.words('english'), tokens))
            #Perform lemmatization
            
            lemmatized=[lemmatizer.lemmatize(word) for word in nostop ]
            return lemmatized

# vectorizer = TfidfVectorizer(tokenizer=customtokenize)

class customVect(TfidfVectorizer):
    def __init__():
        customVect.tokenizer = customtokenize;
