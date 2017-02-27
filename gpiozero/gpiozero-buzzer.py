from gpiozero import Buzzer
import time

buzzer 	= Buzzer(14)

while True:
	buzzer.beep()
	time.sleep(5)
	buzzer.off()
	time.sleep(5)