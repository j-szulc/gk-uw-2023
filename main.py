import numpy as np
import matplotlib.pyplot as plt
from rays import *
from sphere import *

width = 300
height = 200

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

sphere = Sphere(center=np.array([0, 0, -2]), radius=1)

intersections = sphere.intersect(rays) # width*height, 3

intersections = intersections.reshape(width, height, 3) # width, height, 3

image = np.zeros((width, height, 3))

image[intersections[:, :, 2] > 0] = 1
image = np.swapaxes(image, 0, 1)

#
# for i, y in enumerate():
#     for j, x in enumerate(np.linspace(screen[0], screen[2], width)):
#         # image[i, j] = ...
#         print("progress: %d/%d" % (i + 1, height))
#
plt.imsave('image.png', image)