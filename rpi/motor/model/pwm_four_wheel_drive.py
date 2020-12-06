#!/bin/python3

from motor.model.pwm_motor import PWMMotor

class PWMFourWheelDrive:
    def __init__(self, pin_1, pin_2, pin_en_1, pin_3, pin_4, pin_en_2, pin_5, pin_6, pin_en_3, pin_7, pin_8, pin_en_4):
        self.motor_f_r = PWMMotor(pin_1, pin_2, pin_en_1)
        self.motor_f_l = PWMMotor(pin_3, pin_4, pin_en_2)
        self.motor_b_l = PWMMotor(pin_5, pin_6, pin_en_3)
        self.motor_b_r = PWMMotor(pin_7, pin_8, pin_en_4)
        self.speed_x_val = 0
        self.speed_y_val = 0

    def forward(self, speed=1):
        print('forward')
        self.motor_f_r.forward(speed)
        self.motor_f_l.forward(speed)
        self.motor_b_l.forward(speed)
        self.motor_b_r.forward(speed)

    def backward(self, speed=1):
        print('backward')
        self.motor_f_r.backward(speed)
        self.motor_f_l.backward(speed)
        self.motor_b_l.backward(speed)
        self.motor_b_r.backward(speed)

    def turn_left(self, speed=1):
        print('turn left')
        self.motor_f_r.forward(speed)
        self.motor_f_l.backward(speed)
        self.motor_b_l.backward(speed)
        self.motor_b_r.forward(speed)
        
    def turn_right(self, speed=1):
        print('turn right')
        self.motor_f_r.backward(speed)
        self.motor_f_l.forward(speed)
        self.motor_b_l.forward(speed)
        self.motor_b_r.backward(speed)

    def speed_x(self, speed=1):
        self.speed_x_val = speed * 0.5
        self.flash_speed()

    def speed_y(self, speed=1):
        self.speed_y_val = speed
        self.flash_speed()

    def unify_speed(self, speed):
        return min(1, max(-1, speed))

    def flash_speed(self):
        self.motor_f_r.speed(self.unify_speed(self.speed_y_val + self.speed_x_val))
        self.motor_f_l.speed(self.unify_speed(self.speed_y_val - self.speed_x_val))
        self.motor_b_r.speed(self.unify_speed(self.speed_y_val + self.speed_x_val))
        self.motor_b_l.speed(self.unify_speed(self.speed_y_val - self.speed_x_val))
        
    def stop(self):
        self.motor_f_r.stop()
        self.motor_f_l.stop()
        self.motor_b_l.stop()
        self.motor_b_r.stop()
