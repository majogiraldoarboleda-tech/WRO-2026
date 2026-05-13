#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port

# 1. Inicializar el bloque y motores
ev3 = EV3Brick()
test_motor = Motor(Port.B)
test_motor1 = Motor(Port.C)

ev3.speaker.beep()

# 2. Mover ambos motores al tiempo
# Al poner wait=False, el motor B arranca y pasamos a la siguiente línea al instante
test_motor.run_target(500, 1000, wait=False)

# El motor C arranca mientras el B sigue girando
test_motor1.run_target(500, 1000)

# El programa llegará aquí solo cuando el motor C (el último con wait=True) termine
ev3.speaker.beep(1000, 500)
clc
