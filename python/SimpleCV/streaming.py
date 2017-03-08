from SimpleCV import Camera, JpegStreamer
import time

c 	= Camera()
js 	= JpegStreamer("192.168.1.79:80")  #starts up an http server (defaults to port 8080)

while True:
	c.getImage().save(js)
	time.sleep(0.1)
