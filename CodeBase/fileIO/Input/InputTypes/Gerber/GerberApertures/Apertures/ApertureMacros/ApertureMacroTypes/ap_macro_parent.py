import math
from abc import abstractmethod


class APMacroParent:
    def __init__(self, unit):
        self.code = None
        self.exposure = None
        self.common_form = []
        self.unit = unit

    @abstractmethod
    def to_common_form(self, *args, **kwargs):
        pass

    def rotate_point_around_origin_cc(self, point_x, point_y, cc_degrees):
        # Formula for CC (Counter-Clockwise) Degree Rotation around origin
        # X' = x * cos(θ) - y * sin(θ)
        # Y' = x * sin(θ) + y * cos(θ)

        # Convert angle from degrees to radians
        angle_radians = math.radians(cc_degrees)

        # Apply the rotation
        rotated_x = point_x * math.cos(angle_radians) - point_y * math.sin(angle_radians)
        rotated_y = point_x * math.sin(angle_radians) + point_y * math.cos(angle_radians)

        return rotated_x, rotated_y
