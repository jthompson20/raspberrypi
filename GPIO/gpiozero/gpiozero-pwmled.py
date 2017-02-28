from gpiozero import PWMLED
import time

led 	= PWMLED(2,3,4)

led.on()
time.sleep(1)
led.off()
time.sleep(1)
led.toggle()
time.sleep(1)
led.toggle()
time.sleep(1)
led.pulse()
time.sleep(5)

for n in range(100):
	led.value 	= n/100
	time.sleep(1)

