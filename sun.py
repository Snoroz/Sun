from ursina import Entity
from panda3d.core import DirectionalLight

class Sun(Entity):
    def __init__(self, player):
        super().__init__()

        self.lighting = DirectionalLight("lighting")

        self.lighting.getLens().setNearFar(-120, 300)
        self.lighting.getLens().setFilmSize((150, 150))

        self.pivot = render.attachNewNode(self.lighting)
        self.pivot.lookAt((1,-1,-1))
        render.setLight(self.pivot)

        self.player = player

    def update(self):
        self.lighting.setShadowCaster(True, 4000, 4000)
        self.pivot.setPos(self.player.world_position)