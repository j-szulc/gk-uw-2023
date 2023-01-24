from imports import *
from blinn_phong import *
from rays import Rays
from utils import *

class Primitive:

    def __init__(self, material):
        self.material = material

    def normal_at(self, points):
        raise NotImplementedError()

    def intersect_t(self, rays):
        raise NotImplementedError()

    def render(self, scene, rays, intersect_t, lights):
        rays_previous_shape = rays.flatten()

        intersections = rays.evaluate_at_t(intersect_t)

        to_observer = rays.origins - intersections
        to_observer /= np.linalg.norm(to_observer, axis=1, keepdims=True)

        result = np.empty_like(intersections)
        result[:, :] = self.material.ambient_colors_at(intersections)

        for light in lights:
            to_light = light - intersections
            light_dist = np.linalg.norm(to_light, axis=1, keepdims=True)
            to_light /= light_dist
            light_dist = light_dist[:, 0]

            if rays.ttl > 0:
                new_rays = Rays(intersections, to_light, rays.ttl - 1)
                new_rays.offset(1e-6)
                new_intersect_t, _ = scene.cast_rays(new_rays)
                enlightened = np.asarray(new_intersect_t >= light_dist - 1e-6, dtype=bool)
            else:
                enlightened = np.full_like(light_dist, True, dtype=bool)

            if enlightened.any():
                result[enlightened] += blinn_phong(self.material, intersections[enlightened], self.normal_at(intersections[enlightened]), to_light[enlightened], to_observer[enlightened])

        if rays.ttl > 0:
            new_rays = Rays(intersections, reflect(rays.directions, self.normal_at(intersections)), rays.ttl - 1)
            new_rays.offset(1e-6)
            new_rays_results = scene.cast_and_render(new_rays)
            result += self.material.specular_colors_at(intersections) * new_rays_results

        rays.unflatten(rays_previous_shape)
        return np.clip(np.reshape(result, (*rays_previous_shape, 3)), 0, 1)
