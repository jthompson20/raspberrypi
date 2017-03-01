# http://invent.module143.com/daskal_tutorial/rpi-3-tutorial-13-wireless-pi-to-pi-python-communication-with-nrf24l01/
import RPi.GPIO as GPIO
from lib_nrf24 import NRF24 
import time
import spidev

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

pipes 	= [
	[0xe7,0xe7,0xe7,0xe7,0xe7],
	[0xc2,0xc2,0xc2,0xc2,0xc2]
]

radio 	= NRF24(GPIO,spidev.SpiDev())
radio.begin(0,17)	# address/pin?
radio.setPayloadSize(32)
radio.setChannel(0x60)

radio.setDataRate(NRF24.BR_2MBPS)
radio.setPALevel(NRF24.PA_MIN)
radio.setAutoAck(True)
radio.enableDynamicPayloads()
radio.enableAckPayload()

radio.openReadingPipe(0,pipes[1])
radio.printDetails()

radio.startListening()

try:
	while True:
		ackPL 	= [1]
		while not radio.available(0):
			time.sleep(1/100)
		receivedMessage 	= []
		radio.read(receivedMessage,radio.getDynamicPayloadSize())
		print "Received: {}".format(receivedMessage)

		print "Translating the receivedMessage into unicode characters"
		string 	= ""
		for n in receivedMessage:
			# decode into standard unicode set
			if (n &gt;= 32 and n &lt;= 126):
				string += chr(n)
		print string
		radio.writeAckPayload(1,ackPL,len(ackPL))
		print "Loaded payload reply of {}".format(ackPL)
except KeyboardInterrupt:
	print 'keyboard interruption'
except:
	print 'caught exception'
finally:
	GPIO.cleanup()




