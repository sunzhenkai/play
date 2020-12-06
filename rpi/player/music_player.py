# coding: utf-8

from gamepad.controller import GamepadCtrl
import vlc
import os
import threading
import time

class MusicPlayer(GamepadCtrl):
    def __init__(self, res='resources/music'):
        self.files = list(map(lambda x: os.path.join(res, x), os.listdir(res)))
        self.instance = vlc.Instance()
        self.medias = [self.instance.media_new(f) for f in self.files]
        self.current = 0
        self.playing = False
        self.player = vlc.MediaPlayer()
        self.on = False
        self.thd = threading.Thread(target=self.run)
        self.thd.start()

    def run(self):
        while True:
            if self.on and self.medias:
                if not self.player.is_playing():
                    m = self.medias[self.current % len(self.medias)]
                    self.player.set_media(m)
                    self.player.play()
                    self.player.audio_set_volume(300)
                    self.current = (self.current + 1) % len(self.medias)
            elif not self.on and self.player.is_playing():
                self.player.stop()
                    
            time.sleep(0.5)

    def b(self, val):
        if val:
            self.on = not self.on

    def y(self, val):
        if val and self.on:
            self.player.stop()
