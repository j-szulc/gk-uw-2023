from imports import *



class Rays:

    def __init__(self, origins, directions, ttl=1, debug=False):
        self.origins = origins
        self.directions = directions
        self.ttl = ttl
        self.debug = debug

    def __getitem__(self, item):
        return Rays(self.origins[item, :], self.directions[item, :], self.ttl)

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
        return self.origins + np.reshape(t, (-1, 1)) * self.directions

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

    def n_of_rays(self):
        assert len(self.origins.shape) == 2, "Rays must be flattened!"
        return self.origins.shape[0]

    def __copy__(self):
        return Rays(self.origins.copy(), self.directions.copy(), self.ttl)

    def copy(self):
        return self.__copy__()