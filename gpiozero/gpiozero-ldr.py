#http://gpiozero.readthedocs.io/en/v1.3.1/api_input.html#gpiozero.LightSensor
from gpiozero import LED, LightSensor
from signal import pause

led 	= LED(17)
ldr 	= LightSensor(18)

ldr.when_light 	= led.on
ldr.when_dark 	= led.off

pause()