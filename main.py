import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode(size=(SCREEN_WIDTH, SCREEN_HEIGHT))

    player_x = SCREEN_WIDTH / 2
    player_y = SCREEN_HEIGHT / 2

    clock = pygame.time.Clock()
    dt = 0

    # Create groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # Set up containers and instances
    Player.containers = (updatable, drawable)
    player = Player(player_x, player_y)

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    asteoid_field = AsteroidField()

    Shot.containers = (shots, updatable, drawable)

    while True:
        # Exit the game by pressing x
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        updatable.update(dt)
        screen.fill("black")

        for drawable_item in drawable:
            drawable_item.draw(screen)

        for asteroid in asteroids:
            if player.check_collision(asteroid):
                print("Game Over!")
                sys.exit()

        pygame.display.flip()

        # limit the fps to 60
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
