try:
    import cupy as np
except ImportError:
    import numpy as np
import matplotlib.pyplot as plt
width = 1080
height = 1080
wres = 60
hres = 60
default_ray_ttl = 2
rays_to_debug = []
def debug_rays(rays):
    global rays_to_debug
    rays_to_debug.append(rays.copy())
