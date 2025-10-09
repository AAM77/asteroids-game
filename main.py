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
    
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroid_field = AsteroidField()
    
    drawable.add(player)
    updatable.add(player)
    updatable.add(asteroid_field)
    shots.add(player.shoot())

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        updatable.update(dt)
        screen.fill((0, 0, 0))
        
        for to_draw in drawable:
            to_draw.draw(screen)
            
        pygame.display.flip()
        
        # Limit to 60 FPS and get delta time
        dt = clock.tick(60)/1000.0
        
        for to_update in updatable:
            to_update.update(dt)
            player.cooldown -= dt
        
        for asteroid in asteroids:
            if player.checkCollision(asteroid):
                print("Game over!")
                sys.exit()

if __name__ == "__main__":
    main()
