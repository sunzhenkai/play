# coding: utf-8

from car.car import Car
from gamepad.gamepad import Gamepad
from motor.model.four_wheel_drive import FourWheelDrive

if __name__ == '__main__':
    drive = FourWheelDrive(11, 12, 13, 15, 36, 37, 38, 40)
    car = Car(drive)
    gamepad = Gamepad()
    gamepad.register(car)
    gamepad.start()
