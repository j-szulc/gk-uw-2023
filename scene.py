from material import BasicMaterial
from sphere import Sphere
from imports import *


class Scene:

    def __init__(self):
        material = BasicMaterial(ambient_color=np.array([0.5, 0, 0]), diffuse_color=np.array([0.5, 0, 0]),
                                     specular_color=np.array([1, 1, 1]), shininess=25)
        self.sphere = Sphere(center=np.array([0, 0, -2]), radius=1, material=material)

    def render_rays(self, rays):
        width = 600
        height = 600
        result = self.sphere.render(rays, [np.array([1, 1, 1]), np.array([2, 100, 1])])  # width*height, 3
        result = result.reshape(width, height, 3)  # width, height, 3
        return result
