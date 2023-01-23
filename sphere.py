import numpy as np
from utils import *

class Sphere:
    def __init__(self, center, radius, ambient_color, diffuse_color, specular_color, shininess):
        self.center = center
        self.radius = radius
        self.radius_sq = radius ** 2
        self.ambient_color = ambient_color
        self.diffuse_color = diffuse_color
        self.specular_color = specular_color
        self.shininess = shininess

    def normal_at(self, points):
        """
        :param point: N, 3
        :return: N, 3
        """
        return (points - self.center) / self.radius

    def intersect(self, rays):
        """
        :param rays: Rays
        :return: number_of_rays, 3 (intersection point or None)
        """
        # ray(t) = a+b*t
        # sphere: |p-c| = r
        # |a+b*t-c|^2 = r^2
        # (b*t+a-c).(b*t+a-c) = r^2
        # t^2*(b.b) + 2t*(b.(a-c)) + (c-a).(c-a) - r^2 = 0
        b = 2 * np.sum(rays.directions * (rays.origins-self.center), axis=1)
        c = np.sum((self.center - rays.origins) ** 2, axis=1) - self.radius_sq
        a = np.ones(1)
        roots_minus_t, roots_plus_t = solve_quadratic(a, b, c)

        result_t = np.full_like(roots_minus_t, np.nan)

        result_t[roots_plus_t >= 0] = roots_plus_t[roots_plus_t >= 0]
        result_t[roots_minus_t >= 0] = roots_minus_t[roots_minus_t >= 0]

        result = rays.evaluate_at_t(result_t)
        return result

    def render(self, rays, light):
        intersections = self.intersect(rays)
        mask = ~np.isnan(intersections[:, 0])

        to_observer = rays.origins[mask] - intersections[mask]
        to_observer /= np.linalg.norm(to_observer, axis=1, keepdims=True)

        to_light = light - intersections[mask]
        to_light /= np.linalg.norm(to_light, axis=1, keepdims=True)

        result = np.full_like(intersections, np.nan)
        result[mask] = self.blinn_phong(intersections[mask], to_light, to_observer)

        # result[mask] /= np.linalg.norm(result[mask], axis=1, keepdims=True)
        return result