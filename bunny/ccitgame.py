# coding=utf-8

# 1 - Import library
import math
import time
import pyglet
import cocos
from cocos.director import director
from cocos.text import *
from cocos.layer import Layer
from cocos.sprite import Sprite
from cocos.actions.interval_actions import MoveBy, MoveTo, RotateTo, Bezier
from cocos.actions.instant_actions import CallFuncS
from random import randint
import cocos.euclid as eu
import cocos.collision_model as cm


class Entity(object):
    def die(self, sprite):
        sprite.kill()


class BadGuy(Entity):
    def __init__(self, layer):
        super(BadGuy, self).__init__()
        image = pyglet.resource.image("resources/images/badguy.png")
        self.sprite = Sprite(image)
        self.layer = layer

    def born(self, index):
        self.sprite.position = index
        self.cshape = cm.AARectShape(eu.Vector2(index[0], index[1]), self.sprite.width, self.sprite.height)
        self.layer.add(self.sprite)
        move_speed = randint(123, 234) / 100.0
        self.sprite.do(MoveTo((0, index[1]), move_speed) + CallFuncS(self.die))


class Arrow(Entity):
    def __init__(self, by):
        super(Arrow, self).__init__()
        image = pyglet.resource.image("resources/images/bullet.png")
        self.sprite = Sprite(image)
        self.sprite.position = by.sprite.get_rect().center
        self.layer = by.layer
        self.by = by

    def to(self, target):
        angle = math.atan2(target[1] - self.by.position[1], target[0] - self.by.position[0]) * 360 / 2 / math.pi
        self.sprite.rotation = -angle
        self.layer.add(self.sprite)
        self.sprite.do(MoveTo(target, 0.3) + CallFuncS(self.die))

    def toA(self, target):
        angle = math.atan2(target[1] - self.by.position[1], target[0] - self.by.position[0]) * 360 / 2 / math.pi
        self.sprite.rotation = -angle
        self.layer.add(self.sprite)
        circulo = cocos.path.Bezier((7, 7), (0, 1), (630, 237), (630, -234))
        self.sprite.do(Bezier(circulo, 2) + CallFuncS(self.die))


class Hero():
    def __init__(self, layer):
        image = pyglet.resource.image("resources/images/dude.png")
        self.sprite = Sprite(image)
        self.sprite.position = 100, 100
        self.speed = 5
        self.position = self.sprite.position
        self.layer = layer
        self.layer.add(self.sprite)

    def toUp(self):
        if self.position[1] < cocos.director.director.get_window_size()[1]:
            self.sprite.do(MoveBy((0, self.speed), 0.1))

    def toLeft(self):
        if self.position[0] > 0:
            self.sprite.do(MoveBy((-self.speed, 0), 0.1))

    def toDown(self):
        if self.position[1] > 0:
            self.sprite.do(MoveBy((0, -self.speed), 0.1))

    def toRight(self):
        if self.position[0] < cocos.director.director.get_window_size()[0]:
            # self.sprite.do(MoveBy((self.speed, 0), 0.1))
            self.sprite.position = self.sprite.position[0] + self.speed, self.sprite.position[1]

    def attack(self, target):
        angle = math.atan2(target[1] - self.sprite.position[1], target[0] - self.sprite.position[0]) * 360 / 2 / math.pi
        self.sprite.rotation = -angle
        arrow = Arrow(self)
        arrow.to(target)
        return arrow

    def attackA(self, target):
        arrow = Arrow(self)
        arrow.toA(target)


