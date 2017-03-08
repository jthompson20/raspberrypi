import time
c = Camera()
js = JpegStreamer()  #starts up an http server (defaults to port 8080)

while(1)
  c.getImage().save(js)
  time.sleep(0.1)