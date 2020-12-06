# coding: utf-8

import threading
import time
from motor.model.step_motor import StepMotor
from gamepad.controller import GamepadCtrl

class CameraMotor(GamepadCtrl):
    def __init__(self, pin_1, pin_2, pin_3, pin_4):
        self.motor = StepMotor(pin_1, pin_2, pin_3, pin_4)
        self.value = 0
        self.lock = threading.Lock()
        self.thd = threading.Thread(target=self.run)
        self.thd.start()

    def r_joy_x(self, val):
        self.value =val

    def run(self):
        while True:
            if self.value < -0.5:
                self.motor.backward(5)
            elif self.value > 0.5:
                self.motor.forward(5)
            time.sleep(0.01)
            

