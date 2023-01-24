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

red_solid_material = BasicMaterial(ambient_color=np.array([1., 0, 0]), diffuse_color=np.array([1., 0, 0]), specular_color=np.array([0, 0, 0]), shininess=0)

portal1 = Portal(np.array([3., 0, 5.]), np.array([2., 0., 0.]), np.array([0., 2., 0.]),
            BasicMaterial(ambient_color=np.array([0, 0.1, 0]), diffuse_color=np.array([0, 0.5, 0]),
                          specular_color=np.array([0., 0., 0.]), shininess=10))
portal2 = Portal(np.array([0., 0, 6.]), np.array([2., 0., 0.]), np.array([0., 2., 0.]),
                BasicMaterial(ambient_color=np.array([0, 0.1, 0]), diffuse_color=np.array([0, 0.5, 0]),
                              specular_color=np.array([0., 0., 0.]), shininess=10))

primitives = [
    Sky(),
    Quad(np.array([5., -100., -100.]), np.array([0., 0., 10.]), np.array([0., 10., 0]), red_solid_material),
    Sphere(np.array([-1., 2., 10]), 1, green_material),
]

# self.lights = [np.array([0, -100, 0])]
lights = [Light([2.,5.,0.])]

scene = Scene(width, height, wres, hres, primitives, lights, debug_rays)