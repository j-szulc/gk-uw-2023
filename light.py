from imports import *

class Light:

    def __init__(self, position, color = np.array([1, 1, 1])):
        self.position = np.asarray(position)
        self.color = np.asarray(color)


def blinn_phong(material, points, normals, towards_light, towards_observer):
    """
    :param material: Material
    :param points: N, 3
    :param normals: N, 3
    :param towards_light: N, 3
    :param towards_observer: N, 3
    :return: N, 3
    """
    normals = material.normals_override(points, normals)
    halfway = towards_light + towards_observer
    halfway /= np.linalg.norm(halfway, axis=1, keepdims=True)
    diffuse = material.diffuse_colors_at(points) * np.sum(normals * towards_light, axis=1, keepdims=True)
    specular = material.specular_colors_at(points) * np.sum(normals * halfway, axis=1, keepdims=True) ** material.shininess
    specular = np.clip(specular, 0, 1)
    return diffuse + specular
