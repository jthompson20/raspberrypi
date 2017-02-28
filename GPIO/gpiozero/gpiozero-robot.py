from gpiozero import Robot
import time

from gpiozero import Robot

robot = Robot(left=(4, 14), right=(17, 18))

robot.forward()
robot.backward()
robot.left()
robot.right()
robot.reverse()
robot.stop()
