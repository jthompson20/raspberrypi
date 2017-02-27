import RPi.GPIO as GPIO  
import time

# initialize varaiables
pins 	= {
	'led': 	16,
	'pir':	15
}

# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

# setup pin types
GPIO.setup(pins['led'],GPIO.OUT)
GPIO.setup(pins['pir'],GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

try:
	while True:
		motion 	= GPIO.input(pins['pir'])
		if motion:
			print 'motion detected'
			GPIO.output(pins['led'],1)
			time.sleep(1)
		else:
			print 'no motion detected'
			GPIO.output(pins['led'],0)
			time.sleep(1)
except KeyboardInterrupt:
	print 'keyboard interruption'
except:
	print 'exception caught'
finally:
	GPIO.cleanup()