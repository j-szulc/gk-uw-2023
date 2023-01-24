import pygame

from imports import *
from rays import *
from material import *
from sphere import *
from viewer import *
from time import time
from scene import *
from camera import *

last_update_time = time()
width = 600
height = 600
wres = 200
hres = 200
scene = Scene(width, height, wres, hres)
camera = Camera(width=width, height=height, wres=wres, hres=hres,position=[0, 0, 0], direction=[0, 0, 1], up=[0, 1, 0])
camera2 = Camera(width=width, height=height, wres=wres, hres=hres,position=[1, 1, 0], direction=[0, 0, 1], up=[0, 1, 0])

def update(events):
    global last_update_time
    global scene
    print("FPS: ", 1/(time() - last_update_time))
    print(camera.position)
    last_update_time = time()

    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pygame.K_w]:
        camera.move_forward(1)
    if keys_pressed[pygame.K_s]:
        camera.move_forward(-1)
    if keys_pressed[pygame.K_a]:
        camera.move_right(-1)
    if keys_pressed[pygame.K_d]:
        camera.move_right(1)
    if keys_pressed[pygame.K_LEFT]:
        camera.rotate_right(0.1)
    if keys_pressed[pygame.K_RIGHT]:
        camera.rotate_right(-0.1)
    if keys_pressed[pygame.K_UP]:
        camera.rotate_up(0.1)
    if keys_pressed[pygame.K_DOWN]:
        camera.rotate_up(-0.1)

    rays = camera.get_rays()

    tmin, targmin = scene.cast_rays(rays)
    result = scene.render(rays, tmin, targmin)

    def overlay(surface):
        rays.project(camera2)

    return result*255, overlay


viewer = Viewer(update, (width, height))
viewer.start()
