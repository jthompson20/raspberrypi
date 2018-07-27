import numpy as np 
from sklearn.datasets import load_iris 
from sklearn import tree 

# load iris example from sklearn
iris 		= load_iris()

# ids to remove for testing
test_ids 	= [0,50,100]

# training data
train_target 	= np.delete(iris.target,test_ids)
train_data 		= np.delete(iris.data,test_ids,axis=0)

# testing data 
test_target 	= iris.target[test_ids]
test_data 		= iris.data[test_ids]

# init classifier
classifier 		= tree.DecisionTreeClassifier()
classifier.fit(train_data,train_target)

# predict
print(test_target)
print(classifier.predict(test_data))