from SimpleCV import Image

img = Image('lenna')
img.show()
img.binarize().show()
img.toGray().show()
img.edges().show()
img.invert().show()