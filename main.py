import sys
import pygame
from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import *
from player import Player
from shot import Shot


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    drawable = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, drawable, updatable)
    AsteroidField.containers = (updatable)
    Player.containers = (drawable, updatable)
    Shot.containers = (shots, drawable, updatable)

    asteroid_field = AsteroidField()
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill((0, 0, 0))

        updatable.update(dt)
        player.cooldown -= dt

        for asteroid in asteroids:
            if player.checkCollision(asteroid):
                print("Game over!")
                sys.exit()
        
            for shot in shots:
                if shot.checkCollision(asteroid):
                    shot.kill()
                    asteroid.split()
                    

        for object in drawable:
            object.draw(screen)

        pygame.display.flip()

        # Limit to 60 FPS and get delta time
        dt = clock.tick(60)/1000.0

if __name__ == "__main__":
    main()
