from dataclasses import dataclass
from typing import Literal

import pygame


@dataclass
class Magnet:
    x: int
    y: int
    size: int
    color: tuple  # rgb
    polarity: Literal["S", "N"]

    def rect(self):
        return pygame.Rect(self.x, self.y, self.size, self.size)

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect())
