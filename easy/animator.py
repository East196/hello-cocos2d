import pyglet

image_frames = ("PALAIS01.PNG", "PALAIS02.PNG", "PALAIS03.PNG")
images = map(lambda img: pyglet.image.load(img), image_frames)
animation = pyglet.image.Animation.from_image_sequence(images, 0.5)
animSprite = pyglet.sprite.Sprite(animation)

w = animSprite.width
h = animSprite.height
win = pyglet.window.Window(width=w, height=h)


pyglet.gl.glClearColor(1, 1, 1, 1)


@win.event
def on_draw():
    win.clear()
    animSprite.draw()


pyglet.app.run()
