from __future__ import print_function
import threading
import datetime
import imutils
import cv2
import time
import os
import sys


class PhotoBooth:
	def __init__(self,webcam,output='snapshots/'):
		# instance of threaded webcam stream
		self.webcam 	= webcam
		self.output 	= output
		# initialize thread variables
		self.frame 		= None
		self.thread 	= None
		self.stopEvent 	= None
		# initialize other custom vars
		self.started 	= False 	# boolean to track whether we're already started a record or snapshot process

		'''
		# start thread that constantly pools the video sensor for most recently read frame
		self.stopEvent 	= threading.Event()
		self.thread 	= threading.Thread(target=self.loop, args=())
		self.thread.start()
		'''
	def start(self):
		# check to see if we are already running a start or record process
		if self.started:
			print('already started...')
			return

		print('starting...')
		self.started 	= True 	# mark that we've started running a process
		# create new "photobooth project" (i.e. collection of images)
		print('creating new project: Lillian\'s Birthday')
		# display countdown timer
		print('starating countdown timer...')
		self.countdown(5)
		self.snapshot()

		# repeat 
		for i in reversed(range(5)):
			print(i)
			time.sleep(1)

		# take snapshot
		print('taking snapshot...')
		self.started 	= False 	# mark that we've completed running a process

	def loop(self):
		# keep looping over frames until told to stop
		while True:
			# wait for specific keypress to trigger different methods
			if cv2.waitKey(1) & 0xFF == ord('s'):
				#booth.start()
				print('start booth')
				self.start()
				pass

			if cv2.waitKey(1) & 0xFF == ord('r'):
				#booth.record()
				print('recording')
				self.record()
				pass

			if cv2.waitKey(1) & 0xFF == ord('q'):
				#booth.shutdown()
				print('quitting')
				self.shutdown()
				pass

	def record(self):
		# check to see if we are already running a start or record process
		if self.started:
			print('already recording...')
			return

		print('recording...')
		self.started 	= True 		# mark that we've started running a process
		time.sleep(5)
		self.started 	= False 	# mark that we've completed running a process

	def countdown(self,sec):
		for i in reversed(range(sec)):
			print(i)
			time.sleep(1)

	def snapshot(self):
		print('taking snapshot...')
		time.sleep(1)

	def shutdown(self):
		#self.stopEvent.set()
		self.webcam.stop()
		cv2.destroyAllWindows()










