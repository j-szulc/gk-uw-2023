import numpy as np
from utils import *

class Sphere:
    def __init__(self, center, radius):
        self.center = center
        self.radius_sq = radius ** 2

    def intersect(self, rays):
        """
        :param rays: Rays
        :return: number_of_rays, 3 (intersection point or None)
        """
        # ray(t) = a+b*t
        # sphere: |p-c| = r
        # |a+b*t-c|^2 = r^2
        # (b*t+c-a).(b*t+c-a) = r^2
        # t^2*(b.b) + 2t*(b.(c-a)) + (c-a).(c-a) - r^2 = 0
        b = 2 * np.sum(rays.directions * (self.center - rays.origins), axis=1)
        c = np.sum((self.center - rays.origins) ** 2, axis=1) - self.radius_sq
        a = np.ones(1)
        roots_minus_t, roots_plus_t = solve_quadratic(a, b, c)

        result_t = np.empty_like(roots_minus_t)
        mask = roots_minus_t >= 0

        result_t[mask] = roots_minus_t[mask]
        result_t[~mask] = roots_plus_t[~mask]

        return rays.evaluate_at_t(result_t)
