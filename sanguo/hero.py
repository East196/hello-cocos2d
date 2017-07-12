#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division, print_function, unicode_literals

import cocos
from cocos.director import *
from cocos.actions import *
from cocos.sprite import *

import pyglet
from pyglet import *


def sprite_in_x_status(status):
    attacks = [pyglet.image.load('PAK/SHAPE/MAJOR/L4%s1000%s.PNG' % (status, frame)) for frame in
               [1, 2, 3, 4, 5, 6]]
    animation = pyglet.image.Animation.from_image_sequence(attacks, 0.1, True)
    sprite = Sprite(animation)
    return


class Hero(object):
    ATTACK = "A"
    RUN = "R"

    def __init__(self):
        self.sprite = None
        self.position = (320, 250)

    def change_to(self, status):
        attacks = [pyglet.image.load('PAK/SHAPE/MAJOR/L4%s1000%s.BMP' % (status, frame)) for frame in
                   [ 2, 3, 4, 5]]
        animation = pyglet.image.Animation.from_image_sequence(attacks, 0.2, True)
        self.sprite = cocos.sprite.Sprite(animation, position=self.position)

        print(sprite)

    def go(self):
        self.change_to(Hero.ATTACK)
        self.to((50, self.sprite.y))

    def to(self, point=(0, 0)):
        self.sprite.do(MoveTo(point, 1))
