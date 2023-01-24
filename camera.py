from imports import *
from rays import *
from scipy.spatial.transform import Rotation

class Camera:

    def __init__(self, width, height, wres, hres, position, direction, up, camera_speed=0.1):
        self.width = width
        self.height = height
        self.wres = wres
        self.hres = hres
        self.ratio = float(width) / height
        self.position = np.asarray(position, dtype=np.float32)

        self.direction = np.asarray(direction, dtype=np.float32)
        self.direction /= np.linalg.norm(self.direction)
        self.up = np.asarray(up, dtype=np.float32)
        self.up /= np.linalg.norm(self.up)
        self.right = np.cross(self.direction, self.up)
        self.right /= np.linalg.norm(self.right)

        self.update_persepective_matrix()

        self.clipping_distance = 0.01
        self.camera_speed = camera_speed

    def move_forward(self, delta):
        self.position += self.direction * delta * self.camera_speed

    def move_right(self, delta):
        self.position += self.right * delta * self.camera_speed

    def update_persepective_matrix(self):
        self.perspective_matrix = np.vstack((self.right, self.up, self.direction))

    def rotate_right(self, angle):
        rotation = Rotation.from_rotvec(self.up * angle * self.camera_speed)
        self.direction = rotation.apply(self.direction)
        self.right = np.cross(self.direction, self.up)
        self.right /= np.linalg.norm(self.right)
        self.update_persepective_matrix()

    def rotate_up(self, angle):
        rotation = Rotation.from_rotvec(self.right * -angle * self.camera_speed)
        self.direction = rotation.apply(self.direction)
        self.up = np.cross(self.right, self.direction)
        self.up /= np.linalg.norm(self.up)
        self.update_persepective_matrix()

    def reset_rotation(self):
        self.direction = np.asarray([0, 0, 1], dtype=np.float32)
        self.up = np.asarray([0, 1, 0], dtype=np.float32)
        self.right = np.cross(self.direction, self.up)
        self.right /= np.linalg.norm(self.right)
        self.update_persepective_matrix()

    def get_rays(self):

        x = np.linspace(-self.ratio*self.clipping_distance, self.ratio*self.clipping_distance, self.wres)
        y = np.linspace(-self.clipping_distance, self.clipping_distance, self.hres)
        z = self.clipping_distance * np.ones((1))
        screen = np.dstack(np.meshgrid(x, y, z))  # height, width, 3
        screen = np.swapaxes(screen, 0, 1)  # width, height, 3
        screen = screen.reshape(-1, 3)  # width * height, 3

        screen = self.position + np.matmul(screen, self.perspective_matrix)  # width * height, 3

        camera_pos = np.tile(self.position, (self.wres * self.hres, 1))  # width * height, 3

        rays = Rays.from_point_pairs(froms=camera_pos, tos=screen)  # width*height, 3, 3
        rays.unflatten((self.wres, self.hres))

        return rays

    def project_to_screen(self, point, coord_system="pygame"):
        point = point - self.position
        point = np.matmul(point, self.perspective_matrix.T)
        point = point[:2]
        point *= np.array([self.width, self.height])/2

        if coord_system == "pygame":
            point += np.array([self.width, self.height])/2 # topleft = 0, 0
        else:
            assert coord_system == "center", "Unknown coordinate system!"

        return point
