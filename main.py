import pygame
from constants import *
from player import Player


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    clock = pygame.time.Clock()
    dt = 0
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    drawable = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    
    player.containers = (drawable, updatable)
    drawable.add(player)
    updatable.add(player)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill((0, 0, 0))
        
        for to_draw in drawable:
            to_draw.draw(screen)
            
        pygame.display.flip()
        dt = clock.tick(60)/1000.0  # Limit to 60 FPS and get delta time
        
        for to_update in updatable:
            to_update.update(dt)
    

if __name__ == "__main__":
    main()
