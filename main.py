# import libraries
import sys
import pygame
# import modules
from constants import *
from player import Player
from shot import Shot
from asteroid import Asteroid
from asteroidfield import AsteroidField

# define functions
def main():
    # setup game
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock  = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable  = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    AsteroidField.containers = (updatable,)
    Player.containers   = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    Shot.containers = (updatable, drawable, shots)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    dt = 0

    # Game loop
    while True:
        for event in pygame.event.get():
            # end program on window exit
            if event.type == pygame.QUIT:
                return

        # run update method on all in updatable group
        updatable.update(dt)
        for a in asteroids:
            if a.collision_detection(player):
                print("Game Over!")
                sys.exit()

        # redraw graphics
        screen.fill("black")
        for thing in drawable:
            thing.draw(screen)
        pygame.display.flip()

        # limit framerate and generate delta time(dt)
        dt = (clock.tick(60)/1000)


if __name__ == "__main__":
    main()
