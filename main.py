import pygame
from constants import *
from player import *
from asteroid import Asteroid
from asteroidfield import *
from shot import *


def main():

    updatable_group = pygame.sprite.Group()
    drawable_group = pygame.sprite.Group()
    asteroid_group = pygame.sprite.Group()
    shot_group = pygame.sprite.Group()
    
    pygame.init
    pygame.display.init
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
    clock = pygame.time.Clock()
    dt = 0

    Asteroid.containers = (asteroid_group, drawable_group, updatable_group)
    Player.containers = (updatable_group, drawable_group)
    AsteroidField.containers = (updatable_group)
    Shot.containers = (shot_group, drawable_group, updatable_group)


    asteroidfield = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill((0,0,0))

        for things in updatable_group:
            things.update(dt)

        for asteroid in asteroid_group:
            if (asteroid.detectCollision(player)):
                print("Game over!")
                return

        for art in drawable_group:
            art.draw(screen)
        
        pygame.display.flip()

        dt = clock.tick(60) / 1000



if __name__ == "__main__":
    main()