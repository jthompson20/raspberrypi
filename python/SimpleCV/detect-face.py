from SimpleCV import Display, Image, Camera

#initialize the camera
cam 	= Camera()
display = Display()

# Loop until window is closed
while not display.isDone():

	# Get image, flip it so it looks mirrored, scale to speed things up
	img = cam.getImage().flipHorizontal().scale(0.5)
	# Look for a face
	faces = img.findHaarFeatures('face.xml')
	if faces is not None:
		# Draw a box around the face
		faces.draw()
		# Say how many faces were found

	print "%s faces detected" % len(faces)
	img.save(display)
