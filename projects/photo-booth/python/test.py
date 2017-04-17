import cv2
import time
import sys
import PIL
from PIL import Image
from PIL import ImageOps

# "0" is the port of your built-in webcam, probably.
camera_port = 0
# Number of frames to ramp-up the camera. 
ramp_frames = 30

# Note that you will want to keep the row/column count in line with the width
# and height values to maintain a sensible strip. i.e. One column looks good
# with strip_width = 300, but odd with a wider width.
strip_rows = 4
strip_columns = 2
strip_width = 600
strip_height = 900

# Determines the space in pixels between columns and rows.
row_gutter = 15
column_gutter = 10

# How long the script should count down before taking a picture in seconds.
wait_time = 3

# A silly list determining what columns should have a grayscale effect applied.
# Ideally this would be a map of common filters - sepiatone, soft focus, etc.
column_grayscale = (0, 1)

strip = Image.new('RGB', (strip_width, strip_height), (255,255,255))
camera = cv2.VideoCapture(camera_port)

# Takes a single picture from the current video capture device.
def get_image():
  retval, image = camera.read()
  image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
  image = Image.fromarray(image)
  return image

# Warm up the camera to make sure the lightning/focus adjusts.
print 'Warming up...'
for i in xrange(ramp_frames):
  temp = get_image()

# Determine a desired width/height for our frames based on common variables.
target_height = (strip_height - ((strip_rows + 1) * row_gutter)) / strip_rows
target_width = (strip_width - ((strip_columns - 1) * column_gutter)) / strip_columns

for row in xrange(strip_rows):
  # Wait for our users to pose. Wait time doesn't account for execution time 
  # because I'm lazy.
  for i in xrange(wait_time):
    print '%s...' % (wait_time - i)
    time.sleep(1)
  print 'Smile!'
  time.sleep(.5)
  
  # Grab an image from the webcam.
  image = get_image()
  
  # Scale/crop the image to fit our desired width/height.
  image = ImageOps.fit(image, (target_width, target_height), PIL.Image.LANCZOS)
  
  y = (row * target_height) + ((row+1) * row_gutter)
  
  for column in xrange(strip_columns):
    x = (column * target_width) + (column * column_gutter)
    # Check if this column should be grayscaled.
    if column_grayscale[column]:
      strip.paste(ImageOps.grayscale(image), (x, y))
    else:
      strip.paste(image, (x, y))

# Show the strip to the user, this is where you'd put print/save code as well.
strip.show();

# Make sure our camera connection is closed.
del(camera)