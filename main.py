import numpy as np
import matplotlib.pyplot as plt
from rays import *
from material import *
from sphere import *

width = 3000
height = 2000

camera = np.array([0, 0, 1])
camera_direction = np.array([0, 0, -1])

ratio = float(width) / height

x = np.linspace(-ratio, ratio, width)
y = np.linspace(-1, 1, height)
z = np.zeros((1))
screen = np.dstack(np.meshgrid(x,y,z, copy=False)) # height, width, 3
screen = np.swapaxes(screen, 0, 1) # width, height, 3
screen = screen.reshape(width*height, 3) # width * height, 3

camera_pos = np.tile(camera, (width * height, 1)) # width * height, 3

rays = Rays.from_point_pairs(froms=camera_pos, tos=screen) # width*height, 3, 3
# rays = Rays(np.array([[0, 0, 1]]), np.array([[0, 0, -1]])) # width*height, 3, 3

material = BasicMaterial(ambient_color=np.array([0.5, 0, 0]), diffuse_color=np.array([0.5, 0, 0]), specular_color=np.array([1,1,1]), shininess=25)
sphere = Sphere(center=np.array([0, 0, -2]), radius=1, material=material)

result = sphere.render(rays, np.array([1,1,1])) # width*height, 3
result = result.reshape(width, height, 3) # width, height, 3

mask = result[:, :, 2] > 0
image = np.zeros((width, height, 3))
image[mask] = result[mask]

image = np.swapaxes(image, 0, 1)
plt.imsave('image.png', image)
