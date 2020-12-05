# coding: utf-8

import asyncio
from gamepad.gamepad import Gamepad

def test_gamepad():
    gamepad = Gamepad()
    # futures = [gamepad.read()]
    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(asyncio.wait(futures))
    # loop.close()
    gamepad.start()


if __name__ == '__main__':
    print('Hello RPI')
    test_gamepad()
