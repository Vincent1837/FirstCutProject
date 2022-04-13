import pygame

from Player import SPEED_LIMIT
WINDOW_WIDTH = 800
GROUND_LEVEL = 400

class Sword(pygame.sprite.Sprite):
    def __init__(self,n):
        pygame.sprite.Sprite.__init__(self)
        sword90_img = pygame.image.load(os.path.join("sword90.png")).convert()   
        self.ori_image = pygame.transform.scale(sword90_img, (20, 45))
        self.image = self.ori_image.copy()
        self.rect = self.image.get_rect()
        self.rect.center = (WINDOW_WIDTH/5*(n**2) , GROUND_LEVEL)
        self.rotating = False
        self.degree = 90
        self.reverse = False
        self.speedr = 0
        self.speedl = 0
        self.totaldegree = 0
    def update(self, n):
        '''if self.rotating:
            self.rotate(-3)
            self.degree -= 3
            if self.degree == 0:
                self.reverse = True
                self.rotating = False'''
        '''if self.reverse:
            self.rotate(3)
            self.degree += 3
            if self.degree == 90:
                self.reverse = False'''       
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
        if self.rotating == False and self.reverse == False and key_pressed[pygame.K_q]:
            #self.rotating = True
            self.rotate(1)     
        if self.rect.right > WINDOW_WIDTH:
            self.rect.right = WINDOW_WIDTH
        if self.rect.left < 0:
            self.rect.left = 0 
    def rotate(self,degree):
        self.totaldegree+=degree
        self.totaldegree = self.totaldegree % 360
        print(self.totaldegree)
        self.image = pygame.transform.rotate(self.ori_image , self.totaldegree)
        center = self.rect.center
        self.rect = self.image.get_rect()
        self.rect.center = center
        
        
