from SimpleCV import Camera
# Initialize the camera
cam = Camera()
# Loop to continuously get images
while True:
	# Get Image from camera
	img = cam.getImage()
	img = img.edges()    
	img.show()    
	time.sleep(5)

	# show binary
	img = img.binarize()  
	img.show()  
	time.sleep(5)    

	# find blobs
	img = img.findBlobs()  
	for blob in blobs:  
	    blob.draw()  
	img.show()  
	time.sleep(5) 
