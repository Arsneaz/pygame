import pygame
from sys import exit

if __name__ == "__main__":
    pygame.init()
    screen_width = 640
    screen_height = 640
    screen = pygame.display.set_mode(screen_width, screen_height)
    game = Game()
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.QUIT()
                exit()

        clock.tick(60)
        pygame.display.flip()
    