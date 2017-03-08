from SimpleCV import Image

img = Image('lenna')
img.show()
img.listHaarFeatures()
img.findHaarFeatures('haar/eye.xml').draw(color=Color.YELLOW)
