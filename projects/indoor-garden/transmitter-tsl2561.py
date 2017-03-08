from transmitter import radio
from TSL2561 import TSL2561
import time

# initialize libs
transmitter 	= radio()
sensor 	 		= TSL2561()

try:
	while True:

		# get data
		data 		= {
			'sensor': 	'TSL2561',
			'type': 	'light',
			'lux': 		sensor.readLux(1)
		}

		# send data
		response 	= transmitter.send(data)

		# show response
		print response
		time.sleep(1)

except KeyboardInterrupt:
	print 'keyboard interruption'
except Exception as e:
	print 'caught exception'
	print e
finally:
	transmitter.disable()