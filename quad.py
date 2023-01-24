import numpy as np

from imports import *

from utils import *
from primitive import *
from material import *

class Quad(Primitive):
    def __init__(self, corner, x, y, material):
        super().__init__(material)
        self.corner = corner
        self.x = x
        self.y = y
        self.normal = -np.cross(x, y)

    def normal_at(self, points):
        """
        :param point: N, 3
        :return: N, 3
        """
        return self.normal

    def get_basis(self):
        return np.vstack([self.x, self.y, self.normal]).T

    def intersect_t(self, rays):
        """
        :param rays: Rays
        :return: number_of_rays, 3 (t-value of intersection point or [fill_value])
        """

        plane_altitude = project(self.corner - rays.origins, -self.normal)
        orthogonal_direction = project(rays.directions, -self.normal)

        t = np.linalg.norm(plane_altitude, axis=1) / np.linalg.norm(orthogonal_direction, axis=1)
        proj_x = np.full_like(t, np.nan)
        proj_y = np.full_like(t, np.nan)
        proj_z = np.full_like(t, np.nan)

        mask = t > 0

        intersections = rays[mask].evaluate_at_t(t[mask])

        proj_x[mask] = np.dot(intersections - self.corner, self.x) / np.sum(self.x ** 2)
        proj_y[mask] = np.dot(intersections - self.corner, self.y) / np.sum(self.y ** 2)
        proj_z[mask] = np.dot(intersections - self.corner, self.normal)

        mask &= proj_x > 0
        mask &= proj_x < 1
        mask &= proj_y > 0
        mask &= proj_y < 1
        mask &= proj_z < 1e-3
        mask &= proj_z > -1e-3

        t[~mask] = np.nan

        return t
