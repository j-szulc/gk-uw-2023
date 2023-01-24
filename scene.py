from material import BasicMaterial
from sphere import Sphere
from imports import *
from utils import *
from sky import *
from skimage.transform import resize

class Scene:

    def __init__(self, width, height, wres, hres):

        self.width = width
        self.height = height
        self.wres = wres
        self.hres = hres

        red_material = BasicMaterial(ambient_color=np.array([0.1, 0, 0]), diffuse_color=np.array([0.5, 0, 0]),
                                 specular_color=np.array([1, 1, 1]), shininess=25)

        green_material = BasicMaterial(ambient_color=np.array([0, 0.1, 0]), diffuse_color=np.array([0, 0.5, 0]),
                                     specular_color=np.array([1, 1, 1]), shininess=25)

        blue_material = BasicMaterial(ambient_color=np.array([0, 0, 0.1]), diffuse_color=np.array([0, 0, 0.5]),
                                     specular_color=np.array([1, 1, 1]), shininess=25)

        gray_material = BasicMaterial(ambient_color=np.array([0.1, 0.1, 0.1]), diffuse_color=np.array([0.1, 0.1, 0.1]),
                                     specular_color=np.array([1, 1, 1]), shininess=10)

        self.primitives = [
            Sky(),
            Sphere(np.array([0, 1000, 0]), 900, gray_material),
            Sphere(np.array([-3, 0, 5]), 1, red_material),
            Sphere(np.array([0, 0, 5]), 1, green_material),
            Sphere(np.array([3, 0, 5]), 1, blue_material)
        ]

        self.lights = [np.array([0, -100, 0])]

    def cast_rays(self, rays):
        rays.flatten()
        ts = [primitive.intersect_t(rays) for primitive in self.primitives]
        t = np.stack(ts, axis=1)
        targmin = np.nanargmin(t, axis=1)
        tmin = np.take_along_axis(t, np.expand_dims(targmin, axis=1), axis=1).squeeze(axis=1)

        targmin[(tmin == np.inf) | (tmin == np.nan)] = 0    # np.nargmin can't be trusted with only infs and nans
        tmin[(tmin == np.inf) | (tmin == np.nan)] = np.inf  # np.nargmin can't be trusted with only infs and nans

        return tmin, targmin

    def render(self, rays, tmin, targmin):

        result = np.full((self.wres * self.hres, 3), np.nan)

        for i, primitive in enumerate(self.primitives):
            mask = targmin == i
            result[mask] = primitive.render(self, rays[mask], tmin[mask], self.lights)

        result = result.reshape((self.wres, self.hres, 3))
        return resize(result, (self.width, self.height), anti_aliasing=True)
