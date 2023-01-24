from imports import *

from utils import *
from primitive import *

class Sphere(Primitive):
    def __init__(self, center, radius, material):
        super().__init__(material)
        self.center = center
        self.radius = radius
        self.radius_sq = radius ** 2

    def normal_at(self, points):
        """
        :param point: N, 3
        :return: N, 3
        """
        return (points - self.center) / self.radius

    def intersect_t(self, rays, fill_value=np.nan):
        """
        :param rays: Rays
        :return: number_of_rays, 3 (t-value of intersection point or [fill_value])
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

        result_t = np.full_like(roots_minus_t, fill_value)

        result_t[roots_plus_t >= 0] = roots_plus_t[roots_plus_t >= 0]
        result_t[roots_minus_t >= 0] = roots_minus_t[roots_minus_t >= 0]

        return result_t
