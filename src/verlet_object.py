import numpy as np


class VerletObject:
    def __init__(self) -> None:
        self.position = np.array([0, 0])
        self.old_position = np.array([0, 0])
        self.acceleration = np.array([0, 0])
