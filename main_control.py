#!/usr/bin/python

import serial
import os
import sys
import termios
import tty
import rospy
from geometry_msgs.msg import Twist



#Movement variables
SIT = (b'\xff\xff\xfd\x00\xc8\x07\x00\x03\x42\x00\x03\x00\xd9\xed')
STAND = (b'\xff\xff\xfd\x00\xc8\x07\x00\x03\x42\x00\x02\x00\xda\x6b')
FORWARD = (b'\xff\xff\xfd\x00\xc8\x07\x00\x03\x42\x00\x13\x00\xda\x0d')
REVERSE = (b'\xff\xff\xfd\x00\xc8\x07\x00\x03\x42\x00\x14\x00\xd9\x9f')
SIDELEFT = (b'\xff\xff\xfd\x00\xc8\x07\x00\x03\x42\x00\x12\x00\xd9\x8b')
SIDERIGHT = (b'\xff\xff\xfd\x00\xc8\x07\x00\x03\x42\x00\x11\x00\xd9\x81')
TURNLEFT = (b'\xff\xff\xfd\x00\xc8\x07\x00\x03\x42\x00\x10\x00\xda\x07')
TURNRIGHT = (b'\xff\xff\xfd\x00\xc8\x07\x00\x03\x42\x00\x0f\x00\xd9\xc5')
INITIAL = (b'\xff\xff\xfd\x00\xc8\x07\x00\x03\x42\x00\x01\x00\xda\x61')
WAVELEFT = (b'\xff\xff\xfd\x00\xc8\x07\x00\x03\x42\x00\x0e\x00\xda\x43')
WAVERIGHT = (b'\xff\xff\xfd\x00\xc8\x07\x00\x03\x42\x00\x0d\x00\xda\x49')
FASTADVANCE = (b'\xff\xff\xfd\x00\xc8\x07\x00\x03\x42\x00\x27\x00\xd9\x35')
STOPADVANCE = (b'\xff\xff\xfd\x00\xc8\x07\x00\x03\x42\x00\x00\x00\xd9\xe7')


# Initialize Serial Port
port = serial.Serial("/dev/rfcomm0", baudrate = 57600)


def callback(movement):
    global port
    print(movement)
    if movement.linear.y > 0:
        port.write(SIDERIGHT)
    if movement.linear.y < 0:
        port.write(SIDELEFT)
    if movement.linear.x > 0:
        port.write(FORWARD)
    if movement.linear.x < 0:
        port.write(REVERSE)
    if movement.linear.z > 0:
        port.write(STAND)
    if movement.linear.z < 0:
        port.write(SIT)
    if movement.angular.x > 0:
        port.write(TURNRIGHT)
    if movement.angular.x < 0:
        port.write(TURNLEFT)
    if movement.angular.y < 0:
        port.write(WAVERIGHT)
    if movement.angular.y > 0:
        port.write(WAVELEFT)
    if movement.angular.z < 0:
        port.write(FASTADVANCE)
    if movement.angular.z < 0:
        port.write(STOPADVANCE)


if __name__=="__main__":
    rospy.loginfo( "main control robotis mini")
    rospy.init_node("robotis_mini_control")
    port.write(INITIAL)
    command_vel = rospy.Subscriber('/cmd_vel', Twist, callback)
    try:
        rospy.spin()
    except KeyboardInterrupt:
        print("SHUTDOWN")

