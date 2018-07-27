import numpy as np 
from sklearn.datasets import load_iris 
from numpy import array

iris 	= load_iris()

X 		= iris.data 	# features
Y 		= iris.target 	# labels 

#print("X")
#print(X)
#print("Y")
#print(Y)


# split into train/test 
from sklearn.cross_validation import train_test_split 
X_train, X_test, Y_train, Y_test 	= train_test_split(X,Y,test_size=.5)

# train a classifier
def train(classifier,features,labels):
	return classifier.fit(features,labels)

# predict labels for unseen data
def predict(classifier,features):
	return classifier.predict(features)

from sklearn.neighbors import KNeighborsClassifier
classifier 	= KNeighborsClassifier(n_neighbors=1)



X_train 	= array([[30, 1, 1, 18, 18], [5, 0, 1, 18, 18], [31, 1, 1, 12, 6]])
Y_train 	= array([[1, 0, 1]])
X_test 		= array([[10, 1, 1, 13, 17]])


print("X_train")
print(X_train)
print("Y_train")
print(Y_train)


# train
classifier 	= train(classifier,X_train,Y_train)

# predict
predictions = predict(classifier,X_test)

# calculate accuracy
from sklearn.metrics import accuracy_score
accuracy 	= accuracy_score(Y_test,predictions)

print(accuracy)