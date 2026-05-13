#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

# 1. Inicializar el bloque EV3
ev3 = EV3Brick()

# 2. Definir los motores en los puertos B y C
motor_izquierdo = Motor(Port.B)
motor_derecho = Motor(Port.C)
motor_llantaizq = Motor(Port.A)
motor_llantader = Motor(Port.D)

#funciones 
def garra(grados):
    motor_izquierdo.run_angle(1100, grados, then=Stop.HOLD, wait=False)
    motor_derecho.run_angle(1100, grados, then=Stop.HOLD, wait=True)

def llantas(velocidad, grados):
    motor_llantaizq.run_angle(velocidad, grados, then=Stop.HOLD, wait=False)
    motor_llantader.run_angle(velocidad, grados, then=Stop.HOLD, wait=True)
def llanta_izquierda(velocidad, grados):
    motor_llantaizq.run_angle(velocidad, grados, then=Stop.HOLD, wait=True)
def llanta_derecha(velocidad, grados):
    motor_llantader.run_angle(velocidad, grados, then=Stop.HOLD, wait=True)


while True:
    garra(-2000)
    llantas(600,1200)
    garra(2000)
    llantas(600, -1200)
    ev3.speaker.beep()
    llanta_derecha(600, 1200)
    llanta_izquierda(600, 1200)
    llantas.stop()
    garra.stop()
    llanta_derecha.stop()
    llanta_izquierda.stop()
