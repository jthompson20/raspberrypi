from gpiozero import Motor
import time

motor = Motor(forward=17, backward=18)

while True:
	motor.forward()
	time.sleep(5)
	motor.backward()
	time.sleep(5)