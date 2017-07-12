#!/usr/bin/env python
# -*- coding: utf-8 -*-

# coding:utf-8
#
import sys


# author: http://blog.csdn.net/cheng830306/article/details/18449431


# import os
# sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../..'))
# 解决程序中要显示中文问题
reload(sys)
sys.setdefaultencoding('utf8')
from pyglet import image, font
from pyglet.gl import *
from pyglet.window import key

from cocos.actions import *
from cocos.director import director
from cocos.layer import Layer
from cocos.layer import ColorLayer
from cocos.scene import Scene
from cocos.sprite import Sprite
from cocos.text import *
from cocos.menu import *

import random
from cocos.audio.effect import Effect

consts_window = {
    "width": 680,
    "height": 700,
    "vsync": True,
    "resizable": True,
    'audio_backend': 'sdl'
}


def get_sprite_test(index):
    d = tests[index]
    return Scene(d(index))


class SpriteLayer(Layer):
    is_event_handler = True  #: enable pyglet's events

    def __init__(self, index=1):
        super(SpriteLayer, self).__init__()
        self.index = index

        self.top_text = "广州德瀚信息信息科技有限公司-年会抽奖"

        self.image = pyglet.resource.image('r1.png', 0.01)
        # self.image = image.AnimationFrame(image.load('r1.png'),0.1)
        self.image.anchor_x = self.image.width / 2
        self.image.anchor_y = self.image.height / 2

        self.rimage = pyglet.resource.image('r2.png', 0.01)
        # self.rimage = image.AnimationFrame(image.load('r2.png'),0.1)
        self.rimage.anchor_x = self.image.width / 2
        self.rimage.anchor_y = self.image.height / 2

        self.bgimage = pyglet.resource.image('bg1.png')
        self.bgimage.anchor_x = self.image.width / 2
        self.bgimage.anchor_y = self.image.height / 2

        self.pressbgimage = pyglet.resource.image('bg2.png')
        self.pressbgimage.anchor_x = self.image.width / 2
        self.pressbgimage.anchor_y = self.image.height / 2

        self.prizeimage = pyglet.resource.image('name.png')
        self.prizeimage.anchor_x = self.image.width / 2
        self.prizeimage.anchor_y = self.image.height / 2

    def on_key_release(self, keys, mod):
        # LEFT: go to previous scene
        # RIGTH: go to next scene
        # ENTER: restart scene
        if keys == key.LEFT:
            self.index -= 1
            if self.index < 1:
                self.index = len(tests)
        elif keys == key.RIGHT:
            self.index += 1
            if self.index > len(tests):
                self.index = 1

        if keys in (key.LEFT, key.RIGHT):
            director.replace(get_sprite_test(self.index))
            return True


class PrizeMenu(Menu):
    def __init__(self):
        super(PrizeMenu, self).__init__()

        self.menu_valign = BOTTOM
        self.menu_halign = RIGHT
        self.font_item['color'] = (0, 0, 0, 255)
        self.font_item_selected['color'] = (32, 16, 32, 255)
        # print dir(self)

        # then add the items
        items = [
            (MenuItem('一等奖', self.prize_go)),
            (MenuItem('二等奖', self.prize_go)),
            (MenuItem('三等奖', self.prize_go)),
            (MenuItem('参与奖', self.prize_go)),

        ]

        # self.create_menu( items, selected_effect=zoom_in(),
        #                   unselected_effect=zoom_out())
        self.create_menu(items, shake(), shake_back())

    def on_quit(self):
        pyglet.app.exit()

    def prize_go(self):
        s = self.parent
        if s.is_begin:
            s.top_notice.element.text = ""
        else:
            # s.stop_num = 1
            s.go_prize()


# def main():

#     pyglet.font.add_directory('.')

#     director.init( resizable=True)
#     director.run( Scene( PrizeMenu() ) )

# if __name__ == '__main__':
#     main()


