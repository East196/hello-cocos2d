#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division, print_function, unicode_literals

import cocos
import pyglet
from pyglet.gl import *

X_MAX = 800
Y_MAX = 600

LEFT, RIGHT, UP, DOWN = 0, 1, 3, 4
START, STOP = 0, 1


class Explosion(cocos.scene.Scene):
    def __init__(self, x, y):
        super(Explosion, self).__init__()
        self.x = x
        self.y = y
        sheet = pyglet.image.load("res/x.png")
        self.images = []
        for i in range(0, 768, 48):
            image = sheet.get_region(i, 0, 48, 48)
            self.images.append(image)

        animation = pyglet.image.Animation.from_image_sequence(self.images, 0.1, True)
        self.sprite = cocos.sprite.Sprite(animation, position=self.position)
        self.add(self.sprite)

    def draw(self, *args, **kwargs):

        if not self.sprite.is_running:
            self.sprite.kill()


# class EnemySprite(cocos.sprite.Sprite):
#     def __init__(self,image):
#         super(EnemySprite, self).__init__(image)
#         self.velocity = random.randint(3, 10)
#         self.explosion_sound = pygame.mixer.Sound("Arcade Explo A.wav")
#         self.explosion_sound.set_volume(0.4)
#         self.kill()
#
#     def update(self):
#         x, y = self.rect.center
#
#         if y > Y_MAX:
#             x, y = random.randint(0, X_MAX), 0
#             self.velocity = random.randint(3, 10)
#         else:
#             x, y = x, y + self.velocity
#
#         self.rect.center = x, y
#
#     def kill(self):
#         x, y = self.rect.center
#         if pygame.mixer.get_init():
#             self.explosion_sound.play(maxtime=1000)
#             Explosion(x, y)
#         super(EnemySprite, self).kill()


if __name__ == "__main__":
    cocos.director.director.init(width=200, height=200, style='dialog')

    main_scene = Explosion(50, 50)

    cocos.director.director.run(main_scene)
