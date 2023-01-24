from imports import *

class Cubemap():

    def __init__(self, path):
        arr = plt.imread(path)
        arr = arr[:, :, :3]
        arr = arr.swapaxes(0, 1)

        assert arr.shape[0] % 4 == 0
        cube_size = arr.shape[0] // 4
        assert arr.shape[1] == cube_size * 3



        x0 = list(range(0, cube_size))
        x1 = list(range(cube_size, cube_size * 2))
        x2 = list(range(cube_size * 2, cube_size * 3))
        x3 = list(range(cube_size * 3, cube_size * 4))

        y0 = list(range(0, cube_size))
        y1 = list(range(cube_size, cube_size * 2))
        y2 = list(range(cube_size * 2, cube_size * 3))

        self.back = arr[x0, :, :][:, y1, :]
        self.down = arr[x1, :, :][:, y0, :]
        self.left = arr[x1, :, :][:, y1, :]
        self.up = arr[x1, :, :][:, y2, :]
        self.front = arr[x2, :, :][:, y1, :]
        self.right = arr[x3, :, :][:, y1, :]

        breakpoint()

Cubemap("skybox.png")
