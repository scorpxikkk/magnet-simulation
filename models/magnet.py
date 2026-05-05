import math
from dataclasses import dataclass
from typing import Literal

import pygame


@dataclass
class Magnet:
    x: float
    y: float
    size: int
    color: tuple
    polarity: Literal["S", "N"]

    vx: float = 0
    vy: float = 0

    def rect(self):
        return pygame.Rect(int(self.x), int(self.y), self.size, self.size)

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect())


def polarity_value(p):
    return 1 if p == "N" else -1


def distance(a, b):
    dx = b.x - a.x
    dy = b.y - a.y

    return dx, dy, math.sqrt(dx * dx + dy * dy)


def apply_magnet_force(a: Magnet, b: Magnet, k=500):
    dx, dy, r = distance(a, b)

    if r < 1:
        return

    force = k * (polarity_value(a.polarity) * polarity_value(b.polarity)) / (r * r)

    fx = force * dx / r
    fy = force * dy / r

    a.vx += fx
    a.vy += fy
    b.vx -= fx
    b.vy -= fy


def update_magnets(magnets):
    for i in range(len(magnets)):
        for j in range(i + 1, len(magnets)):
            apply_magnet_force(magnets[i], magnets[j])

    for m in magnets:
        m.x += m.vx
        m.y += m.vy

        m.vx *= 0.95
        m.vy *= 0.95
