# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame

# import the connect_database function
# and the database_version variable
# from database.py into the current file
# from database import connect_database, database_version

# import everything from the module
# database.py into the current file
# from database import *
from constants import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Jogo de Asteroides")

    print("\nStarting Asteroids!")
    print("SCREEN_WIDTH:", SCREEN_WIDTH)
    print("SCREEN_HEIGHT:", SCREEN_HEIGHT)
    print("ASTEROID_MIN_RADIUS:", ASTEROID_MIN_RADIUS)
    print("ASTEROID_KINDS:", ASTEROID_KINDS)
    print("ASTEROID_SPAWN_RATE:", ASTEROID_SPAWN_RATE)
    print("ASTEROID_MAX_RADIUS:", ASTEROID_MAX_RADIUS * ASTEROID_KINDS,"\n")

    running = True
    clock = pygame.time.Clock()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))  # fundo preto
        
        # Desenhar aqui a nave, asteroides, etc.
        
        pygame.display.flip() # atualizar a tela com o novo desenho
        clock.tick(60) # limitar a 60 quadros por segundo
        
    pygame.quit()

if __name__ == "__main__":
    main()
