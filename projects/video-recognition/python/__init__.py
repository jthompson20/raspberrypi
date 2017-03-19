# import the necessary packages
from __future__ import print_function
from Recognize import Face
from imutils.video import WebcamVideoStream
import imutils
import cv2
import sys

WRITE_TO_DISK 	= True

cascPath 	= '/Applications/XAMPP/htdocs/raspberrypi-travis/python/OpenCV/haar/face.xml' #sys.argv[1]
faceCascade = cv2.CascadeClassifier(cascPath)

# created a *threaded* video stream, allow the camera sensor to warmup,
vs = WebcamVideoStream(src=0).start()

# loop over some frames...this time using the threaded stream
cnt 	= 0
while True:
	cnt+=1
	# grab the frame from the threaded video stream and resize it
	# to have a maximum width of 400 pixels
	frame = vs.read()
	frame = imutils.resize(frame, width=600)

	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	faces = faceCascade.detectMultiScale(
		gray,
		scaleFactor=1.1,
		minNeighbors=5,
		minSize=(30, 30),
		flags=cv2.cv.CV_HAAR_SCALE_IMAGE
	)

	# Draw a rectangle around the faces
	for (x, y, w, h) in faces:
		cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

		# perform facial recognition
		# initialize recognition library
		recognition 	= Face()
		# crop the image around the face
		cropped 		= frame[y:y+h,x:x+w]
		# write frame to file so that we can read
		# TODO: make this so that we dont have to write a file (just run algorithm against frame)
		cv2.imwrite('/Applications/XAMPP/htdocs/raspberrypi-travis/projects/video-recognition/python/cropped.png',cropped)
		# run recognition algorithm to detect person
		recognition.person('/Applications/XAMPP/htdocs/raspberrypi-travis/projects/video-recognition/python/cropped.png')
		cv2.putText(frame,recognition.prediction['person'],(x,y), cv2.FONT_HERSHEY_SIMPLEX, 1,(255,255,255),2)

		# should we write this image to this person's library?
		#if WRITE_TO_DISK and recognition.prediction['score'] < 0.10:
		#	path_to_file 	= '/Applications/XAMPP/htdocs/raspberrypi-travis/python/OpenCV/search-engine/img/people/%s/%d-%d-%d-%d.png' % (recognition.prediction['person'],x,y,w,h)
		#	cv2.imwrite(path_to_file,cropped)

		if WRITE_TO_DISK and recognition.prediction['person'] == 'unknown':
			path_to_file 	= '/Users/mattthompson/Desktop/photos/people/%s/%d-%d-%d-%d.png' % (recognition.prediction['person'],x,y,w,h)
			cv2.imwrite(path_to_file,cropped)

	## TODO: take image of JUST the face (within rectangle)
	# run algorithm against this image, instead of just against the entire video frame


	# Display the resulting frame
	cv2.imshow('Video', frame)

	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
 
# do a bit of cleanup
cv2.destroyAllWindows()
vs.stop()









