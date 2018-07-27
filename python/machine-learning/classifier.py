# this is an example K Nearest Neighbors Classifier
# https://www.youtube.com/watch?v=AoeEHqVSNOw
from scipy.spatial import distance

class MyClassifier():
	
	def fit(self,features,labels):
		self.features 	= features
		self.labels 	= labels

	def predict(self,features):
		predictions 	= []
		for row in features:
			# measure distance between two points (Euclidean Distance) - a2 + b2 = c2
			########################
			#
			# 				|\
			#  b = (y2-y1) 	| \
			# 				|  \
			# 				|___\
			# 			a = (x2 - x1)
			#
			# The distance that we compute is the length of the hypotenuse
			# d(a,b) = sqrt of (x2-x1)2 + (y2-y1)2 + .. + (n2-n1)2

			# find closest training point to the test point
			label 	= self.closest(row)

			predictions.append(label)
		return predictions

	def closest(self,row):
		best_distance 	= self.distance(row,self.features[0])
		best_index 		= 0
		for i in range(1,len(self.features)):
			distance 	= self.distance(row,self.features[i])
			if distance < best_distance:
				best_distance 	= distance
				best_index 		= i
		# return label for closest distance in training data
		return self.labels[best_index]

	# determine distance using Euclidean Distance
	def distance(self,training_data_point,testing_data_point):
		return distance.euclidean(training_data_point,testing_data_point)

import numpy as np 
from sklearn.datasets import load_iris 

iris 	= load_iris()

X 		= iris.data 	# features
Y 		= iris.target 	# labels 

# split into train/test 
from sklearn.cross_validation import train_test_split 
X_train, X_test, Y_train, Y_test 	= train_test_split(X,Y,test_size=.5)

#from sklearn.neighbors import KNeighborsClassifier
#classifier 	= KNeighborsClassifier(n_neighbors=1)
classifier 		= MyClassifier()

# train
classifier.fit(X_train,Y_train)

# predict
predictions = classifier.predict(X_test)

# calculate accuracy
from sklearn.metrics import accuracy_score
accuracy 	= accuracy_score(Y_test,predictions)

print(accuracy)