from SimpleCV import Display, Image, Camera

display = Display()

# Loop until window is closed
while not display.isDone():



	# Look for a face
	faces = img.findHaarFeatures('face')
	if faces is not None:
	# Draw a box around the face
	faces.draw()
	# Say how many faces were found
	print ‘%s faces detected” % len(faces)
	img.save(display)