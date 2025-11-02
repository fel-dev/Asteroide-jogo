import pygame
from constants import *
from player import Player

def main():
    pygame.init()

    # ✅ Criar o objeto de relógio # ✅ Inicializar a variável de delta time
    clock = pygame.time.Clock()    
    dt = 0

    player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
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
        dt = clock.tick(60) / 1000  # em segundos

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
        player.update(dt)

        screen.fill((0, 0, 0))  # fundo preto
        player.draw(screen)
        pygame.display.flip()  # atualizar a tela com o novo desenho

    pygame.quit() 

if __name__ == "__main__":
    main()

# Fim do arquivo main.py