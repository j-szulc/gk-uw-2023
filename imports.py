import numpy as np
import matplotlib.pyplot as plt
width = 600
height = 600
wres = 600
hres = 600
default_ray_ttl = 2
rays_to_debug = []
def debug_rays(rays):
    global rays_to_debug
    rays_to_debug.append(rays.copy())
