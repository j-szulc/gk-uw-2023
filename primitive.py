from imports import *
from blinn_phong import *

class Primitive:

    def __init__(self, material):
        self.material = material

    def normal_at(self, points):
        raise NotImplementedError()

    def intersect(self, rays):
        raise NotImplementedError()

    def render(self, rays, lights):
        intersections = self.intersect(rays)
        mask = ~np.isnan(intersections[:, 0])

        to_observer = rays.origins[mask] - intersections[mask]
        to_observer /= np.linalg.norm(to_observer, axis=1, keepdims=True)

        result = np.full_like(intersections, np.nan)
        result[mask] = self.material.ambient_colors_at(intersections[mask])

        for light in lights:
            to_light = light - intersections[mask]
            to_light /= np.linalg.norm(to_light, axis=1, keepdims=True)

            result[mask] += blinn_phong(self.material, intersections[mask], self.normal_at(intersections[mask]), to_light, to_observer)

        return np.clip(result, 0, 1)
