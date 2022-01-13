import core

class Window:
    def  __init__(self):
        self.hauteur = 800
        self.largeur = 800
        self.fps = 60
        self.couleur = (0,0,0)

    def set(self):
        core.bgColor = self.couleur
        core.WINDOW_SIZE = [self.hauteur, self.largeur]
        core.fps = self.fps

    def setHauteur(self, h):
        self.hauteur = h
    def setLargeur(self, l):
        self.hauteur = l
    def setFps(self, f):
        self.fps = f
    def setCouleur(self, c):
        self.couleur = c
    def setTaille(self, h,l):
        self.hauteur=h
        self.largeur=l
    def getHauteur(self):
        return self.hauteur()
    def getLargeur(self):
        return self.largeur()
    def getCouleur(self):
        return self.couleur
    def getFps(self):
        return self.fps