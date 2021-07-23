import pandas as pd

#reading of dataset
messages=pd.read_csv('C:/Users/archi/Downloads/smsspamcollection/SMSSpamCollection',sep="\t",names=["label","message"])




import re
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer


ps = PorterStemmer()
corpus = []
for i in range(len(messages)):
    review = re.sub('[^a-zA-Z]', ' ', messages['message'][i]) #remove all except a-z and A-Z
    review = review.lower() #lowercasing all letters
    review = review.split() #splitting up sentences to words
    review = [ps.stem(word) for word in review if not word in set(stopwords.words('english'))]  #stemming
    review = ' '.join(review)
    corpus.append(review)
    
# Creating the Bag of Words model
from sklearn.feature_extraction.text import CountVectorizer
cv=CountVectorizer(max_features=4500) #max_features means tp 1500 models of dataset
X = cv.fit_transform(corpus).toarray()
#if 1 comes up in the X, 1 depicts that at that row number the particular word was present.

y=pd.get_dummies(messages['label']) #getting dummies of the dataset
y=y.iloc[:,1].values #merging up columns and showing up on the basis of data0 and 1

from sklearn.model_selection import train_test_split  #splitting of dataset into test and training dataset
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.20,random_state=0) #splitups into 80% test and 20% train


from sklearn.naive_bayes import MultinomialNB   #naive bayes classification algorithm is used
spam_model=MultinomialNB().fit(X_train,y_train) 


pred=spam_model.predict(X_test)  #further predictions for test the dependent features

#finding exact predicts of y_train and prediction on y
from sklearn.metrics import confusion_matrix
mconf=confusion_matrix(y_test,pred)

#finding accuracy
from sklearn.metrics import accuracy_score
accuracy=accuracy_score(y_test,pred)


