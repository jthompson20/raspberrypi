# example usage: python2.7 recognize.py -d ~/Desktop/photos/ -q ~/Desktop/photos/2014-11-22\ 17.19.30.jpg
# import the necessary packages
from RGBHistogram import RGBHistogram
from Searcher import Searcher
import numpy as np
import argparse
import cPickle
import cv2
import glob
import sys

## VARIABLE CONSTANTS
HIGH_SCORE 		= 0.5 	# highest score to be deemed as "recognized" (0 is lowest)
PEOPLE_PATH 	= '/Users/mattthompson/Desktop/photos/people'
PEOPLE 			= [
	'matt',
	'jess',
	'maci',
	'lily',
	'paula',
	'grandma-fran',
	'grandpa-jim',
	'jeff',
	'jimmy',
	'miranda'
]

class Face:
	def __init__(self):
		self.path 			= PEOPLE_PATH
		self.tracker 		= HIGH_SCORE  	# defaults the tracker to the highest score allowed
		self.recognized 	= []
		self.prediction 	= {
			'score': 		0.0,
			'person': 		'unknown',
			'image': 		'unknown.png'
		}

	def clear(self):
		self.__init__

	def person(self,img):

		# iterate all people we're looking for
		for ppl in PEOPLE:

			person_path = self.path + '/' + ppl + '/' + ppl + '.txt'

			# grab our index of blobs for this person
			index 		= cPickle.loads(open(person_path).read())

			# query the new image
			query 		= cv2.imread(img)

			if query != None:
				# describe the query in the same way that we did in
				# index.py -- a 3D RGB histogram with 8 bins per
				# channel
				description  	= RGBHistogram([8, 8, 8])
				features  		= description.describe(query)
				# load the index perform the search
				#index_results  	= cPickle.loads(cPickle.dumps(index)).read())
				searcher  		= Searcher(index)
				results  		= searcher.search(features)

				resultDict 		= dict(results)

				# iterate the top 3 results
				for key in resultDict:
					# grab our variables
					score 		= key
					imgurl 		= resultDict[key]
					#(score,img) = results[i]
					# make sure the score is below our highscore
					if score <= HIGH_SCORE:
						# add this to the recognized array
						self.recognized.append({'score': score, 'person': ppl, 'img': imgurl})
						# check to see if this score is our lowest score yet
						if score < self.tracker:
							self.tracker 	= score
							self.prediction = {'score': score, 'person': ppl, 'img': imgurl}
							print(self.prediction);





