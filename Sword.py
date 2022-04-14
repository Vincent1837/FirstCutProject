import pygame
import os
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
        self.direction = n
        self.squat = False
        self.squatr = False
        self.done = False
    def update(self, n):
        self.degree = self.degree%360
        if self.rotating:
            self.swing(self.direction)
        if self.reverse:
            self.reversing(self.direction)       
        if self.squat:
            self.squatting(self.direction)    
        if self.squatr:
            if self.degree != 90:
                self.rsquatting(self.rdirection)
            else:
                self.squatr = False    
        key_pressed = pygame.key.get_pressed()
        self.rect.centerx += self.speedr - self.speedl
        if self.speedr > self.speedl and not self.rotating and not self.reverse:
            self.direction = 1
        elif self.speedr < self.speedl and not self.rotating and not self.reverse:
            self.direction = 2    
        if self.speedr != 0:
            self.speedr -= 0.5
        if self.speedl != 0:
            self.speedl -= 0.5
        
        if n==2: 
            if key_pressed[pygame.K_RIGHT] and self.speedr < SPEED_LIMIT:
                self.speedr += 1
            if key_pressed[pygame.K_LEFT] and self.speedl < SPEED_LIMIT:
                self.speedl += 1
            if self.rotating == False and self.reverse == False and key_pressed[pygame.K_SLASH]:
                self.rotating = True
            if key_pressed[pygame.K_DOWN] and self.squatr == False:
                self.squat = True
            else:
                if self.squat:
                    self.rdirection = self.direction
                    self.squat = False
                    self.squatr = True
        else:
            if key_pressed[pygame.K_d] and self.speedr < SPEED_LIMIT:
                self.speedr += 1            
            if key_pressed[pygame.K_a] and self.speedl < SPEED_LIMIT:
                self.speedl += 1 
            if self.rotating == False and self.reverse == False and key_pressed[pygame.K_q]:
                self.rotating = True    
            if key_pressed[pygame.K_s] and self.squatr == False:
                self.squat = True
            else:
                if self.squat:
                    self.rdirection = self.direction
                    self.squat = False
                    self.squatr = True    
        if self.rect.right > WINDOW_WIDTH:
            self.rect.right = WINDOW_WIDTH
        if self.rect.left < 0:
            self.rect.left = 0 
    def rotate(self,degree):
        
        self.totaldegree+=degree
        self.totaldegree = self.totaldegree % 360
        self.image = pygame.transform.rotate(self.ori_image , self.totaldegree)
        center = self.rect.center
        self.rect = self.image.get_rect()
        self.rect.center = center
    def swing(self,n):    
        if n == 2:
            self.rotate(5)
            self.degree += 5
            if self.degree == 180:
                self.reverse = True
                self.rotating = False
        else:
            self.rotate(-5)
            self.degree -= 5
            if self.degree == 0:
                self.reverse = True
                self.rotating = False
    def reversing(self,n):    
        if n == 2:
            self.rotate(-5)
            self.degree -= 5
            if self.degree == 90:
                self.reverse = False
        else:
            self.rotate(5)
            self.degree += 5
            if self.degree == 90:
                self.reverse = False
    def squatting(self, n):
            if n == 1:            
                if self.degree != 310:
                    self.rotate (-10)
                    self.degree -= 10
            else:            
                if self.degree < 230:
                    self.rotate (10)
                    self.degree += 10
    def rsquatting(self, n):
            if n == 1:            
                self.rotate (10)
                self.degree += 10
            else:            
                self.rotate (-10)
                self.degree -= 10                          
                 
                       

        
        
