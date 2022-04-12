import pygame
#from main import WINDOW_HEIGHT, WINDOW_WIDTH, GROUND_LEVEL
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
GROUND_LEVEL = 400
SPEED_LIMIT = 7


class Player(pygame.sprite.Sprite):
    def __init__(self,n):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50,40))
        self.rect = self.image.get_rect()
        self.rect.center = (WINDOW_WIDTH/5*(n**2) , GROUND_LEVEL)
        self.radius = 20
        self.speedr = 0
        self.speedl = 0
    def update(self,n):
        key_pressed = pygame.key.get_pressed()
        self.rect.centerx += self.speedr - self.speedl
        if self.speedr != 0:
            self.speedr -= 0.5
        if self.speedl != 0:
            self.speedl -= 0.5
        if n==2: 
            if key_pressed[pygame.K_RIGHT] and self.speedr < SPEED_LIMIT:
                self.speedr += 1
            if key_pressed[pygame.K_LEFT] and self.speedl < SPEED_LIMIT:
                self.speedl += 1
        else:
            if key_pressed[pygame.K_d] and self.speedr < SPEED_LIMIT:
                self.speedr += 1            
            if key_pressed[pygame.K_a] and self.speedl < SPEED_LIMIT:
                self.speedl += 1 
        if self.rect.right > WINDOW_WIDTH:
            self.rect.right = WINDOW_WIDTH
        if self.rect.left < 0:
            self.rect.left = 0 