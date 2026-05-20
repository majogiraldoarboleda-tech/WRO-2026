#!/usr/bin/env pybricks-micropython

"""
Example LEGO® MINDSTORMS® EV3 Robot Educator Color Sensor Down Program
----------------------------------------------------------------------

This program requires LEGO® EV3 MicroPython v2.0.
Download: https://education.lego.com/en-us/support/mindstorms-ev3/python-for-ev3

Building instructions can be found at:
https://education.lego.com/en-us/support/mindstorms-ev3/building-instructions#robot
"""

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
ev3 = EV3Brick()
# Initialize the motors.
left_motor = Motor(Port.A)
right_motor = Motor(Port.D)
claw_motor = Motor(Port.B)
claw_motor1 = Motor(Port.C)


# Initialize the color sensor.
line_sensor1 = ColorSensor(Port.S1)
line_sensor2 = ColorSensor(Port.S2)
# Initialize the drive base.
robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=104)

# Calculate the light threshold. Choose values based on your measurements.
BLACK = 2
WHITE = 59
threshold = (BLACK + WHITE) / 2
thresoldsensor = (line_sensor1.reflection() + line_sensor2.reflection()) / 2
# Set the drive speed at 100 millimeters per second.
DRIVE_SPEED = 250

# Set the gain of the proportional line controller. This means that for every
# percentage point of light deviating from the threshold, we set the turn
# rate of the drivebase to 1.2 degrees per second.

# For example, if the light value deviates from the threshold by 10, the robot
# steers at 10*1.2 = 12 degrees per second.
PROPORTIONAL_GAIN = 0.8





# seguir linea recta
while robot.distance() < 1500:

    

    # Set the drive base speed and turn rate.
    robot.drive(DRIVE_SPEED, 2.4)

#154cm
while robot.distance() >= 1500 and robot.distance() < 1750:
    #ir rotando a la derecha en linea no curveada
    
   
    if abs(line_sensor1.reflection() - line_sensor2.reflection()) < 8 and line_sensor1.reflection() < 13 :
        robot.turn(-120)
        robot.straight(60)
        robot.turn(90)

        
    elif abs(line_sensor1.reflection() - line_sensor2.reflection()) >= 8 or line_sensor1.reflection() >= 13 :
        deviation = line_sensor2.reflection() - line_sensor1.reflection() 
    
        # Calculate the turn rate.
        turn_rate = 1.2 * deviation + 35

        # Set the drive base speed and turn rate.
        robot.drive(DRIVE_SPEED, turn_rate)

#TERMINA PRIMER GIRO

#9cm
#ir rotando a la izquierda en linea no curveada        
while robot.distance() >= 1750 and robot.distance() < 1975:
   


    # cuando alguno de los dos o los sensores esten en blanco o la diferencia entre ambos sea mayor a 8
 
 
    deviation = line_sensor2.reflection() - line_sensor1.reflection() + 15
    
        # Calculate the turn rate.
    turn_rate = PROPORTIONAL_GAIN * deviation

        # Set the drive base speed and turn rate.
    robot.drive(DRIVE_SPEED, turn_rate)
#30cm
DRIVE_SPEED = 300
while robot.distance() >= 1975:
    robot.stop()
    garra = DriveBase(claw_motor, claw_motor1, wheel_diameter=55.5, axle_track=104)
    garra.settings(straight_speed=500)  
    wait(100)
    garra.straight(1200)
    garra.stop()
    robot= DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=104)
    robot.settings(straight_speed=250)
    robot.straight(-360)
    robot.stop()
    if abs(line_sensor1.reflection() - line_sensor2.reflection()) < 8 and line_sensor1.reflection() < 13 :
  
        robot.turn(-60)

        
    elif abs(line_sensor1.reflection() - line_sensor2.reflection()) >= 8 or line_sensor1.reflection() >= 13 :
        deviation = line_sensor2.reflection() - line_sensor1.reflection() 
    
        # Calculate the turn rate.
        turn_rate = PROPORTIONAL_GAIN * deviation - 25

        # Set the drive base speed and turn rate.
        robot.drive(DRIVE_SPEED, turn_rate)
