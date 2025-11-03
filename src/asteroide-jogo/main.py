import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    pygame.init()

    clock = pygame.time.Clock()    
    dt = 0

# Grupos de sprites
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group() 
    
# Associar os grupos às classes
    Player.containers = (updatable, drawable) 
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    
# Criar o jogador e Configurar a tela
    player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
# Inicializar o campo de asteroides
    asteroid_field = AsteroidField()
    
    pygame.display.set_caption("Jogo de Asteroides")
    print("Starting Asteroids!")
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)
    print("ASTEROID_MIN_RADIUS =", ASTEROID_MIN_RADIUS)
    print("ASTEROID_KINDS =", ASTEROID_KINDS)
    print("ASTEROID_SPAWN_RATE =", ASTEROID_SPAWN_RATE)
    print("ASTEROID_MAX_RADIUS =", ASTEROID_MAX_RADIUS * ASTEROID_KINDS, "\n")
        
    collided = 0
    running = True
    
    while running:
        dt = clock.tick(60) / 1000

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        updatable.update(dt)
        
        for asteroid in asteroids:
            if player.collides_with(asteroid):
                collided += 1
                print("Collision", collided ,"with asteroid at", asteroid.position)
        
        screen.fill((0, 0, 0))
        
        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()

    pygame.quit() 

if __name__ == "__main__":
    main()

# Fim do arquivo main.py