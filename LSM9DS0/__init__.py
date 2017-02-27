import LSM9DS0
import Charts
# create LSM9DS0 instance
lsm9ds0 	= LSM9DS0()

# init 3d cube
# init chart(s)


while True:
	# grab LSM9DS0 data
	data 	= LSM9DS0.formatted()

	# update 3d cube
	# update line chart(s)