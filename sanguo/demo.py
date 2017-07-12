#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division, print_function, unicode_literals

import cocos
from cocos.director import director
from cocos.actions import *
from cocos.sprite import *

import pyglet
from pyglet import *
import sys
import os

from cocos.euclid import Vector2

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
#

import cocos
from hero import Hero
from warctrl import WarCtrl
class Square(cocos.layer.Layer):

    """Square (color, c, y, size=50) : A layer drawing a square at (x,y) of
    given color and size"""

    def __init__(self, color, x, y, size=50):
        super(Square, self).__init__()

        self.x = x
        self.y = y
        self.size = size
        self.layer_color = color

    def draw(self):
        super(Square, self).draw()

        gl.glColor4f(*self.layer_color)
        x, y = self.x, self.y
        w = x + self.size
        h = y + self.size
        gl.glBegin(gl.GL_QUADS)
        gl.glVertex2f(x, y)
        gl.glVertex2f(x, h)
        gl.glVertex2f(w, h)
        gl.glVertex2f(w, y)
        gl.glEnd()
        gl.glColor4f(1, 1, 1, 1)

class GameScene(cocos.scene.Scene):
    def __init__(self):
        super(GameScene, self).__init__()

    def create_layer(self):

        layer = Square((255,255,255,1),0,0,640)
        hero = Hero()
        print(hero.sprite)
        if hero.sprite is not None:
            hero.change_to("R")
        else:
            hero.change_to("A")
        layer.add(hero.sprite)
        ctrl = WarCtrl(hero)
        self.add(layer)
        self.add(ctrl)


if __name__ == "__main__":
    director.init(resizable=True)
    director.show_FPS = True
    main_scene = GameScene()
    main_scene.create_layer()
    director.run(main_scene)
