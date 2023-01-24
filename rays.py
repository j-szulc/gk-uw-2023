from imports import *



class Rays:

    def __init__(self, origins, directions, ttl=1):
        self.origins = origins
        self.directions = directions
        self.ttl = ttl

    def __getitem__(self, item):
        return Rays(self.origins[item, :], self.directions[item, :])

    @staticmethod
    def from_point_pairs(froms, tos):
        """
        :param froms: N, 3
        :param tos: N, 3
        :return: Rays
        """
        origins = froms
        directions = tos - froms
        directions /= np.linalg.norm(directions, axis=1, keepdims=True)
        return Rays(origins, directions)

    def evaluate_at_t(self, t):
        """
        :param t: N
        :return: N, 3
        """
        t = np.reshape(t, (-1, 1))
        t = np.broadcast_to(t, self.origins.shape)
        return self.origins + t * self.directions

    def flatten(self):
        previous_shape = self.origins.shape[:-1]
        self.origins = self.origins.reshape(-1, 3)
        self.directions = self.directions.reshape(-1, 3)
        return previous_shape

    def unflatten(self, previous_shape):
        self.origins = self.origins.reshape(previous_shape + (3,))
        self.directions = self.directions.reshape(previous_shape + (3,))

    def offset(self, t_offset):
        self.origins += t_offset * self.directions