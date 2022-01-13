import core
import random
import pygame
from pygame import Vector2
from pygame import time
from fenetre import Window
from asteroid import Asteroid
from player import Player


def setup():
    core.memory("window", Window())
    core.memory("window").set()
    core.memory("asteroids", [])
    for i in range(4):
        core.memory("asteroids").append(Asteroid())
        core.memory("asteroids")[i].taille = random.randint(3,3)
    core.memory("player", Player())
    core.memory("bullets", [])
    core.memory("temps", [])
    core.memory("temps").append(time.get_ticks())
    core.memory("temps").append(random.randint(5, 15))

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
    asteroidsGeneration()


def collide(player_, asteroids, bullets):
    for ast in asteroids:
        if ast.getRect().collidepoint(player_.position.x, player_.position.y) or ast.getRect().collidepoint(player_.endPos.x, player_.endPos.y):
            player_.vie-=1
            if player_.vie==0:
                gameOver()
            player_.position=Vector2(core.WINDOW_SIZE[0]/2, core.WINDOW_SIZE[1]/2)
            player_.vitesse = Vector2(0,0)
            ast.taille=0
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
            if core.memory("bullets")[i].position.x < 0 or core.memory("bullets")[i].position.x > core.WINDOW_SIZE[0] or core.memory("bullets")[i].position.y < 0 or core.memory("bullets")[i].position.y > core.WINDOW_SIZE[1] or core.memory("bullets")[i].vie<1:
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

def asteroidsGeneration():
    if time.get_ticks()>core.memory("temps")[0]+(core.memory("temps")[1]*1000):
        core.memory("asteroids").append(Asteroid(random.randint(1,3)))
        core.memory("temps")[0] = time.get_ticks()
        core.memory("temps")[1] = random.randint(10,20)

def gameOver():
    core.noLoop()


core.main(setup, run)