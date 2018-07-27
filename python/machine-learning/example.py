from sklearn import tree

#####################################
# 	Weight (kg) 	Texture 	Label
# 	140 			Smooth 		Apple
# 	130 			Smooth 		Apple
# 	150 			Bumpy 		Orange
# 	170 			Bumpy 		Orange
#####################################

# init vars
features 	= [[140,1],[130,1],[150,0],[170,0]] 	# lbs, 0 = bumpy, 1 = smooth
labels 		= [0,0,1,1] 	# 0 = apple, 1 = orange

# train the algorithm
classifier 	= tree.DecisionTreeClassifier()
classifier 	= classifier.fit(features,labels)

# predict what 160kg + bumpy would be (expecting orage - i.e. 1)
print(classifier.predict([[160,0]]))