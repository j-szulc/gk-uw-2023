import numpy as np


class Rays:

    def __init__(self, origins, directions):
        self.origins = origins
        self.directions = directions

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
        return self.origins + t[:, np.newaxis] * self.directions