class StartPrize(SpriteLayer):
    def __init__(self, index):
        super(StartPrize, self).__init__(index)

        self.current_num = 0  # 当前位置
        self.is_begin = False  # 是否已经开始
        self.prize_cycle = 0  # 转动圈数
        self.prize_speed = 0.05  # 初始速度
        self.prize_speed_slow = 0.3  # 慢速度
        self.stop_num = 0  # 停止的位置
        self.alread_get_prize = []  # 已经得奖的人
        self.start_slow = False
        self.can_stop = False
        self.press_go = False

        self.sprite = Sprite(self.image)
        # self.sprite = Sprite( image.Animation([image.AnimationFrame(image.load('r1.png'),0.001)] ))
        self.alread_prize_sprite = Sprite(self.rimage)

        self.bgsprite = Sprite(self.bgimage)
        self.pressbgsprite = Sprite(self.pressbgimage)
        self.prizesprite = Sprite(self.prizeimage)

        self.top_label = Label(self.top_text)
        # 注意是要有个element
        self.top_label.element.x = -250
        self.top_label.element.y = 350
        self.top_label.element.color = (0, 0, 0, 255)
        self.top_label.element.font_size = 20

        self.top_notice = Label("点击中间开始抽奖")
        self.top_notice.element.x = 120
        self.top_notice.element.y = 300
        self.top_notice.element.color = (255, 0, 0, 255)
        self.top_notice.element.font_size = 20

        self.pressbgsprite.do(Hide())
        self.alread_prize_sprite.do(Hide())
        # self.sprite.do(Hide())

    def on_enter(self):
        super(StartPrize, self).on_enter()

        bgcolor = ColorLayer(255, 255, 255, 255, consts_window['width'], consts_window['height'])
        bgcolor.position = (-320, -320)
        # 背景颜色
        self.add(bgcolor)
        # 标题
        self.add(self.top_label)
        self.add(self.top_notice)
        # 转动的背景图
        self.add(self.sprite, z=3)
        self.add(self.alread_prize_sprite, z=3)
        # 人名图
        self.add(self.prizesprite, z=4)
        # 背景图
        self.add(self.bgsprite, z=1)
        self.add(self.pressbgsprite, z=1)

        self.position = 320, 320

        # menu = PrizeMenu()
        # menu.position = (-320,-320)
        # self.add(menu)

        # self.sprite.do( Repeat(Rotate( 360, 4 )  ))

    def on_key_press(self, keys, mod):
        super(StartPrize, self).on_key_release(keys, mod)
        if keys == key.ENTER:
            if self.is_begin:
                self.top_notice.element.text = "正在抽奖中。。"
            else:
                self.press_go = True
                self.go_prize()
            return True

    def on_key_release(self, keys, mod):
        super(StartPrize, self).on_key_release(keys, mod)
        if keys == key.ENTER:
            if self.press_go:
                self.prize_cycle = 0
                self.can_stop = True
                self.press_go = False
            return True
        if keys == key.S:
            # self.stop_prize()
            return True

    def on_mouse_press(self, x, y, buttons, modifiers):
        px, py = director.get_virtual_coordinates(x, y)
        # print px,py
        if px > 188 and px < 450 and py > 188 and py < 450:
            if self.is_begin:
                self.top_notice.element.text = "正在抽奖中。。"
            else:
                self.press_go = True
                self.go_prize()

    def on_mouse_release(self, x, y, buttons, modifiers):
        px, py = director.get_virtual_coordinates(x, y)
        if self.press_go:
            self.prize_cycle = 0
            self.can_stop = True
            self.press_go = False

    def rotate_select(self, dt):

        if (self.current_num >= 24):
            self.current_num = 0
            self.prize_cycle += 1

        if (self.prize_cycle > 1 and self.can_stop):
            if (not self.start_slow):
                # 减速
                self.unschedule(self.rotate_select)
                self.schedule_interval(self.rotate_select, self.prize_speed_slow)
                self.start_slow = True

                # print self.alread_get_prize
        # print "stopnum" , self.stop_num
        # print "prize_cycle" , self.prize_cycle
        # print "current_num" , self.current_num
        # print self.current_num
        # 注意rotate_select是要两个参数的
        self.sprite.rotation = self.sprite.rotation + 15
        self.alread_prize_sprite.rotation = self.alread_prize_sprite.rotation + 15

        if self.current_num in self.alread_get_prize:
            self.sprite.do(Hide())
            self.alread_prize_sprite.do(Show())
        else:
            self.alread_prize_sprite.do(Hide())
            self.sprite.do(Show())
        effect = Effect('1.wav')
        effect.play()

        if (self.prize_cycle > 2 and self.stop_num == self.current_num and self.can_stop):
            self.stop_prize()
            return True

        self.current_num += 1

    def get_random(self):
        r = random.randint(0, 23)
        if r in self.alread_get_prize:
            r = self.get_random()
        return r

    def go_prize(self):
        self.current_num = 0
        self.sprite.rotation = 0
        self.alread_prize_sprite.rotation = 0
        self.prize_cycle = 0
        self.stop_num = self.get_random()
        # self.stop_num = 0

        if self.stop_num in self.alread_get_prize:
            self.top_notice.element.text = "error, alread get prize"
            return False
        self.top_notice.element.text = "正在抽奖中。。"
        self.start_slow = False
        self.can_stop = False

        self.is_begin = True

        # 定时器
        self.schedule_interval(self.rotate_select, self.prize_speed)
        # self.schedule(self.rotate_select)
        self.bgsprite.do(Hide())
        self.pressbgsprite.do(Show())

    def stop_prize(self):
        self.alread_get_prize.append(self.current_num)
        self.is_begin = False
        effect = Effect('2.wav')
        effect.play()
        self.top_notice.element.text = ""

        self.pressbgsprite.do(Hide())
        self.bgsprite.do(Show())
        self.unschedule(self.rotate_select)


tests = {
    1: StartPrize,
}


def main():
    director.init(**consts_window)
    # director.show_FPS = True
    director.run(get_sprite_test(1))


if __name__ == '__main__':
    main()
