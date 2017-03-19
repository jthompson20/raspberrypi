# example usage: python2.7 recognize.py -d ~/Desktop/photos/ -q ~/Desktop/photos/2014-11-22\ 17.19.30.jpg
# import the necessary packages
from RGBHistogram import RGBHistogram
from Searcher import Searcher
import numpy as np
import argparse
import cPickle
import cv2
import glob
 
# constants
PEOPLE_IMAGES 	= 'img/people'
PEOPLE 			= [
	#'matt',
	'jess',
	'maci',
	'lily',
	#'paula',
	'grandma-fran',
	'grandpa-jim',
	'jeff',
	'jimmy',
	'miranda'
]

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-q", "--query", required = True, help = "Path to query image")
args = vars(ap.parse_args())

# grab index from file (the reason why the above section is commented out)
# prediction
lowscore 	= 1.5
prediction 	= {
	'score': 	0.0,
	'person': 	'nobody',
	'image': 	'img/example_test.png'
}
for person in PEOPLE:
	index 	= cPickle.loads(open(PEOPLE_IMAGES + '/' + person + '/' + person + '.txt').read())

	# SEARCH
	# load the query image and show it
	queryImage = cv2.imread(args["query"])
	cv2.imshow("Original Query:", cv2.resize(queryImage,(300,250)))

	# describe the query in the same way that we did in
	# index.py -- a 3D RGB histogram with 8 bins per
	# channel
	desc_results  	= RGBHistogram([8, 8, 8])
	queryFeatures  	= desc_results.describe(queryImage)

	# load the index perform the search
	#index_results  	= cPickle.loads(cPickle.dumps(index)).read())
	searcher  		= Searcher(index)
	results  		= searcher.search(queryFeatures)

	# show top 5 results
	for j in xrange(0,1):
		(score, imageName) = results[j]

		# see if this beats any others
		if score < lowscore:
			lowscore 	= score
			prediction 	= {
				'score': 	score,
				'person': 	person,
				'image': 	PEOPLE_IMAGES + '/' + person + '/' + imageName
			}
		#cv2.imshow('Score: %s' % score,cv2.resize(cv2.imread(args['dataset'] + imageName),(300,250)))


print(prediction)
cv2.waitKey(0)






