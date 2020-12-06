# coding: utf-8

from gamepad.gamepad import GamepadCtrl

class Car(GamepadCtrl):
    def __init__(self, drive):
        self.drive = drive 

    def x(self, val):
        if val:
            self.drive.stop()

    def dir_x(self, val):
        self.l_joy_x(val)

    def dir_y(self, val):
        self.l_joy_y(val)

    def l_joy_x(self, val):
        print('car.y', val)
        if val < -0.5:
            self.drive.turn_left()
        elif val > 0.5:
            self.drive.turn_right()

    def l_joy_y(self, val):
        print('car.x', val)
        if val < -0.5:
            self.drive.forward()
        elif val > 0.5:
            self.drive.backward()
 
