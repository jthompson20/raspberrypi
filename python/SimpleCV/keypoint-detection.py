from SimpleCV import Image, Color, Display, Camera

# Initialize the camera
cam = Camera()
# Loop to continuously get images
while True:
    # Get Image from camera
    img = cam.getImage()
	# use a keypoint detector to find areas of interest
	feats = img.findKeypoints()
	# draw the list of keypoints
	feats.draw(color=Color.RED)
	# show the  resulting image. 
	img.show()