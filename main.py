import pygame
from constants import *
from Player import Player
from asteroidfeild import *
import sys
from bullet import Bullet

def main():
    
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Bullet.containers = (shots, updatable, drawable)
    AsteroidField.containers =(updatable,)
    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable,drawable)
    player = Player(SCREEN_WIDTH/ 2, SCREEN_HEIGHT /2)
    asteroid_field = AsteroidField()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
              
        screen.fill((0,0,0))
        updatable.update(dt)


        for asteroid in asteroids:
            if player.collision(asteroid):
                print("Game over!")
                sys.exit()
            for bullet in shots:
                if bullet.collision(asteroid):
                    asteroid.split()

        for sprite in drawable:
            sprite.draw(screen) 
        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()

