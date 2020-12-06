# coding: utf-8

from car.pwm_car import PWMCar
from gamepad.gamepad import Gamepad
from motor.model.pwm_four_wheel_drive import PWMFourWheelDrive
from camera.camera_motor import CameraMotor
from player.music_player import MusicPlayer

if __name__ == '__main__':
    drive = PWMFourWheelDrive(11, 12, 16, 13, 15, 19, 36, 37, 26, 38, 40, 24)
    car = PWMCar(drive)
    camera_motor = CameraMotor(29, 31, 33, 35)
    music_player = MusicPlayer()

    gamepad = Gamepad()
    gamepad.register(car)
    gamepad.register(camera_motor)
    gamepad.register(music_player)
    gamepad.start()
