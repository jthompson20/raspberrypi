from gpiozero import RGBLED
import time

rgb 	= RGBLED(2,3,4)

rgb.on()
time.sleep(1)
rgb.off()
time.sleep(1)
rgb.toggle()
time.sleep(1)
rgb.toggle()
time.sleep(1)
rgb.color(1,0.5,1)
time.sleep(1)
rgb.pulse()
time.sleep(5)

for n in range(100):
    rgb.red = n/100
    sleep(0.1)

for n in range(100):
    rgb.blue = n/100
    sleep(0.1)

for n in range(100):
    rgb.green = n/100
    sleep(0.1)
