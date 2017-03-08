from transmitter import radio
import TSL2561
import time

transmitter 	= radio()
sensor 	 		= TSL2561.TSL2561()

try:
	while True:

		# create data dict to send to receiver
		data 		= {
			'sensor': 	'TSL2561',
			'type': 	'light',
			'lux': 		sensor.readLux(1)
		}

		# send data
		response 	= transmitter.send(json.dumps(data))

		print response
		time.sleep(1)

except KeyboardInterrupt:
	print 'keyboard interruption'
except Exception as e:
	print 'caught exception'
	print e
finally:
	transmitter.end()