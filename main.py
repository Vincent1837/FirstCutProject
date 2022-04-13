"""
First Cut
Dual Battle Game
"""

import pygame
from pygame.locals import QUIT
from Player import Player
from Sword import Sword
import sys

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
GROUND_LEVEL = 400
FPS = 60
all_sprite = pygame.sprite.Group()

def main():
    pygame.init()
    window_surface = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("First Cut DEMO")
    head_font = pygame.font.SysFont(None, 60)
    text_surface = head_font.render('Hello World!', True, (0, 0, 0))
    pygame.display.update()

    player1 = Player(1)
    player2 = Player(2)
    sword1 = Sword(1)
    sword2 = Sword(2)
    all_sprite.add(player1, player2, sword1, sword2)
    clock = pygame.time.Clock()
    while True:
        window_surface.fill((255,255,255))
        window_surface.blit(text_surface, (10, 10))
        player1.update(1)
        player2.update(2)
        sword1.update(1)        
        sword2.update(2)
        all_sprite.draw(window_surface)
        for event in pygame.event.get():            
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        clock.tick(FPS)
        pygame.display.update()
if __name__ == '__main__':
    main() 
       