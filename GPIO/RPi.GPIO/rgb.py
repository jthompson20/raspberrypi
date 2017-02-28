import RPi.GPIO as GPIO
import time
import sys

# init vars
pins 	= {
	'red': 		11,
	'green':	13,
	'blue': 	15
}
colors 	= {
	'red': 		{
		'red': 		'on',
		'green': 	'off',
		'blue': 	'off'
	},
	'blue': 	{
		'red': 		'off',
		'green': 	'off',
		'blue': 	'on'
	},
	'green': 	{
		'red': 		'off',
		'green': 	'on',
		'blue': 	'off'
	},
	'purple': 	{
		'red': 		'on',
		'green': 	'off',
		'blue': 	'on'
	},
	'off': 		{
		'red': 		'off',
		'green': 	'off',
		'blue': 	'off'	
	}
}

# setup GPIO pins
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

# make all pins output type
for pin in pins:
	GPIO.setup(pin,GPIO.OUT)

# method to switch to a specific color
def led(color='red'):
	try:
		colors[color]
	except NameError:
		print 'color doesnt exist'
		return

	for rgb,switch in enumerate(colors[color]):
		if switch == 'on':
			GPIO.output(pins[rgb],GPIO.HIGH)
		elif switch == 'off':
			GPIO.output(pins[rgb],GPIO.LOW)
	
	return

try:
	while True:
		cmd 	= raw_input('Choose a color (red, blue, green, purple):')
		led(cmd)
		time.sleep(5)
		led('off')
		time.sleep(1)

except KeyboardInterrupt:
	print 'keyboard interrupt'
except:
	print 'caught exception'
finally:
	GPIO.cleanup()








