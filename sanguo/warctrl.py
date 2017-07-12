from __future__ import division, print_function, unicode_literals

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../..'))

from pyglet.window import key
from cocos.layer import Layer
from hero import Hero

class WarCtrl(Layer):
    is_event_handler = True  #: enable pyglet's events

    def __init__(self, model):
        super(WarCtrl, self).__init__()
        self.model = model

    def on_key_press(self, k, m):
        if k in (key.A, key.D, key.S, key.W, key.SPACE):
            if k == key.A:
                print("A")
                self.model.change_to(Hero.ATTACK)
            elif k == key.D:
                print("D")
                self.model.change_to(Hero.RUN)
            elif k == key.S:
                self.model.block_down()
            elif k == key.W:
                self.model.block_rotate()
            return True
        return False
