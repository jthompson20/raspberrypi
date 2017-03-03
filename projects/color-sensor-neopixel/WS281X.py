import time
import _rpi_ws281x as ws

# LED configuration.
LED_CHANNEL    = 0
LED_COUNT      = 1         	# How many LEDs to light.
LED_FREQ_HZ    = 800000     # Frequency of the LED signal.  Should be 800khz or 400khz.
LED_DMA_NUM    = 5          # DMA channel to use, can be 0-14.
LED_GPIO       = 18         # GPIO connected to the LED signal line.  Must support PWM!
LED_BRIGHTNESS = 30        	# Set to 0 for darkest and 255 for brightest
LED_INVERT     = 0          # Set to 1 to invert the LED signal, good if using NPN
							# transistor as a 3.3V->5V level converter.  Keep at 0
							# for a normal/non-inverted signal.

# Define colors which will be used by the example.  Each color is an unsigned
# 32-bit value where the lower 24 bits define the red, green, blue data (each
# being 8 bits long).
DOT_COLORS = [  0x200000,   # red
				0x201000,   # orange
				0x202000,   # yellow
				0x002000,   # green
				0x002020,   # lightblue
				0x000020,   # blue
				0x100010,   # purple
				0x200010 ]  # pink

def Color(red, green, blue, white = 0):
	"""Convert the provided red, green, blue color to a 24-bit color value.
	Each color component should be a value 0-255 where 0 is the lowest intensity
	and 255 is the highest intensity.
	"""
	return (white << 24) | (red << 16)| (green << 8) | blue

class WS281X(object):
	def __init__(self,gpio):
		if gpio:
			LED_GPIO 	= gpio

		# Create a ws2811_t structure from the LED configuration.
		# Note that this structure will be created on the heap so you need to be careful
		# that you delete its memory by calling delete_ws2811_t when it's not needed.
		self.leds = ws.new_ws2811_t()

		# Initialize all channels to off
		for channum in range(2):
		    channel = ws.ws2811_channel_get(self.leds, channum)
		    ws.ws2811_channel_t_count_set(channel, 0)
		    ws.ws2811_channel_t_gpionum_set(channel, 0)
		    ws.ws2811_channel_t_invert_set(channel, 0)
		    ws.ws2811_channel_t_brightness_set(channel, 0)

		self.channel = ws.ws2811_channel_get(self.leds, LED_CHANNEL)

		ws.ws2811_channel_t_count_set(self.channel, LED_COUNT)
		ws.ws2811_channel_t_gpionum_set(self.channel, LED_GPIO)
		ws.ws2811_channel_t_invert_set(self.channel, LED_INVERT)
		ws.ws2811_channel_t_brightness_set(self.channel, LED_BRIGHTNESS)

		ws.ws2811_t_freq_set(self.leds, LED_FREQ_HZ)
		ws.ws2811_t_dmanum_set(self.leds, LED_DMA_NUM)

		# Initialize library with LED configuration.
		resp = ws.ws2811_init(self.leds)
		if resp != ws.WS2811_SUCCESS:
			message = ws.ws2811_get_return_t_str(resp)
			raise RuntimeError('ws2811_init failed with code {0} ({1})'.format(resp, message))

	def color(self,r,g,b,c=0):
		"""Convert the provided red, green, blue color to a 24-bit color value.
		Each color component should be a value 0-255 where 0 is the lowest intensity
		and 255 is the highest intensity.
		"""
		return (c << 24) | (r << 16)| (g << 8) | b

	def update(self,r,g,b,c):
		newcolor 	= Color(r,g,b)
		print "new color:"
		print newcolor
		print ""
		for i in range(LED_COUNT):
			# Set the LED color buffer value.
			ws.ws2811_led_set(self.channel, i, Color(r,g,b))

		# Send the LED color data to the hardware.
		resp = ws.ws2811_render(self.leds)
		if resp != ws.WS2811_SUCCESS:
			message = ws.ws2811_get_return_t_str(resp)
			raise RuntimeError('ws2811_render failed with code {0} ({1})'.format(resp, message))

		# Delay for a small period of time.
		time.sleep(0.25)

	def disable(self):
		# Ensure ws2811_fini is called before the program quits.
		ws.ws2811_fini(self.leds)
		# Example of calling delete function to clean up structure memory.  Isn't
		# strictly necessary at the end of the program execution here, but is good practice.
		ws.delete_ws2811_t(self.leds)

