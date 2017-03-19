# import libs
from PhotoBooth import Button
from PhotoBooth import Camera

# initialize our classes
button 	= PhotoBooth.Button()
camera 	= PhotoBooth.Camera()

# run infinite loop
while True:

	# determine if any buttons were pressed
	if button.pressed == 'photobooth':
		# run custom methods for each button (i.e. take pictures)
		camera.photobooth()

	if button.pressed == 'recording':
		camera.recording()

	if button.pressed == 'shutdown':
		camera.shutdown()
		break
