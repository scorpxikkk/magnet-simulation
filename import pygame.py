import pygame

pygame.init()

window = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Magnet Simulation")

blue = 0, 0, 255
red = 255, 0, 0


magnet1_s = {
    "pos_x": 255,
    "pos_y": 255,
    "height": 50,
    "width": 50,
    "color": blue,
    "field": 1
}

magnet1_n = {
    "pos_x": magnet1_n["pos_x"] + magnet1_n["width"],
    "pos_y": magnet1_n["pos_y"],
    "height": 50,
    "width": 50,
    "color": red,
    "field": 2
}

magnet1_rect = pygame.draw.rect

running = True
while running:
    window.fill((255, 255, 255))
    pygame.draw.rect(window, ( magnet1_s["color"]), (magnet1_s["pos_x"], magnet1_s["pos_y"], magnet1_s["width"], magnet1_s["height"]))
    pygame.draw.rect(window, ( magnet1_n["color"]), (magnet1_n["pos_x"], magnet1_n["pos_y"], magnet1_n["width"], magnet1_n["height"]))

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()