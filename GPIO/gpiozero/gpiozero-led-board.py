# control an entire board of LEDs
from gpiozero import LEDBoard
import time

leds 	= LEDBoard(2,3,4,5,6)

leds.on()
time.sleep(1)
leds.off()
time.sleep(1)
leds.toggle()
time.sleep(1)
leds.toggle()
time.sleep(1)
leds.blink()
pause()