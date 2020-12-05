#!/usr/bin/env python3
# coding: utf-8

import asyncio
from evdev import InputDevice, ff, ecodes
from gamepad.controller import GamepadCtrl


class Gamepad(GamepadCtrl):
    def __init__(self, evt_f='/dev/input/event0'):
        self.input = InputDevice(evt_f)
        self.ctrls = set()
        self.on = True

    def register(self, ctrl: GamepadCtrl):
        self.ctrls.add(ctrl)

    def lt(self, val):
        for ctrl in self.ctrls:
            ctrl.lt(val)

    def rt(self, val):
        for ctrl in self.ctrls:
            ctrl.rt(val)


    def lb(self, val):
        for ctrl in self.ctrls:
            ctrl.lb(val)

    def rb(self, val):
        for ctrl in self.ctrls:
            ctrl.rb(val)

    def x(self, val):
        for ctrl in self.ctrls:
            ctrl.x(val)

    def y(self, val):
        for ctrl in self.ctrls:
            ctrl.y(val)

    def a(self, val):
        for ctrl in self.ctrls:
            ctrl.a(val)

    def b(self, val):
        for ctrl in self.ctrls:
            ctrl.b(val)

    def l_joy_x(self, val):
        for ctrl in self.ctrls:
            ctrl.l_joy_x(val)

    def l_joy_y(self, val):
        for ctrl in self.ctrls:
            ctrl.l_joy_y(val)

    def r_joy_x(self, val):
        for ctrl in self.ctrls:
            ctrl.r_joy_x(val)

    def r_joy_y(self, val):
        for ctrl in self.ctrls:
            ctrl.r_joy_y(val)

    def dir_x(self, val):
        for ctrl in self.ctrls:
            ctrl.dir_x(val)
            
    def dir_y(self, val):
        for ctrl in self.ctrls:
            ctrl.dir_y(val)

    async def read(self):
        joy_mid = 0xFFFF / 2.0
        max_trigger = 1023.0
        async for event in self.input.async_read_loop():
            if not self.on:
                break

            tp = int(event.type)
            val = int(event.value)
            code = int(event.code)
            # print(tp, val, code, code == 3, tp == 10)
            if tp == 3:
                if code == 0:
                    val = (val - joy_mid) / joy_mid
                    self.l_joy_x(val)
                elif code == 1:
                    val = (val - joy_mid) / joy_mid
                    self.l_joy_y(val)
                elif code == 2:
                    val = (val - joy_mid) / joy_mid
                    self.r_joy_x(val)
                elif code == 5:
                    val = (val - joy_mid) / joy_mid
                    self.r_joy_y(val)
                elif code == 9:
                    val /= max_trigger
                    self.rt(val)
                elif code == 10:
                    val /= max_trigger
                    self.lt(val)
                elif code == 16:
                    self.dir_x(val)
                elif code == 17:
                    self.dir_y(val)

            elif tp == 1:
                if code == 304:
                    self.a(val == 1)
                elif code == 305:
                    self.b(val == 1)
                elif code == 307:
                    self.x(val == 1)
                elif code == 308:
                    self.y(val == 1)
                elif code == 310:
                    self.lb(val == 1)
                elif code == 311:
                    self.rb(val == 1)

    def start(self):
        futures = [self.read()]
        loop = asyncio.get_event_loop()
        loop.run_until_complete(asyncio.wait(futures))
        loop.close()

    def stop(self):
        self.on = False
