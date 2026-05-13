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

#funciones 
def garra(grados):
    motor_izquierdo.run_angle(500, grados, then=stop.HOLD, wait=False)
    motor_derecho.run_angle(500, grados, then=stop.HOLD, wait=True)

def llantas(velocidad, grados):
    motor_llantaizq.run_angle(velocidad, grados, then=stop.HOLD, wait=False)
    motor_llantader.run_angle(velocidad, grados, then=stop.HOLD, wait=True)



# Sonido de inicio




# Initialize a motor at port B.






ev3.speaker.beep()

# Run the motor up to 500 degrees per second. To a target angle of 90 degrees.






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

    
    
