

class OrbitCameraAction(SpriteLayer):

    def on_enter(self):
        super(OrbitCameraAction, self).on_enter()
        sprite1 = Sprite(self.image_sister1)
        sprite2 = Sprite(self.image_sister2)

        self.add(sprite1)
        self.add(sprite2)
        sprite1.position = (20, 100)
        sprite2.position = (20, 300)

        orbit1 = OrbitCamera(radius=10, delta_radius=0, angle_z=45, delta_z=180, angle_x=90, delta_x=0)
        orbit2 = OrbitCamera(radius=10, delta_radius=0, angle_z=45, delta_z=180, angle_x=90, delta_x=0)
        sprite1.do(orbit1)
        sprite2.do(orbit2)