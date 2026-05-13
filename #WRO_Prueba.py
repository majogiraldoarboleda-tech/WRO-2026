#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port
from pybricks.robotics import DriveBase

# 1. Inicializar el bloque EV3
ev3 = EV3Brick()

# 2. Definir los motores en los puertos B y C
motor_izquierdo = Motor(Port.B)
motor_derecho = Motor(Port.C)
motor_llantaizq = Motor(Port.A)
motor_llantader = Motor(Port.D)
garra = DriveBase(motor_izquierdo, motor_derecho, wheel_diameter=56, axle_track=114)
#funciones 
def garra(grados):
    motor_izquierdo.run_angle(500, grados, then=Stop.HOLD, wait=True)
    motor_derecho.run_angle(500, grados, then=Stop.HOLD, wait=False)

def llantas(velocidad, grados):
    motor_llantaizq.run_angle(velocidad, grados, then=Stop.HOLD, wait=True)
    motor_llantader.run_angle(velocidad, grados, then=Stop.HOLD, wait=False)


garra.settings(straight_speed=12000, straight_acceleration=1000000)
# Sonido de inicio




# Initialize a motor at port B.





llantas = DriveBase(motor_llantaizq, motor_llantader, wheel_diameter=56, axle_track=114)
llantas.settings(straight_speed=500, straight_acceleration=1000000)
# Sonido de inicio
ev3.speaker.beep()
# Initialize the EV3 brick.

llantas.straight(1200)
ev3.speaker.beep()

# Run the motor up to 500 degrees per second. To a target angle of 90 degrees.





llantas = DriveBase(motor_llantaizq, motor_llantader, wheel_diameter=56, axle_track=114)
llantas.settings(straight_speed=500, straight_acceleration=1000000)
llantas.straight(-1200)
# Sonido de inicio






# Initialize a motor at port B.





# Si prefieres que gire sobre su propio eje:
# robot.turn(90)  # Gira 90 grados

# Sonido de finalización


while True:
    garra(-1200)
    llantas(600,1200)
     garra(1200)
    llantas(600, -1200)
    ev3.speaker.beep()

    
