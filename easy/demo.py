#
# cocos2d
# http://python.cocos2d.org
#

from __future__ import division, print_function, unicode_literals

# This code is so you can run the samples without installing the package
import sys
import os

from cocos.euclid import Vector2

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
#

import cocos


class GameScene(cocos.scene.Scene):

    def __init__(self):
        super(GameScene, self).__init__()

    def create_layer(self):
        layer = cocos.layer.Layer()
        # a cocos.text.Label is a wrapper of pyglet.text.Label
        # with the benefit of being a cocosnode
        label = cocos.text.Label('Hello, World!',
                                 font_name='Times New Roman',
                                 font_size=32,
                                 anchor_x='center', anchor_y='center')

        label.position = 320, 240
        layer.add(label)


        return layer


if __name__ == "__main__":
    # director init takes the same arguments as pyglet.window
    cocos.director.director.init()

    # A scene that contains the layer hello_layer
    main_scene = GameScene()
    main_scene.add(main_scene.create_layer())

    # And now, start the application, starting with main_scene
    cocos.director.director.run(main_scene)

    # or you could have written, without so many comments:
    #      director.run( cocos.scene.Scene( HelloWorld() ) )
