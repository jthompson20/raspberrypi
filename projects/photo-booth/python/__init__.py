# import the necessary packages
from __future__ import print_function
from imutils.video import WebcamVideoStream
#from gpiozero import LED, Button
from signal import pause
#from PhotoBooth import PhotoBooth
import imutils
import cv2
import sys
import cv2
import sys
import time
import datetime

## CONFIGURATION VARIABLES
GPIO 		= False
WAIT 		= 5
RECORD 		= 30
SNAPSHOTS 	= 4

# setup GPIO pins
if GPIO:
	pins 	= {
		'start': 		{
			'button': 	Button(4),
			'led': 		LED(18)
		},
		'record': 		{
			'button': 	Button(3),
			'led': 		LED(17)
		},
		'shutdown': 	{
			'button': 	Button(5),
			'led': 		LED(19)
		}
	}

# setup booth variables
booth 	= {
	'sequence': 	{
		'active': 		False,
		'wait': 		WAIT,
		'snapshots': 	SNAPSHOTS,
		'clock': 		0
	},
	'recording': 	{
		'active': 		False,
		'wait': 		RECORD,
		'start': 		0
	},
	'counter': 		0
}

# initialize webcam
webcam 	= WebcamVideoStream(src=0).start()

try:
	while True:

		frame 	= webcam.read()
		frame 	= imutils.resize(frame, width=600)

		# if we have started the photo booth sequence
		if booth['sequence']['active'] and not booth['recording']['active']:

			now 	= datetime.datetime.now()

			# lets start the timer
			if booth['sequence']['wait'] == WAIT and booth['sequence']['clock'] == 0:
				# initialize our clock
				booth['sequence']['clock'] 	= now
				# display our first number
				cv2.putText(frame, "matt motherfuckin thompson",(105, 105),cv2.FONT_HERSHEY_COMPLEX_SMALL,.7,(225,0,0))

			# perform datetime difference
			diff 		= now - booth['sequence']['clock']
			(min,sec) 	= divmod(diff.days * 86400 + diff.seconds, 60)

			# if we've waited another second
			if sec > 1:
				# reset clock
				booth['sequence']['clock'] 	= datetime.datetime.now()
				# we either have to print a number, or take a snapshot
				if booth['sequence']['wait'] > 0:
					print(booth['sequence']['wait'])
					cv2.putText(frame, "Number: %d" % booth['sequence']['wait'],(105, 105),cv2.FONT_HERSHEY_COMPLEX_SMALL,.7,(0,0,0))
					booth['sequence']['wait']-=1

				if booth['sequence']['wait'] == 0 and booth['sequence']['snapshots'] > 0:
					# take snapshot
					print('taking snapshot...')
					cv2.putText(frame, "Number: %d" % booth['sequence']['wait'],(105, 105),cv2.FONT_HERSHEY_COMPLEX_SMALL,.7,(0,0,0))
					# decrement snapshots
					booth['sequence']['snapshots']-=1
					# reset wait time
					booth['sequence']['wait'] 	= WAIT


			# lets reset everything
			if booth['sequence']['snapshots'] == 0:
				print('ending photobooth sequence')
				booth['sequence']['active'] 	= False
				booth['sequence']['wait'] 		= WAIT
				booth['sequence']['snapshots'] 	= SNAPSHOTS
				booth['sequence']['clock'] 		= 0


		# if we have started the recording method
		if booth['recording']['active'] and not booth['sequence']['active']:
			# record video
			pass

		
		# Display the resulting frame
		cv2.imshow('Lillian\'s Birthday Photo Booth!', frame)



		# wait for specific keypress to trigger different methods
		if cv2.waitKey(1) & 0xFF == ord('s'):
			#booth.start()
			print('start booth')
			booth['sequence']['active'] 	= True
			pass

		if cv2.waitKey(1) & 0xFF == ord('r'):
			#booth.record()
			print('recording')
			booth['recording']['active'] 	= True
			pass

		if cv2.waitKey(1) & 0xFF == ord('q'):
			#booth.shutdown()
			print('quitting')
			pass
except KeyboardInterrupt:
	pass
except Exception as e:
	print(e)
finally:
	webcam.stop()
	cv2.destroyAllWindows()














'''
try:
	# run photobooth capture method on button press if GPIO enabled
	if GPIO:
		pins['start']['button'].when_pressed 	= booth.start()
		pins['record']['button'].when_pressed 	= booth.record()
		pins['shutdown']['button'].when_pressed = booth.shutdown()

		pause()
	else:
		# run never ending loop of video
		while True:

			frame 	= webcam.read()
			frame 	= imutils.resize(frame, width=600)

			# Display the resulting frame
			cv2.imshow('Lillian\'s Birthday Photo Booth!', frame)

			# wait for specific keypress to trigger different methods
			if cv2.waitKey(1) & 0xFF == ord('s'):
				booth.start()

			if cv2.waitKey(1) & 0xFF == ord('r'):
				booth.record()

			if cv2.waitKey(1) & 0xFF == ord('q'):
				booth.shutdown()

except KeyboardInterrupt:
	pass
except Exception as e:
	print(e)
finally:
	webcam.stop()
	cv2.destroyAllWindows()
'''











