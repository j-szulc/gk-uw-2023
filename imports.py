import numpy as np
import matplotlib.pyplot as plt
width = 600
height = 600
wres = 200
hres = 200

rays_to_debug = []
def debug_rays(rays):
    global rays_to_debug
    rays_to_debug.append(rays.copy())
