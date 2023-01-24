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
scene = Scene(width, height)
camera = Camera(width=width, height=height, position=[0, 0, 0], direction=[0, 0, 1], up=[0, 1, 0])

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
    print(np.dot(camera.direction, camera.up))
    # for event in events:
    #     if event.type == pygame.KEYDOWN:
    #         if event.unicode == "w":
    #             camera.move_forward(1)
    #         if event.unicode == "s":
    #             camera.move_forward(-1)
    #         if event.unicode == "a":
    #             camera.move_sideways(1)
    #         if event.unicode == "d":
    #             camera.move_sideways(-1)

    # rays = Rays(np.array([[0, 0, 1]]), np.array([[0, 0, -1]])) # width*height, 3, 3
    rays = camera.get_rays()

    result = scene.cast_rays(rays)

    return result*255

viewer = Viewer(update, (width, height))
viewer.start()
