
#importing needed libraries
import numpy as np
import pandas as pd
import itertools
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import PassiveAggressiveClassifier
from sklearn.metrics import accuracy_score, confusion_matrix


#importing data
#Read the data
df=pd.read_csv('C:\\Users\\Antti\\Desktop\\Demo\\news.csv')

#Get shape and head
df.shape
df.head()


#Get labels for dataframe
labels=df.label
labels.head()

##Test print to check that table (6335 x 4) was read in correctly
#print (df)


#Splitting data into training and testing datasets (original input values 0.2 and 7)
x_train,x_test,y_train,y_test=train_test_split(df['text'], labels, test_size=0.33333, random_state=7)


##Initialize a TfidfVectorizer 
#(max_df = maximum document frequency of 0.7 (terms with a higher document frequency will be discarded))
tfidf_vectorizer=TfidfVectorizer(stop_words='english', max_df=0.7)

#Fit and transform the vectorizer on the train set and transform the vectorizer on the test set
tfidf_train=tfidf_vectorizer.fit_transform(x_train) 
tfidf_test=tfidf_vectorizer.transform(x_test)


#Initialize a PassiveAggressiveClassifier (and fit this on tfidf_train and y_train)
pac=PassiveAggressiveClassifier(max_iter=50)
pac.fit(tfidf_train,y_train)

#Predict on the test set from the TfidfVectorizer 
#calculate the accuracy with accuracy_score() from sklearn.metrics 
y_pred=pac.predict(tfidf_test)
score=accuracy_score(y_test,y_pred)
print(f'Accuracy: {round(score*100,2)}%')

#Build confusion matrix
array = confusion_matrix(y_test,y_pred, labels=['FAKE','REAL'])
print(f'confusion_matrix: {array}')
