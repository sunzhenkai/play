# coding: utf-8

from car.pwm_car import PWMCar
from gamepad.gamepad import Gamepad
from motor.model.pwm_four_wheel_drive import PWMFourWheelDrive

if __name__ == '__main__':
    drive = PWMFourWheelDrive(11, 12, 16, 13, 15, 19, 36, 37, 26, 38, 40, 32)
    car = PWMCar(drive)
    gamepad = Gamepad()
    gamepad.register(car)
    gamepad.start()
