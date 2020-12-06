#!/bin/python3

from motor.model.pwm_motor import PWMMotor
import time

if __name__ == '__main__':
    drive = PWMMotor(38, 40, 32)
    drive.stop()
    while True:
        drive.forward(0.25)
        time.sleep(3)
        drive.forward(0.9)
        time.sleep(3)
        # drive.backward()
        # time.sleep(10)
        # drive.turn_left()
        # time.sleep(10)
        # drive.turn_right()
        # time.sleep(10)
