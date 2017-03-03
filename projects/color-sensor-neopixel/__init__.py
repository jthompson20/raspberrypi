import time
import smbus
import TCS34725	# color sensor
import WS281X	# neopixel

# initialize sensor
sensor 	= TCS34725.TCS34725()
rgb 	= WS281X.WS281X(18)

try:
	while True:
		# disbale interrupts
		sensor.set_interrupt(False)

		# Read the R, G, B, C color data.
		r, g, b, c = tcs.get_raw_data()

		# Calculate lux with another utility function.
		lux = TCS34725.calculate_lux(r, g, b)

		# if lux if within range, update RGB colors
		if lux > 50 and lux < 100:
			# update RGB
			rgb.update(r,g,b,c)

		time.sleep(1)

except KeyboardInterrupt:
	pass
except Exception as e:
	print(e)
finally:
	# Enable interrupts and put the chip back to low power sleep/disabled for color sensor.
	sensor.set_interrupt(True)
	sensor.disable()
	# disable the RGB
	rgb.disable()