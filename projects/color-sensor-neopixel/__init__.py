import smbus
import time
import WS281X

bus 	= smbus.SMBus(1)
rgb 	= WS281X.WS281X(18)

# I2C address 0x29
# Register 0x12 has device ver. 
# Register addresses must be OR'ed with 0x80
bus.write_byte(0x29,0x80|0x12)
ver = bus.read_byte(0x29)

# version # should be 0x44
if ver == 0x44:
	print "Device found\n"
	bus.write_byte(0x29, 0x80|0x00) # 0x00 = ENABLE register
	bus.write_byte(0x29, 0x01|0x02) # 0x01 = Power on, 0x02 RGB sensors enabled
	bus.write_byte(0x29, 0x80|0x14) # Reading results start register 14, LSB then MSB

	try:
		while True:
			# read data
			data = bus.read_i2c_block_data(0x29, 0)

			# grab RGB & Clear values
			clear = clear = data[1] << 8 | data[0]
			red = data[3] << 8 | data[2]
			green = data[5] << 8 | data[4]
			blue = data[7] << 8 | data[6]

			# print results
			crgb = "C: %s, R: %s, G: %s, B: %s\n" % (clear, red, green, blue)
			print crgb

			# update RGB
			rgb.update(red,green,blue,clear)
			
			# RGBC ADC wait time (see datasheet: https://cdn-shop.adafruit.com/datasheets/TCS34725.pdf)
			time.sleep(.44)

	except KeyboardInterrupt:
		pass
	except Exception as e:
		print(e)
	finally:
		# turn rgb OFF
		rgb.update(0,0,0,0)
		rgb.disable()


else: 
	print "Device not found\n"






