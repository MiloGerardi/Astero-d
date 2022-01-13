from pygame import Vector2
import core
import random
import pygame

class Asteroid:
    def __init__(self, taille=3, position=Vector2(0,0)):
        if position==Vector2(0,0):
            self.position = Vector2(random.randint(0,core.WINDOW_SIZE[0]),random.randint(0,core.WINDOW_SIZE[1]))
        else:
            self.position=position
        self.vitesseMax = 2
        self.vitesse = Vector2(random.randint(0,self.vitesseMax),random.randint(0,self.vitesseMax))
        self.accelerationMax = 1
        self.acceleration = Vector2(random.randint(0,self.accelerationMax),random.randint(0,self.accelerationMax))
        self.taille = taille
        self.dimmensionsGrand = Vector2(100,100)
        self.dimmensionsPetit = Vector2(50,50)
        self.rect = pygame.Rect(0,0,0,0)

    def moove(self, acc=Vector2(0,0)):
        self.acceleration += acc
        if self.acceleration.magnitude()>self.accelerationMax:
            self.acceleration.scale_to_length(self.accelerationMax)
        self.vitesse+=self.acceleration
        if self.vitesse!=Vector2(0,0):
            self.vitesse.scale_to_length(self.vitesseMax)
        self.position += self.vitesse

        if self.position.x<0 :
            self.position.x+=core.WINDOW_SIZE[0]
        elif self.position.x>core.WINDOW_SIZE[0]:
            self.position.x-=core.WINDOW_SIZE[0]
        if self.position.y<0 :
            self.position.y+=core.WINDOW_SIZE[1]
        elif self.position.y>core.WINDOW_SIZE[1]:
            self.position.y-=core.WINDOW_SIZE[1]

        self.acceleration = Vector2(0,0)

    def display(self):
        if self.taille == 3:
            core.Draw.rect((255,255,255), (self.position.x-(self.dimmensionsGrand.x/2), self.position.y-(self.dimmensionsGrand.y/2), self.dimmensionsGrand.x, self.dimmensionsGrand.y))
            self.rect = pygame.Rect(self.position.x-50, self.position.y-50, 100, 100)
        elif self.taille == 2 :
            core.Draw.rect((255, 255, 255), (self.position.x-(self.dimmensionsPetit.x/2), self.position.y-(self.dimmensionsPetit.y/2), self.dimmensionsPetit.x, self.dimmensionsPetit.y))
            self.rect = pygame.Rect(self.position.x-25, self.position.y-25, 50, 50)
        else :
            core.Draw.rect((255, 255, 255), (self.position.x - (25 / 2), self.position.y - (25 / 2),25, 25))
            self.rect = pygame.Rect(self.position.x - 12, self.position.y - 12, 25, 25)

        if self.taille == 0:
            del self
    def getRect(self):
        return self.rect
    def hit(self):
        if self.taille==2:
            self.vitesse = Vector2(random.randint(0,self.vitesseMax),random.randint(0,self.vitesseMax))
            core.memory("asteroids").append(Asteroid(2, Vector2(self.position.x, self.position.y)))
            core.memory("asteroids")[-1].acceleration = Vector2(random.randint(0, 100), random.randint(0, 100))
            self.acceleration = Vector2(random.randint(0, 100), random.randint(0, 100))
        if self.taille==1:
            self.vitesse = Vector2(random.randint(0,self.vitesseMax),random.randint(0,self.vitesseMax))
            core.memory("asteroids").append(Asteroid(1, Vector2(self.position.x, self.position.y)))
            core.memory("asteroids")[-1].acceleration = Vector2(random.randint(0, 100), random.randint(0, 100))
            self.acceleration = Vector2(random.randint(0, 100), random.randint(0, 100))