# imports
import pygame
from constants import *
from player import Player

# define functions
def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    dt = 0

    while True:
        for event in pygame.event.get():
            # end program on window exit
            if event.type == pygame.QUIT:
                return

        # run update method on all in updatable group
        updatable.update(dt)

        # redraw graphics
        screen.fill("black")
        for thing in drawable:
            thing.draw(screen)
        pygame.display.flip()

        # limit framerate and generate delta time(dt)
        dt = (clock.tick(60)/1000)


if __name__ == "__main__":
    main()
