# This is only a sample code for the project developer (scropxikkk). It's not finished and serves only as a preliminary setup.

import pygame

from models.magnet import Magnet


class App:
    def __init__(self):
        pygame.init()

        self.window = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Magnet Simulation")

        self.bg_color = (255, 255, 255)

        self.magnet_s = Magnet(
            x=255,
            y=255,
            size=50,
            color=(0, 0, 255),
            polarity="S",
        )

        self.magnet_n = Magnet(
            x=255 + 50,
            y=255,
            size=50,
            color=(255, 0, 0),
            polarity="N",
        )

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
        # add the physics etc. here
        pass

    def render(self):
        self.window.fill(self.bg_color)

        self.magnet_s.draw(self.window)
        self.magnet_n.draw(self.window)

        pygame.display.flip()


if __name__ == "__main__":
    App().run()
