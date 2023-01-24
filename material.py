import numpy as np

class BasicMaterial:
    override_normals = None

    def __init__(self, ambient_color, diffuse_color, specular_color, shininess):
        self.ambient_color = ambient_color
        self.diffuse_color = diffuse_color
        self.specular_color = specular_color
        self.shininess = shininess

    def normals_override(self, _, normals):
        return normals

    def diffuse_colors_at(self, _):
        return self.diffuse_color

    def specular_colors_at(self, _):
        return self.specular_color

    def ambient_colors_at(self, _):
        return self.ambient_color

class MirrorMaterial(BasicMaterial):
    override_normals = None

    def __init__(self, shininess):
        super().__init__(np.array([0, 0, 0]), np.array([0, 0, 0]), np.array([1, 1, 1]), shininess)
