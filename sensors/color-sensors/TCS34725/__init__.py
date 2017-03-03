import time
import smbus
import TCS34725

tcs 	= TCS34725.TCS34725()

try:
	while True:
		# You can also override the I2C device address and/or bus with parameters:
		#tcs = Adafruit_TCS34725.TCS34725(address=0x30, busnum=2)

		# Or you can change the integration time and/or gain:
		#tcs = Adafruit_TCS34725.TCS34725(integration_time=Adafruit_TCS34725.TCS34725_INTEGRATIONTIME_700MS,
		#                                 gain=Adafruit_TCS34725.TCS34725_GAIN_60X)
		# Possible integration time values:
		#  - TCS34725_INTEGRATIONTIME_2_4MS  (2.4ms, default)
		#  - TCS34725_INTEGRATIONTIME_24MS
		#  - TCS34725_INTEGRATIONTIME_50MS
		#  - TCS34725_INTEGRATIONTIME_101MS
		#  - TCS34725_INTEGRATIONTIME_154MS
		#  - TCS34725_INTEGRATIONTIME_700MS
		# Possible gain values:
		#  - TCS34725_GAIN_1X
		#  - TCS34725_GAIN_4X
		#  - TCS34725_GAIN_16X
		#  - TCS34725_GAIN_60X

		# Disable interrupts (can enable them by passing true, see the set_interrupt_limits function too).
		tcs.set_interrupt(False)

		# Read the R, G, B, C color data.
		r, g, b, c = tcs.get_raw_data()

		# Calculate color temperature using utility functions.  You might also want to
		# check out the colormath library for much more complete/accurate color functions.
		color_temp = TCS34725.calculate_color_temperature(r, g, b)

		# Calculate lux with another utility function.
		lux = TCS34725.calculate_lux(r, g, b)

		# Print out the values.
		print('Color: red={0} green={1} blue={2} clear={3}'.format(r, g, b, c))

		# Print out color temperature.
		if color_temp is None:
		    print('Too dark to determine color temperature!')
		else:
		    print('Color Temperature: {0} K'.format(color_temp))

		# Print out the lux.
		print('Luminosity: {0} lux'.format(lux))

		# Print HEX
		print('#%02x%02x%02x' % (r,g,b))
		print('')
except KeyboardInterrupt:
	print('')
	print('ending loop..')
	print('')
except:
	print('caught exception')
	print('')
finally:
	# Enable interrupts and put the chip back to low power sleep/disabled.
	tcs.set_interrupt(True)
	tcs.disable()



