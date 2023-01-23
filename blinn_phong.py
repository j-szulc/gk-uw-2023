import numpy as np

def blinn_phong(self, points, towards_light, towards_observer):
    """
    :param points: N, 3
    :param towards_light: N, 3
    :param towards_observer: N, 3
    :return: N, 3
    """
    normals = self.normal_at(points)
    halfway = towards_light + towards_observer
    halfway /= np.linalg.norm(halfway, axis=1, keepdims=True)
    diffuse = self.diffuse_color * np.sum(normals * towards_light, axis=1, keepdims=True)
    specular = self.specular_color * np.sum(normals * halfway, axis=1, keepdims=True) ** self.shininess
    specular = np.clip(specular, 0, 1)
    return np.clip(self.ambient_color + diffuse + specular, 0, 1)
