import pygame
from constants import *
from player import Player
from asteroid import Asteroid

def main():
    pygame.init()

    clock = pygame.time.Clock()    
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()    
    Player.containers = (updatable, drawable)    
    player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    Asteroid.containers = (asteroids, updatable, drawable)
    asteroid = [
        Asteroid(100, 100, ASTEROID_MIN_RADIUS),
        Asteroid(300, 200, ASTEROID_MIN_RADIUS * 2),
        Asteroid(500, 300, ASTEROID_MIN_RADIUS * 3)
    ]
    pygame.display.set_caption("Jogo de Asteroides")
    print("Starting Asteroids!")
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)
    print("ASTEROID_MIN_RADIUS =", ASTEROID_MIN_RADIUS)
    print("ASTEROID_KINDS =", ASTEROID_KINDS)
    print("ASTEROID_SPAWN_RATE =", ASTEROID_SPAWN_RATE)
    print("ASTEROID_MAX_RADIUS =", ASTEROID_MAX_RADIUS * ASTEROID_KINDS, "\n")

    running = True
    
    while running:
        dt = clock.tick(60) / 1000

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        updatable.update(dt) # Atualizar todos os objetos no grupo updatable
     
        screen.fill((0, 0, 0))
        
        # Desenhar todos os objetos no grupo drawable
        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()

    pygame.quit() 

if __name__ == "__main__":
    main()

# Fim do arquivo main.py