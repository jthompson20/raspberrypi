#http://gpiozero.readthedocs.io/en/v1.3.1/api_input.html#motion-sensor-d-sun-pir
from gpiozero import LED, MotionSensor
from signal import pause

led 	= LED(17)
pir 	= MotionSensor(15)

pir.when_motion 		= led.on
pir.when_no_motion		= led.off

pause()