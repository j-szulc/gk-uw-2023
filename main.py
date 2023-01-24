import pygame

from imports import *
from rays import *
from material import *
from sphere import *
from viewer import *
from time import time
from scene2 import *
from camera import *
from skimage.transform import resize

last_update_time = time()

camera = Camera(width=width, height=height, wres=wres, hres=hres,position=[2, 2, 0], direction=[0, 0, 1], up=[0, 1, 0])

def update(events):
    global last_update_time
    global scene
    # print("FPS: ", 1/(time() - last_update_time))
    # print(camera.position)
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
        camera.rotate_right(1)
    if keys_pressed[pygame.K_RIGHT]:
        camera.rotate_right(-1)
    if keys_pressed[pygame.K_UP]:
        camera.rotate_up(1)
    if keys_pressed[pygame.K_DOWN]:
        camera.rotate_up(-1)
    if keys_pressed[pygame.K_r]:
        camera.reset_rotation()

    # print(np.dot(camera.direction, camera.up))
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
    result = scene.cast_and_render(rays)
    def overlay(surf):
        # pygame.draw.line(surf, (255, 0, 0), camera.project_to_screen(camera2.position), camera.project_to_screen(camera2.position + camera2.direction))
        # pygame.draw.line(surf, (0, 255, 0), camera.project_to_screen(camera2.position), camera.project_to_screen(camera2.position + camera2.right))
        # pygame.draw.line(surf, (0, 0, 255), camera.project_to_screen(camera2.position), camera.project_to_screen(camera2.position + camera2.up))
        # pygame.draw.circle(surf, (0, 0, 255), camera.project_to_screen(camera2.position), 5)
        global rays_to_debug
        for rays in rays_to_debug:
            rays.flatten()
            for beg, dir in zip(rays.origins, rays.directions):
                # pygame.draw.circle(surf, (0, 0, 255), camera.project_to_screen(), 5)
                pygame.draw.line(surf, (0, 255, 0), camera.project_to_screen(beg), camera.project_to_screen(beg + dir*100))
        rays_to_debug = []

    return resize(result*255, (width, height), anti_aliasing=True).astype(np.uint8), overlay

viewer = Viewer(update, (width, height))
viewer.start()
