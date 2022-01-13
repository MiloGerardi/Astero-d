from pygame import Vector2
import core
from bullet import Bullet
from pygame import time

class Player:
    def __init__(self):
        self.position = Vector2(core.WINDOW_SIZE[0]/2, core.WINDOW_SIZE[1]/2)
        self.vitesseMax = 2
        self.vitesse = Vector2(0,0)
        self.accelerationMax = 1
        self.acceleration = Vector2(0,0)
        self.vie = 3
        self.orientation = Vector2(1,0)
        self.score = 0
        self.endPos = Vector2(0,0)
        self.delais = 300
        self.temps = time.get_ticks()

    def moove(self, acc=Vector2(0,0)):
        self.acceleration = acc
        self.keys()
        if self.acceleration.magnitude()>self.accelerationMax:
            self.acceleration.scale_to_length(self.accelerationMax)
        self.vitesse+=self.acceleration
        if self.vitesse.magnitude()>self.vitesseMax:
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
        self.endPos.x = self.position.x
        self.endPos.y = self.position.y
        self.endPos += self.orientation*20
        core.Draw.line((255,255,255), (self.position.x, self.position.y), (self.endPos.x, self.endPos.y), 5)
        core.Draw.text((255,255,255), 'Life : '+str(self.vie), (30,30), 20)

    def keys(self):
        if core.getKeyPressList('d'):
            self.orientation = self.orientation.rotate(2)
        if core.getKeyPressList('q'):
            self.orientation = self.orientation.rotate((-2))
        if core.getKeyPressList('SPACE') or core.getKeyPressList('z'):
            self.acceleration += self.orientation/10
        if core.getMouseLeftClick():
            if time.get_ticks()>self.temps+self.delais :
                core.memory("bullets").append(Bullet(Vector2(self.endPos.x, self.endPos.y), Vector2(self.orientation.x, self.orientation.y)))
                self.temps = time.get_ticks()