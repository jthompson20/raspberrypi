from SimpleCV import Image
import time

img = Image('lenna')

while True:
	img.show()
	time.sleep(3)
	img.binarize().show()
	time.sleep(3)
	img.toGray().show()
	time.sleep(3)
	img.edges().show()
	time.sleep(3)
	img.invert().show()
	time.sleep(3)