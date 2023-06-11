from ursina import Entity, Vec4
from panda3d.core import DirectionalLight, AmbientLight

class Sun(Entity):
    def __init__(self, target):
        super().__init__()

        self.sun = DirectionalLight("sun")

        self.sun.getLens().setNearFar(-120, 300)
        self.sun.getLens().setFilmSize((150, 150))

        self.pivot = render.attachNewNode(self.sun)
        self.pivot.lookAt((1,-1,-1))
        render.setLight(self.pivot)

        self.lighting = AmbientLight('lighting')
        self.lighting.setColor(Vec4(0.4, 0.5, 0.6, 0) * 1.3)
        self.parent = render.attachNewNode(self.lighting)
        render.setLight(self.parent)

        self.target = target

    def update(self):
        self.sun.setShadowCaster(True, 4000, 4000)
        self.pivot.setPos(self.target.world_position)
