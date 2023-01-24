from primitive import *
from material import *


class EmptyMaterial(BasicMaterial):

    def __init__(self):
        super().__init__(None, None, None, None)

    def ambient(self, points):
        raise RuntimeError("Empty material!")

    def diffuse(self, points):
        raise RuntimeError("Empty material!")

    def specular(self, points):
        raise RuntimeError("Empty material!")

class Sky(Primitive):

    def __init__(self):
        super().__init__(EmptyMaterial())

    def normal_at(self, points):
        raise RuntimeError("Sky has no normal")

    def intersect_t(self, rays):
        return np.full_like(rays.directions[:, 0], np.inf)

    def render(self, rays, _, _):
        # Sky is blue
        return np.broadcast_to([0, 0, 1], rays.directions.shape)
