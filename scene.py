from material import BasicMaterial
from sphere import *
from imports import *
from utils import *
from sky import *
from quad import *
from portal import *

class Scene:

    def __init__(self, width, height, wres, hres, primitives, lights, debug_rays = lambda rays: None):

        self.width = width
        self.height = height
        self.wres = wres
        self.hres = hres
        self.debug_rays = debug_rays
        self.primitives = primitives
        self.lights = lights

    def cast_rays(self, rays):

        if rays.debug:
            self.debug_rays(rays)

        rays_previous_shape = rays.flatten()
        ts = [primitive.intersect_t(rays) for primitive in self.primitives]
        t = np.stack(ts, axis=1)
        targmin = np.nanargmin(t, axis=1)
        tmin = np.take_along_axis(t, np.expand_dims(targmin, axis=1), axis=1).squeeze(axis=1)

        targmin[(tmin == np.inf) | (tmin == np.nan)] = 0    # np.nargmin can't be trusted with only infs and nans
        tmin[(tmin == np.inf) | (tmin == np.nan)] = np.inf  # np.nargmin can't be trusted with only infs and nans

        rays.unflatten(rays_previous_shape)
        return tmin, targmin

    def render(self, rays, tmin, targmin):

        rays_previous_shape = rays.flatten()
        n_of_rays = rays.n_of_rays()

        result = np.full((n_of_rays, 3), np.nan)

        for i, primitive in enumerate(self.primitives):
            mask = targmin == i
            result[mask] = primitive.render(self, rays[mask], tmin[mask], self.lights)

        result = result.reshape((*rays_previous_shape, 3))
        return result

    def cast_and_render(self, rays):
        tmin, targmin = self.cast_rays(rays)
        return self.render(rays, tmin, targmin)
