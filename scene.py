from material import BasicMaterial
from sphere import Sphere
from imports import *
from utils import *
from sky import *

class Scene:

    def __init__(self, width, height):

        self.width = width
        self.height = height

        material = BasicMaterial(ambient_color=np.array([0.5, 0, 0]), diffuse_color=np.array([0.5, 0, 0]),
                                 specular_color=np.array([1, 1, 1]), shininess=25)

        self.primitives = [Sky(), Sphere(np.array([0, 1000, 0]), 900, material)]
        for i in range(3):
            for j in range(3):
                self.primitives.append(Sphere(center=np.array([i, j, 3]), radius=0.5, material=material))
        self.lights = [np.array([0.5, 0.5, 2.9])]

    def cast_rays(self, rays):
        rays.flatten()
        ts = [primitive.intersect_t(rays) for primitive in self.primitives]
        t = np.stack(ts, axis=1)
        targmin = np.nanargmin(t, axis=1)
        tmin = np.take_along_axis(t, np.expand_dims(targmin, axis=1), axis=1).squeeze(axis=1)

        targmin[(tmin == np.inf) | (tmin == np.nan)] = 0 # np.nargmin can't be trusted with only infs and nans

        result = np.full((self.width * self.height, 3), np.nan)

        for i, primitive in enumerate(self.primitives):
            mask = targmin == i
            result[mask] = primitive.render(rays[mask], ts[i][mask], self.lights)

        result = result.reshape((self.width, self.height, 3))
        return result
