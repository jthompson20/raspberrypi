from SimpleCV import Camera, JpegStreamer
import time

c 	= Camera()
js 	= JpegStreamer("0.0.0.0:8080")  #starts up an http server (defaults to port 8080)

while True:
	c.getImage().save(js)
	time.sleep(0.1)
