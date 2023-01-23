from material import BasicMaterial
from sphere import Sphere
from imports import *
from utils import *

class Scene:

    def __init__(self):
        material = BasicMaterial(ambient_color=np.array([0.5, 0, 0]), diffuse_color=np.array([0.5, 0, 0]),
                                     specular_color=np.array([1, 1, 1]), shininess=25)
        self.primitives = [
            Sphere(center=np.array([0, 0, 3]), radius=1, material=material),
            Sphere(center=np.array([2, 2, 3]), radius=1, material=material)
        ]
        self.lights = [np.array([5, 5, 3])]

    def render_rays(self, rays):
        width = 600
        height = 600
        result = np.full((width, height, 3), np.nan)
        for primitive in self.primitives:
            result = add_respecting_nans(result, primitive.render(rays, self.lights))  # width, height, 3
        return result
