# import the necessary packages
from __future__ import print_function
from imutils.video import WebcamVideoStream
import imutils
import cv2

cascPath 	= 'haar/face.xml' #sys.argv[1]
faceCascade = cv2.CascadeClassifier(cascPath)

# created a *threaded* video stream, allow the camera sensor to warmup,
vs = WebcamVideoStream(src=0).start()
 
# loop over some frames...this time using the threaded stream
while True:
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

	# Display the resulting frame
	cv2.imshow('Video', frame)

	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
 
# do a bit of cleanup
cv2.destroyAllWindows()
vs.stop()









