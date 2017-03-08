from transmitter import radio
from TSL2561 import TSL2561
import time
import json

# initialize libs
transmitter 	= radio()
sensor 	 		= TSL2561()

try:
	while True:

		# calc lux
		lux 		= sensor.readLux(16)

		# get data
		data 		= {
			'sensor': 	'TSL2561',
			'type': 	'light',
			'lux': 		str(lux)
		}

		print data

		# convert data
		msg 	= json.dumps(data)
		binary 	= str(msg)
		message = list(binary)
		#print message

		# send data
		response 	= transmitter.send(list(str(lux)))

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