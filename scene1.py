from material import BasicMaterial
from sphere import *
from imports import *
from utils import *
from sky import *
from quad import *
from scene import *
from portal import *

red_material = BasicMaterial(ambient_color=np.array([0.1, 0, 0]), diffuse_color=np.array([0.3, 0, 0]),
                             specular_color=np.array([1, 1, 1]), shininess=25)

green_material = BasicMaterial(ambient_color=np.array([0, 0.1, 0]), diffuse_color=np.array([0, 0.3, 0]),
                               specular_color=np.array([1, 1, 1]), shininess=25)

blue_material = BasicMaterial(ambient_color=np.array([0, 0, 0.1]), diffuse_color=np.array([0, 0, 0.3]),
                              specular_color=np.array([1, 1, 1]), shininess=25)

gray_material = BasicMaterial(ambient_color=np.array([0.1, 0.1, 0.1]), diffuse_color=np.array([0.1, 0.1, 0.1]),
                              specular_color=np.array([1, 1, 1]), shininess=10)

quad = Quad(np.array([3., 0, 6.]), np.array([2., 0., 0.]), np.array([0., 2., 0.]),
            BasicMaterial(ambient_color=np.array([0, 0.1, 0]), diffuse_color=np.array([0, 0.5, 0]),
                          specular_color=np.array([0., 0., 0.]), shininess=10))
portal = Portal(np.array([0., 0, 6.]), np.array([2., 0., 0.]), np.array([0., 2., 0.]),
                BasicMaterial(ambient_color=np.array([0, 0.1, 0]), diffuse_color=np.array([0, 0.5, 0]),
                              specular_color=np.array([0., 0., 0.]), shininess=10))
portal.pair_quad(quad)
primitives = [
    Sky(),
    Sphere(np.array([0, 1000, 0]), 900, gray_material),
    Sphere(np.array([0, 0, -40]), 30, red_material),
    Sphere(np.array([-3, 0, 5]), 1, red_material),
    Sphere(np.array([0, 0, 5]), 1, green_material),
    Sphere(np.array([3, 0, 5]), 1, blue_material),
    quad,
    portal,
    Sphere(np.array([6, 0, 5]), 1, blue_material)
]

# self.lights = [np.array([0, -100, 0])]
lights = [np.array([0, -100, 0]), np.array([20., 20., 20.])]

scene = Scene(width, height, wres, hres, primitives, lights, debug_rays)