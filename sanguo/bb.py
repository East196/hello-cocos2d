#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division, print_function, unicode_literals

import cocos
from cocos.director import director
from cocos.actions import MoveTo,QuadMoveBy,MoveCornerUp
from cocos.sprite import Sprite

import pyglet
from pyglet import gl


class HelloWorld(cocos.layer.Layer):
    is_event_handler = True

    def __init__(self):
        super(HelloWorld, self).__init__()



        soldier = Soldier()
        if soldier.sprite is not None:
            self.add(soldier.sprite)
            soldier.to((200, 200))

        hero = Hero()
        if hero.sprite is not None:
            self.add(hero.sprite)
            hero.go()

        self.posx = 100
        self.posy = 240
        self.text = cocos.text.Label('No mouse events yet', font_size=18, x=self.posx, y=self.posy)
        self.add(self.text)

    def update_text(self, x, y):
        text = 'Mouse @ %d,%d' % (x, y)
        self.text.element.text = text
        self.text.element.x = self.posx
        self.text.element.y = self.posy

    def on_mouse_motion(self, x, y, dx, dy):
        """Called when the mouse moves over the app window with no button pressed

        (x, y) are the physical coordinates of the mouse
        (dx, dy) is the distance vector covered by the mouse pointer since the
          last call.
        """

        self.update_text(x, y)
        if x<20:
            self.position = self.position[0]-20,self.position[1]
        if x>620:
            self.position = self.position[0] + 20, self.position[1]

    def on_mouse_drag(self, x, y, dx, dy, buttons, modifiers):
        """Called when the mouse moves over the app window with some button(s) pressed

        (x, y) are the physical coordinates of the mouse
        (dx, dy) is the distance vector covered by the mouse pointer since the
          last call.
        'buttons' is a bitwise or of pyglet.window.mouse constants LEFT, MIDDLE, RIGHT
        'modifiers' is a bitwise or of pyglet.window.key modifier constants
           (values like 'SHIFT', 'OPTION', 'ALT')
        """
        self.update_text(x, y)

    def on_mouse_press(self, x, y, buttons, modifiers):
        """This function is called when any mouse button is pressed

        (x, y) are the physical coordinates of the mouse
        'buttons' is a bitwise or of pyglet.window.mouse constants LEFT, MIDDLE, RIGHT
        'modifiers' is a bitwise or of pyglet.window.key modifier constants
           (values like 'SHIFT', 'OPTION', 'ALT')
        """
        self.posx, self.posy = director.get_virtual_coordinates(x, y)
        self.update_text(x, y)

class HUD(cocos.layer.Layer):
    def __init__(self):
        super(HUD, self).__init__()
        WARBAR = Sprite("PAK/SHAPE/MENU/WARBAR.PNG")
        WARBAR.position = 320, 68
        self.add(WARBAR)

        enemy = Sprite("PAK/SHAPE/FACE/FACE001.PNG")
        enemy.position = 55, 83
        self.add(enemy)

        enemy = Sprite("PAK/SHAPE/FACE/FACE004.PNG")
        enemy.position = 640 - 55, 83
        self.add(enemy)




class Soldier(object):
    ATTACK = "A"

    def __init__(self):
        self.sprite = None
        self.change_to(Soldier.ATTACK)

    def change_to(self, status):
        attacks = [pyglet.image.load('PAK/SHAPE/FORCE/M5H%s000%s.PNG' % (status, frame)) for frame in [1, 2, 3, 4]]
        animation = pyglet.image.Animation.from_image_sequence(attacks, 0.1, True)
        self.sprite = cocos.sprite.Sprite(animation)

    def to(self, point=(0, 0)):
        self.sprite.do(MoveTo(point, 1))


class Hero(object):
    ATTACK = "A"
    RUN = "R"

    def __init__(self):
        self.sprite = None
        self.position = (320, 250)
        self.go()

    def change_to(self, status):
        attacks = [pyglet.image.load('PAK/SHAPE/MAJOR/L4%s1000%s.PNG' % (status, frame)) for frame in
                   [1, 2, 3, 4, 5, 6]]
        animation = pyglet.image.Animation.from_image_sequence(attacks, 0.1, True)
        self.sprite = cocos.sprite.Sprite(animation, position=self.position)

    def go(self):
        self.change_to(Hero.RUN)
        self.to((50, self.sprite.y))

    def to(self, point=(0, 0)):
        self.sprite.do(MoveTo(point, 1))


class Sky(cocos.layer.Layer):
    """
    远处的偏移较小，天空有一张图足矣
    使用宫殿等作近景，偏移稍大
    使用树木等点缀quadMoveBy之后的地面网格
    """

    def __init__(self):
        super(Sky, self).__init__()

        floor = cocos.sprite.Sprite('PAK/SHAPE/BG/FLOOR01.PNG')
        floor.position = 320, 240
        floor.scale =1
        move = QuadMoveBy(delta0=(-120, 0), delta1=(120, 0), delta2=(-120, 0),
                          delta3=(120, 0), duration=0)
        floor.do(move)
        self.add(floor)

        bg = cocos.sprite.Sprite('PAK/SHAPE/BG/BG1-25.PNG')
        bg.position = 320, 480-48
        self.add(bg)

        cei = cocos.sprite.Sprite('PAK/SHAPE/BG/CEI09.PNG')
        cei.position = 320, 480-48
        self.add(cei)






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


if __name__ == "__main__":
    director.init( resizable=True )
    director.show_FPS = True

    # We create a new layer, an instance of HelloWorld
    hello_layer = HelloWorld()

    # A scene that contains the layer hello_layer
    main_scene = cocos.scene.Scene(Square((0, 255, 0, 1), 50, 50, size=10),Sky(), hello_layer,  HUD())

    # And now, start the application, starting with main_scene
    cocos.director.director.run(main_scene)

    # or you could have written, without so many comments:
    #      director.run( cocos.scene.Scene( HelloWorld() ) )
