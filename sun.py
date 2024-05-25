from panda3d.core import Vec4, DirectionalLight, AmbientLight

class Sun:
    def __init__(self, target, intensity=1.25, resolution=4096):
        super().__init__()

        self.sun = DirectionalLight('sun')

        self.sun.getLens().setNearFar(-120, 300)
        self.sun.getLens().setFilmSize((150, 150))

        self.pivot = render.attachNewNode(self.sun)
        self.pivot.lookAt((1,-1,-1))
        render.setLight(self.pivot)

        self.lighting = AmbientLight('lighting')
        self.lighting.setColor(Vec4(.4, .5, .6, 0) * intensity)
        self.parent = render.attachNewNode(self.lighting)
        render.setLight(self.parent)

        self.target = target
        self.resolution = resolution
        
        taskMgr.add(self.update, 'update')

    def update(self, task):
        self.sun.setShadowCaster(True, self.resolution, self.resolution)
        self.pivot.setPos((self.target.world_x, 0, self.target.world_z))
        
        return task.cont
