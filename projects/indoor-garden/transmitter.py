import RPi.GPIO as GPIO
from lib_nrf24 import NRF24 
import time
import spidev
import json

class radio:
	def __init__(self):
		GPIO.setwarnings(False)
		GPIO.setmode(GPIO.BCM)

		self.pipes 	= [
			[0xe7,0xe7,0xe7,0xe7,0xe7],
			[0xc2,0xc2,0xc2,0xc2,0xc2]
		]

		self.radio 	= NRF24(GPIO,spidev.SpiDev())
		self.radio.begin(0,17)	# address/pin?
		self.radio.setPayloadSize(32)
		self.radio.setChannel(0x60)

		self.radio.setDataRate(NRF24.BR_2MBPS)
		self.radio.setPALevel(NRF24.PA_MIN)
		self.radio.setAutoAck(True)
		self.radio.enableDynamicPayloads()
		self.radio.enableAckPayload()

		# radio.openReadingPipe(1,pipes[1])
		self.radio.openWritingPipe(self.pipes[1])
		self.radio.printDetails()

	def send(string):
		self.radio.write(list(str(string)))
		if radio.isAckPayloadAvailable():
			payload 	= []
			self.radio.read(payload,self.radio.getDynamicPayloadSize())
			return {'success': True,'payload': payload}
		else:
			return {'success': True,'payload': 0}

	def disable():
		self.radio.flush_rx()
		self.radio.flush_tx()
		self.radio.end()
		GPIO.cleanup()