class GameLayer(Layer):
    is_event_handler = True

    def __init__(self):
        super(GameLayer, self).__init__()
        self.hero = Hero(self)
        self.text = cocos.text.Label("", x=100, y=0)
        self.add(self.text)
        self.keys_pressed = set()
        self.update_text()
        self.schedule_interval(self.bornBadGuy, 0.5, self)

    def bornBadGuy(self, dt, layer):
        position = 640, randint(0 + 30, 480 - 30)
        bad_guy = BadGuy(layer)
        bad_guy.born(position)
        badguys.append(bad_guy)

    def on_key_press(self, key, modifiers):
        self.keys_pressed.add(key)

    def on_key_release(self, key, modifiers):
        self.keys_pressed.remove(key)

    def on_mouse_press(self, x, y, buttons, modifiers):
        self.mouse_target = director.get_virtual_coordinates(x, y)
        arrow = self.hero.attack(self.mouse_target)
        arrows.append(arrow)

    def draw(self, *args, **kwargs):
        self.update_text()
        for arrow in arrows:
            for badguy in badguys:
                if arrow.sprite.get_rect().intersect(badguy.sprite.get_rect()):
                    print arrow.sprite.get_rect(), badguy.sprite.get_rect()
                    arrow.sprite.delete()
                    arrows.remove(arrow)
                    badguy.sprite.delete()
                    badguys.remove(badguy)

    def update_text(self):
        key_names = [pyglet.window.key.symbol_string(k) for k in self.keys_pressed]
        if key_names.__contains__("W"):
            self.hero.toUp()
        if key_names.__contains__("A"):
            self.hero.toLeft()
        if key_names.__contains__("S"):
            self.hero.toDown()
        if key_names.__contains__("D"):
            self.hero.toRight()
        text = 'Keys: ' + ','.join(key_names)
        # Update self.text
        self.text.element.text = text


class BgLayer(Layer):
    def __init__(self):
        super(BgLayer, self).__init__()
        self.grass = pyglet.resource.image("resources/images/grass.png")
        self.castle = pyglet.resource.image("resources/images/castle.png")
        window_size = cocos.director.director.get_window_size()
        for x in range(window_size[0] / self.grass.width + 1):
            for y in range(window_size[1] / self.grass.height + 1):
                self.add_sprite(self.grass, (x * 100, y * 100 + 50))
        self.add_sprite(self.castle, (50, 100))
        self.add_sprite(self.castle, (50, 200))
        self.add_sprite(self.castle, (50, 300))
        self.add_sprite(self.castle, (50, 400))

    def add_sprite(self, image, position):
        sprite = Sprite(image)
        sprite.position = position
        self.add(sprite)


class MessageLayer(Layer):
    def __init__(self):
        super(MessageLayer, self).__init__()
        self.msg = str((90 - int(time.clock())) / 60).zfill(2) + ":" + str((90 - int(time.clock())) % 60).zfill(2)
        self.score = Label(self.msg, font_size=24,
                           font_name='Edit Undo Line BRK',
                           color=(255, 255, 255, 255),
                           anchor_x='right',
                           anchor_y='top')
        self.score.position = (640 - 5, 480 - 5)
        self.add(self.score)

    def draw(self):
        super(MessageLayer, self).draw()
        self.msg = str((90 - int(time.clock())) / 60).zfill(2) + ":" + str((90 - int(time.clock())) % 60).zfill(2)
        self.score.element.text = self.msg


class HealthLayer(Layer):
    def __init__(self):
        super(HealthLayer, self).__init__()
        self.hp = 194
        self.health_bar_image = pyglet.resource.image("resources/images/healthbar.png")
        self.health_image = pyglet.resource.image("resources/images/health.png")

        self.health_bar = Sprite(self.health_bar_image)
        self.health_bar.anchor = (0, 0)
        self.health_bar.position = (0 + 5 + 100, 480 - 5 - 10)

    def update_health(self):
        self.add(self.health_bar)
        for i in range(self.hp):
            h = Sprite(self.health_image)
            h.anchor = (0, 0)
            h.position = (i + 8, 480 - 8 - 7)
            self.add(h)

    def draw(self):
        super(HealthLayer, self).draw()
        self.hp -= 1
        for children in self.get_children():
            self.remove(children)
        self.update_health()


class HUD(Layer):
    def __init__(self):
        super(HUD, self).__init__()
        self.add(MessageLayer(), name='msg')
        self.add(HealthLayer(), name='health')


if __name__ == "__main__":
    arrows = []
    badguys = []
    cocos.director.director.init()
    main_scene = cocos.scene.Scene()
    main_scene.add(BgLayer())
    main_scene.add(GameLayer())
    main_scene.add(HUD())
    print "window size: ", cocos.director.director.get_window_size()
    cocos.director.director.run(main_scene)
