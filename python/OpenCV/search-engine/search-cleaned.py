# example usage: python2.7 search-cleaned.py -d ~/Desktop/photos/ -q ~/Desktop/photos/2014-11-22\ 17.19.30.jpg
# import the necessary packages
from RGBHistogram import RGBHistogram
from Searcher import Searcher
import numpy as np
import argparse
import cPickle
import cv2
import glob
 
# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-d", "--dataset", required = True,
	help = "Path to the directory that contains the images to index (and search)")
ap.add_argument("-q", "--query", required = True,
	help = "Path to query image")
args = vars(ap.parse_args())

'''
# initialize the index dictionary to store our our quantifed
# images, with the 'key' of the dictionary being the image
# filename and the 'value' our computed features
index = {}

# initialize our image descriptor -- a 3D RGB histogram with
# 8 bins per channel
desc = RGBHistogram([8, 8, 8])

# use glob to grab the image paths and loop over them
for imagePath in glob.glob(args["dataset"] + "/*.jpg"):

	# extract our unique image ID (i.e. the filename)
	k = imagePath[imagePath.rfind("/") + 1:]
 
	# load the image, describe it using our RGB histogram
	# descriptor, and update the index
	image = cv2.imread(imagePath)
	features = desc.describe(image)
	index[k] = features

'''
# grab index from file (the reason why the above section is commented out)
index 	= cPickle.loads(open('index.txt').read())

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
for j in xrange(0,5):
	(score, imageName) = results[j]
	cv2.imshow('Score: %s' % score,cv2.resize(cv2.imread(args['dataset'] + imageName),(300,250)))

cv2.waitKey(0)






