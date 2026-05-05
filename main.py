# This is only a sample code for the project developer (scropxikkk). It's not finished and serves only as a preliminary setup.

import pygame

from models.magnet import Magnet, update_magnets

w_height = 800
w_width = 600


def clamp(value, min_value, max_value):
    return max(min_value, min(value, max_value))


class App:
    def __init__(self):
        pygame.init()

        self.window = pygame.display.set_mode((w_height, w_width))
        pygame.display.set_caption("Magnet Simulation")

        self.bg_color = (255, 255, 255)

        self.magnets = [
            Magnet(
                x=250,
                y=250,
                size=50,
                color=(255, 0, 0),
                polarity="N",
            ),
            Magnet(
                x=250 + 100,
                y=250,
                size=50,
                color=(255, 0, 0),
                polarity="N",
            ),
            Magnet(
                x=250 + 100,
                y=300,
                size=50,
                color=(0, 0, 255),
                polarity="S",
            ),
            Magnet(
                x=250 + 100,
                y=-200,
                size=50,
                color=(0, 0, 255),
                polarity="S",
            ),
        ]

        self.running = True

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.render()

        pygame.quit()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        update_magnets(self.magnets)

        for m in self.magnets:
            m.x = clamp(m.x, 0, w_height - m.size)
            m.y = clamp(m.y, 0, w_width - m.size)

    def render(self):
        self.window.fill(self.bg_color)

        for m in self.magnets:
            m.draw(self.window)

        pygame.display.flip()


if __name__ == "__main__":
    App().run()
