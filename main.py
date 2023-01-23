from imports import *
from rays import *
from material import *
from sphere import *
from viewer import *
from time import time
from scene import *

last_update_time = time()
scene = Scene()
def update(events):
    global last_update_time
    global scene
    print("FPS: ", 1/(time() - last_update_time))
    last_update_time = time()
    print(events)
    width = 600
    height = 600

    ratio = float(width) / height
    camera = np.array([0, 0, 1])

    x = np.linspace(-ratio, ratio, width)
    y = np.linspace(-1, 1, height)
    z = np.zeros((1))
    screen = np.dstack(np.meshgrid(x,y,z)) # height, width, 3
    screen = np.swapaxes(screen, 0, 1) # width, height, 3
    screen = screen.reshape(width*height, 3) # width * height, 3

    camera_pos = np.tile(camera, (width*height, 1)) # width * height, 3

    rays = Rays.from_point_pairs(froms=camera_pos, tos=screen) # width*height, 3, 3
    rays.unflatten((width, height))
    # rays = Rays(np.array([[0, 0, 1]]), np.array([[0, 0, -1]])) # width*height, 3, 3

    result = scene.render_rays(rays)
    mask = result[:, :, 2] > 0
    image = np.zeros((width, height, 3))
    image[mask] = result[mask]

    return image*255

viewer = Viewer(update, (600, 600))
viewer.start()
