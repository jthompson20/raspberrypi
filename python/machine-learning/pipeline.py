from sklearn import datasets 
iris 	= datasets.load_iris()

X 		= iris.data  	# X = features = function input
Y 		= iris.target 	# Y = labels = function output

# split into train/test 
from sklearn.cross_validation import train_test_split 
X_train, X_test, Y_train, Y_test 	= train_test_split(X,Y,test_size=.5)

