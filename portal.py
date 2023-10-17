from quad import *

class Portal(Quad):

    def __init__(self, corner, x, y, material):
        super().__init__(corner, x, y, material)
        self.paired_quad = None
        self.transform_to_paired = None

    def pair_quad(self, quad):
        self.paired_quad = quad
        # Since the basis vectors are orthogonal, a transpose should be sufficient
        self.transform_to_paired = quad.get_basis() @ np.linalg.inv(self.get_basis())

    def render(self, scene, rays, intersect_t, lights):
        if rays.ttl <= 0:
            return np.zeros((*intersect_t.shape, 3))
        new_origins = rays.evaluate_at_t(intersect_t-1e-3)
        new_origins -= self.corner
        new_origins = np.dot(new_origins, self.transform_to_paired)
        new_origins += self.paired_quad.corner
        # new_directions = np.random.random(rays.directions.shape)
        # new_directions = np.array([0,0,-20]) - new_origins
        # new_directions /= np.linalg.norm(new_directions, axis=1, keepdims=True)
        new_directions = -rays.directions @ self.transform_to_paired
        new_directions /= np.linalg.norm(new_directions, axis=1, keepdims=True)
        # new_directions = np.broadcast_to([0,0,-1], rays.directions.shape)
        new_rays = Rays(new_origins, new_directions, rays.ttl - 1, True)
        result = scene.cast_and_render(new_rays)
        return result