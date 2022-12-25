#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor, GyroSensor
from pybricks.parameters import Port, Color, Button, Direction
from pybricks.robotics import DriveBase
import time
import thread

rightMotor = Motor(Port.B, Direction.COUNTERCLOCKWISE)
leftMotor = Motor(Port.C, Direction.COUNTERCLOCKWISE)

rightColor = ColorSensor(Port.S2)
leftColor = ColorSensor(Port.S3)

robot = DriveBase(leftMotor, rightMotor, wheel_diameter=94.2, axle_track=157)
robot.settings(straight_speed=300)

def saveData():
    ...

def recordData():
    ...

def drive():
    ...