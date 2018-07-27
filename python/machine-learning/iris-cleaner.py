import numpy as np 
from sklearn.datasets import load_iris 

iris 	= load_iris()

X 		= iris.data 	# features
Y 		= iris.target 	# labels 

# split into train/test 
from sklearn.cross_validation import train_test_split 
X_train, X_test, Y_train, Y_test 	= train_test_split(X,Y,test_size=.5)

# train a classifier
def train(classifier,features,labels):
	return classifier.fit(features,labels)

# predict labels for unseen data
def predict(classifier,features):
	return classifier.predict(features)

from sklearn import tree
classifier 	= tree.DecisionTreeClassifier()

# train
classifier 	= train(classifier,X_train,Y_train)

# predict
predictions = predict(classifier,X_test)

# calculate accuracy
from sklearn.metrics import accuracy_score
accuracy 	= accuracy_score(Y_test,predictions)

print(accuracy)