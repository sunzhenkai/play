# coding: utf-8

from gamepad.gamepad import GamepadCtrl
from motor.model.pwm_four_wheel_drive import PWMFourWheelDrive

class PWMCar(GamepadCtrl):
    def __init__(self, drive: PWMFourWheelDrive):
        self.drive = drive 

    def x(self, val):
        if val:
            self.drive.stop()

    def dir_x(self, val):
        self.l_joy_x(val)

    def dir_y(self, val):
        self.l_joy_y(val)

    def l_joy_x(self, val):
        print('car.x', val)
        self.drive.speed_x(val)

    def l_joy_y(self, val):
        print('car.y', val)
        self.drive.speed_y(val)
    


    
