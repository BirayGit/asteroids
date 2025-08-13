# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame

# import the connect_database function
# and the database_version variable
# from database.py into the current file
from constants import *
from player import *

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

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    player = Player(player_x, player_y)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        updatable.update(dt)
        screen.fill("black")

        for drawable_item in drawable:
            drawable_item.draw(screen)

        pygame.display.flip()

        # limit the fps to 60
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
