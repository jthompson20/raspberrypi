import Adafruit.GPIO.I2C as I2C
import math

class LSM9DS0(object):
    # set global variables
    # The same address is used for both the magnetometer and accelerometer, but
    # each has their own variable, to avoid confusion.
    LSM9DS0_MAG_ADDRESS	    =   0x1D
    LSM9DS0_ACCEL_ADDRESS	=	0x1D
    LSM9DS0_GYRO_ADDRESS    =   0x6B

    #LSM9DS0 gyrometer registers
    LSM9DS0_WHO_AM_I_G	      =	0x0F
    LSM9DS0_CTRL_REG1_G	      =	0x20
    LSM9DS0_CTRL_REG3_G	      =	0x22
    LSM9DS0_CTRL_REG4_G	      =	0x23
    LSM9DS0_OUT_X_L_G	      =	0x28
    LSM9DS0_OUT_X_H_G	      =	0x29
    LSM9DS0_OUT_Y_L_G	      =	0x2A
    LSM9DS0_OUT_Y_H_G	      =	0x2B
    LSM9DS0_OUT_Z_L_G	      =	0x2C
    LSM9DS0_OUT_Z_H_G	      =	0x2D

    # LSM9DS0 temperature addresses
    LSM9DS0_OUT_TEMP_L_XM	  =	0x05
    LSM9DS0_OUT_TEMP_H_XM	  =	0x06

    # Magnetometer addresses
    LSM9DS0_STATUS_REG_M	  =	0x07
    LSM9DS0_OUT_X_L_M         =	0x08
    LSM9DS0_OUT_X_H_M         =	0x09
    LSM9DS0_OUT_Y_L_M         =	0x0A
    LSM9DS0_OUT_Y_H_M         =	0x0B
    LSM9DS0_OUT_Z_L_M         =	0x0C
    LSM9DS0_OUT_Z_H_M         =	0x0D

    # Shared addresses
    LSM9DS0_WHO_AM_I_XM	      =	0x0F
    LSM9DS0_INT_CTRL_REG_M    =	0x12
    LSM9DS0_INT_SRC_REG_M	  =	0x13
    LSM9DS0_CTRL_REG1_XM      =	0x20
    LSM9DS0_CTRL_REG2_XM	  =	0x21
    LSM9DS0_CTRL_REG5_XM	  =	0x24
    LSM9DS0_CTRL_REG6_XM	  =	0x25
    LSM9DS0_CTRL_REG7_XM	  =	0x26

    # Accelerometer addresses
    LSM9DS0_OUT_X_L_A	      =	0x28
    LSM9DS0_OUT_X_H_A	      =	0x29
    LSM9DS0_OUT_Y_L_A	      =	0x2A
    LSM9DS0_OUT_Y_H_A	      =	0x2B
    LSM9DS0_OUT_Z_L_A	      =	0x2C
    LSM9DS0_OUT_Z_H_A	      =	0x2D

    # Various settings included in the Arduino library. I haven't used these,
    # to keep to a default setting for simplicity, however, users can change
    # the settings easily.
    LSM9DS0_ACCELRANGE_2G                = 0b000 << 3
    LSM9DS0_ACCELRANGE_4G                = 0b001 << 3
    LSM9DS0_ACCELRANGE_6G                = 0b010 << 3
    LSM9DS0_ACCELRANGE_8G                = 0b011 << 3
    LSM9DS0_ACCELRANGE_16G               = 0b100 << 3

    LSM9DS0_ACCELDATARATE_POWERDOWN      = 0b0000 << 4
    LSM9DS0_ACCELDATARATE_3_125HZ        = 0b0001 << 4
    LSM9DS0_ACCELDATARATE_6_25HZ         = 0b0010 << 4
    LSM9DS0_ACCELDATARATE_12_5HZ         = 0b0011 << 4
    LSM9DS0_ACCELDATARATE_25HZ           = 0b0100 << 4
    LSM9DS0_ACCELDATARATE_50HZ           = 0b0101 << 4
    LSM9DS0_ACCELDATARATE_100HZ          = 0b0110 << 4
    LSM9DS0_ACCELDATARATE_200HZ          = 0b0111 << 4
    LSM9DS0_ACCELDATARATE_400HZ          = 0b1000 << 4
    LSM9DS0_ACCELDATARATE_800HZ          = 0b1001 << 4
    LSM9DS0_ACCELDATARATE_1600HZ         = 0b1010 << 4

    LSM9DS0_MAGGAIN_2GAUSS               = 0b00 << 5
    LSM9DS0_MAGGAIN_4GAUSS               = 0b01 << 5
    LSM9DS0_MAGGAIN_8GAUSS               = 0b10 << 5
    LSM9DS0_MAGGAIN_12GAUSS              = 0b11 << 5

    LSM9DS0_MAGDATARATE_3_125HZ          = 0b000 << 2
    LSM9DS0_MAGDATARATE_6_25HZ           = 0b001 << 2
    LSM9DS0_MAGDATARATE_12_5HZ           = 0b010 << 2
    LSM9DS0_MAGDATARATE_25HZ             = 0b011 << 2
    LSM9DS0_MAGDATARATE_50HZ             = 0b100 << 2
    LSM9DS0_MAGDATARATE_100HZ            = 0b101 << 2

    LSM9DS0_GYROSCALE_245DPS             = 0b00 << 4
    LSM9DS0_GYROSCALE_500DPS             = 0b01 << 4
    LSM9DS0_GYROSCALE_2000DPS            = 0b10 << 4

    def __init__(self,bus):
    	# grab addresses for each (gyroscope, accelerometer and magnetometer)

    	# initialize magnetometer

    	# initialize accelerometer

    	# initialize gyroscope

    	# initialize variables

    def gyroscope():
    	# get raw gyroscope data

    def accelerometer():
    	# get raw accelerometer data

    def magnetometer():
    	# get raw magnetometer data

    def roll():
    	# get roll

    def pitch():
    	# get pitch

    def yaw():
    	# get yaw

    def dpsX():
    	# get degrees per second on X axis

    def dpsY():
    	# get degrees per second on Y axis

    def dpsZ():
    	# get degrees per second on Z axis

    def filtered():
    	# get filtered data

    def complementary_filter():
    	# run complementary filter methodology

    def kalman_filter():
    	# run kalman filter methodology



