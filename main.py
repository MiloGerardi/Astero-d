import core
import pygame
from pygame import Vector2
from fenetre import Window
from asteroid import Asteroid
from player import Player
from bullet import Bullet


def setup():
    core.memory("window", Window())
    core.memory("window").set()
    core.memory("asteroids", [])
    for i in range(1):
        core.memory("asteroids").append(Asteroid())
    core.memory("player", Player())
    core.memory("bullets", [])

def run():
    core.cleanScreen()
    core.memory("player").moove()
    core.memory("player").display()
    for asteroid in core.memory("asteroids"):
        asteroid.moove()
        asteroid.display()
    for bullet in core.memory("bullets"):
        bullet.moove()
        bullet.display()
    collide(core.memory("player"), core.memory("asteroids"), core.memory("bullets"))
    bulletKill()
    asteroidKill()


def collide(player_, asteroids, bullets):
    for ast in asteroids:
        if ast.getRect().collidepoint(player_.position.x, player_.position.y) or ast.getRect().collidepoint(player_.endPos.x, player_.endPos.y):
            player_.vie-=1
            return player_
    for ast in asteroids:
        for bul in bullets:
            if ast.getRect().collidepoint(bul.position.x, bul.position.y):
                ast.taille-=1
                ast.hit()
                bul.vie-=1
                return ast

def bulletKill():
    for i in range(len(core.memory("bullets"))):
        try :
            if core.memory("bullets")[i].position.x < 0 or core.memory("bullets")[i].position.x > core.WINDOW_SIZE[0] or core.memory("bullets")[i].position.y < 0 or core.memory("bullets")[i].position.y > core.WINDOW_SIZE[1]:
                del core.memory("bullets")[i]
        except :
            pass
def asteroidKill():
    for i in range(len(core.memory("asteroids"))):
        try:
            if core.memory("asteroids")[i].taille==0:
                del core.memory("asteroids")[i]
        except:
            pass


core.main(setup, run)