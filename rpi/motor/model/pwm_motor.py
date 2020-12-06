#!/bin/python
# coding: utf-8

import RPi.GPIO as GPIO

class PWMMotor:
    def __init__(self, pin_1, pin_2, pin_en, hz=100):
        print('init PWMMotor:', pin_1, pin_2, pin_en)
        self.pin_1 = pin_1
        self.pin_2 = pin_2
        self.pin_en = pin_en
        self.hz = hz
        self.setup()
        self.pwm = GPIO.PWM(pin_en, hz)
        self.pwm.start(0)
        self.pwm.ChangeDutyCycle(0)

    def setup(self):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.pin_1, GPIO.OUT)
        GPIO.setup(self.pin_2, GPIO.OUT)
        GPIO.setup(self.pin_en, GPIO.OUT)

    def set_duty(self, duty):
        duty = 0 if duty < 10 else duty 
        self.pwm.ChangeDutyCycle(duty)
        
    def set_step(self, s1, s2, speed=1):
        duty = int(abs(100 * speed))
        self.set_duty(duty)
        GPIO.output(self.pin_1, s1)
        GPIO.output(self.pin_2, s2)
        GPIO.output(self.pin_en, duty)


    def forward(self, speed = 1):
        self.set_step(1, 0, speed)

    def backward(self, speed = 1):
        self.set_step(0, 1, speed)

    def stop(self):
        self.set_step(0, 0)

    def speed(self, speed=1):
        if speed > 0:
            self.backward(speed)
        else:
            self.forward(abs(speed))

