from material import BasicMaterial
from sphere import *
from imports import *
from utils import *
from sky import *
from quad import *
from portal import *

class Scene:

    def __init__(self, width, height, wres, hres, primitives, lights, debug_rays = lambda rays: None, portals=None):

        self.width = width
        self.height = height
        self.wres = wres
        self.hres = hres
        self.debug_rays = debug_rays
        self.primitives = primitives
        self.lights = lights
        if portals is None:
            portals = []
        self.portals = portals

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

    def find_routes(self, origins, destination):

        # check direct

        direct = destination - origins
        direct_dist = np.linalg.norm(direct, axis=1, keepdims=True)
        direct /= direct_dist
        direct_dist = direct_dist[:, 0]

        new_rays = Rays(origins, direct, 1)
        new_rays.offset(1e-6)
        new_intersect_t, _ = self.cast_rays(new_rays)
        enlightened = np.asarray(new_intersect_t >= direct_dist - 1e-6, dtype=bool)

        yield direct, enlightened

        # check portals

        for portal in self.portals:

            # FIXME not working
            fake_reflection = portal.paired_quad.corner + ((origins - portal.corner) @ portal.transform_to_paired)
            indirect = destination - fake_reflection
            corresponding_indirect = (indirect - portal.paired_quad.corner) @ np.linalg.inv(portal.paired_quad.transform_to_paired) + portal.corner
