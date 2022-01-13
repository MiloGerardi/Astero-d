import core
from pygame import Vector2

class Bullet:
    def __init__(self, position=Vector2(0,0), direction=Vector2(0,0)):
        self.position = position
        self.direction = direction
        self.vitesseMax = 4
        self.vie = 1

    def moove(self, acc=Vector2(0,0)):
        vitesse = Vector2(0,0)
        vitesse += self.direction*self.vitesseMax
        vitesse += acc
        self.position += vitesse


    def display(self):
        core.Draw.circle((255,255,255), (self.position.x, self.position.y), 2)
        if self.vie == 0:
            del self
