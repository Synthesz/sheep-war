from random import *
from classe_monde import *
from classe_mouton import *


class Loup:
    def __init__(self, position_x, position_y):
        self.gain_nourriture = 18
        self.position_x = position_x
        self.position_y = position_y
        self.energie = randint(1,2*self.gain_nourriture)
        self.taux_reproduction = 5
        a = randint(0,100)
        if a <= 50:
            self.sexe = 0
        else:
            self.sexe = 1


    def deplacement_lou(self,tableau,window):
        dx = randint(-1, 1)
        dy = randint(-1, 1)
        self.position_x = (self.position_x + dx) % tableau.dimension
        self.position_y = (self.position_y + dy) % tableau.dimension
        return self.position_x, self.position_y
    
    def adjacentes_lou(self,mouton,monde,window):
        if self.position_x == 0 and self.position_y == 0: # coin en haut à gauche
            if (self.position_x, self.position_y + 1) == (mouton.position_x, mouton.position_y):
                (self.position_x, self.position_y) = (mouton.position_x, mouton.position_y)
            elif (self.position_x + 1, self.position_y + 1) == (mouton.position_x, mouton.position_y):
                (self.position_x, self.position_y) = (mouton.position_x, mouton.position_y)
            elif (self.position_x + 1, self.position_y + 1) == (mouton.position_x, mouton.position_y):
                (self.position_x, self.position_y) = (mouton.position_x, mouton.position_y)
        if self.position_x == 0 and self.position_y == monde.dimension - 1: # coin en haut à droite
            if (self.position_x - 1, self.position_y - 1) == (mouton.position_x, mouton.position_y):
                (self.position_x, self.position_y) = (self.position_x - 1, self.position_y - 1)
            elif (self.position_x + 1, self.position_y + 1) == (mouton.position_x, mouton.position_y):
                (self.position_x, self.position_y) = (self.position_x + 1, self.position_y + 1)
            elif (self.position_x + 1, self.position_y - 1) == (mouton.position_x, mouton.position_y):
                (self.position_x, self.position_y) = (mouton.position_x, mouton.position_y)
        if self.position_x == monde.dimension - 1 and self.position_y == 0: #coin en bas à gauche
            if (self.position_x + 1, self.position_y ) == (mouton.position_x, mouton.position_y):
                (self.position_x, self.position_y) = (mouton.position_x, mouton.position_y)
            if (self.position_x + 1, self.position_y + 1 ) == (mouton.position_x, mouton.position_y):
                (self.position_x, self.position_y) = (mouton.position_x, mouton.position_y)
            if (self.position_x , self.position_y + 1 ) == (mouton.position_x, mouton.position_y):
                (self.position_x, self.position_y) = (mouton.position_x, mouton.position_y)
        if self.position_x == monde.dimension - 1 and self.position_y == monde.dimension - 1:
            if (self.position_x , self.position_y -1) == (mouton.position_x, mouton.position_y):# coin en bas à droite
                (self.position_x, self.position_y) = (mouton.position_x, mouton.position_y)
            if (self.position_x - 1, self.position_y - 1 ) == (mouton.position_x, mouton.position_y):
                (self.position_x, self.position_y) = (mouton.position_x, mouton.position_y)
            if (self.position_x -1 , self.position_y) == (mouton.position_x, mouton.position_y):
                (self.position_x, self.position_y) = (mouton.position_x, mouton.position_y)
        if self.position_x == 0 and self.position_y != 0 and self.position_y != monde.dimension - 1: #le loup sur une case du haut hormis 0,0 et 0,dimension
            if (self.position_x , self.position_y -1) == (mouton.position_x, mouton.position_y):
                (self.position_x, self.position_y) = (mouton.position_x, mouton.position_y)
            if (self.position_x + 1, self.position_y - 1 ) == (mouton.position_x, mouton.position_y):
                (self.position_x, self.position_y) = (mouton.position_x, mouton.position_y)
            if (self.position_x + 1, self.position_y) == (mouton.position_x, mouton.position_y):
                (self.position_x, self.position_y) = (mouton.position_x, mouton.position_y)
            if (self.position_x + 1, self.position_y + 1) == (mouton.position_x, mouton.position_y):
                (self.position_x, self.position_y) = (mouton.position_x, mouton.position_y)
            if (self.position_x, self.position_y + 1 ) == (mouton.position_x, mouton.position_y):
                (self.position_x, self.position_y) = (mouton.position_x, mouton.position_y)
        if self.position_x == monde.dimension - 1 and self.position_y != 0 and self.position_y != monde.dimension - 1: #le loup sur une case du bas  hormis dimension,0 et dismension,dimension
            if (self.position_x , self.position_y -1) == (mouton.position_x, mouton.position_y):
                (self.position_x, self.position_y) = (mouton.position_x, mouton.position_y)
            if (self.position_x, self.position_y + 1 ) == (mouton.position_x, mouton.position_y):
                (self.position_x, self.position_y) = (mouton.position_x, mouton.position_y)
            if (self.position_x - 1, self.position_y - 1) == (mouton.position_x, mouton.position_y):
                (self.position_x, self.position_y) = (mouton.position_x, mouton.position_y)
            if (self.position_x - 1, self.position_y) == (mouton.position_x, mouton.position_y):
                (self.position_x, self.position_y) = (mouton.position_x, mouton.position_y)
            if (self.position_x - 1, self.position_y + 1 ) == (mouton.position_x, mouton.position_y):
                (self.position_x, self.position_y) = (mouton.position_x, mouton.position_y)
        if self.position_y == 0 and self.position_x != 0 and self.position_x != monde.dimension - 1: #le loup sur une case à gauche  hormis dimension,0 et 0,0
            if (self.position_x - 1, self.position_y) == (mouton.position_x, mouton.position_y):
                (self.position_x, self.position_y) = (mouton.position_x, mouton.position_y)
            if (self.position_x - 1, self.position_y + 1 ) == (mouton.position_x, mouton.position_y):
                (self.position_x, self.position_y) = (mouton.position_x, mouton.position_y)
            if (self.position_x, self.position_y + 1) == (mouton.position_x, mouton.position_y):
                (self.position_x, self.position_y) = (mouton.position_x, mouton.position_y)
            if (self.position_x + 1, self.position_y + 1) == (mouton.position_x, mouton.position_y):
                (self.position_x, self.position_y) = (mouton.position_x, mouton.position_y)
            if (self.position_x + 1, self.position_y) == (mouton.position_x, mouton.position_y):
                (self.position_x, self.position_y) = (mouton.position_x, mouton.position_y)
        if self.position_y == monde.dimension and self.position_x != 0 and self.position_x != monde.dimension - 1: #le loup sur une case à droite  hormis 0,dimension et dimension,dimension
            if (self.position_x - 1, self.position_y) == (mouton.position_x, mouton.position_y):
                (self.position_x, self.position_y) = (mouton.position_x, mouton.position_y)
            if (self.position_x - 1, self.position_y - 1 ) == (mouton.position_x, mouton.position_y):
                (self.position_x, self.position_y) = (mouton.position_x, mouton.position_y)
            if (self.position_x, self.position_y - 1) == (mouton.position_x, mouton.position_y):
                (self.position_x, self.position_y) = (mouton.position_x, mouton.position_y)
            if (self.position_x + 1, self.position_y - 1) == (mouton.position_x, mouton.position_y):
                (self.position_x, self.position_y) = (mouton.position_x, mouton.position_y)
            if (self.position_x + 1, self.position_y) == (mouton.position_x, mouton.position_y):
                (self.position_x, self.position_y) = (mouton.position_x, mouton.position_y)
            else:
                if (self.position_x - 1, self.position_y - 1) == (mouton.position_x, mouton.position_y):
                    (self.position_x, self.position_y) = (mouton.position_x, mouton.position_y)
                if (self.position_x - 1, self.position_y) == (mouton.position_x, mouton.position_y):
                    (self.position_x, self.position_y) = (mouton.position_x, mouton.position_y)
                if (self.position_x - 1, self.position_y + 1) == (mouton.position_x, mouton.position_y):
                    (self.position_x, self.position_y) = (mouton.position_x, mouton.position_y)
                if (self.position_x , self.position_y - 1) == (mouton.position_x, mouton.position_y):
                    (self.position_x, self.position_y) = (mouton.position_x, mouton.position_y)
                if (self.position_x , self.position_y + 1) == (mouton.position_x, mouton.position_y):
                    (self.position_x, self.position_y) = (mouton.position_x, mouton.position_y)
                if (self.position_x + 1, self.position_y - 1) == (mouton.position_x, mouton.position_y):
                    (self.position_x, self.position_y) = (mouton.position_x, mouton.position_y)
                if (self.position_x + 1, self.position_y ) == (mouton.position_x, mouton.position_y):
                    (self.position_x, self.position_y) = (mouton.position_x, mouton.position_y)
                if (self.position_x + 1, self.position_y + 1) == (mouton.position_x, mouton.position_y):
                    (self.position_x , self.position_y) = (mouton.position_x, mouton.position_y)
        else:
            self.deplacement_lou(monde,window)
    
    def placeLou(self, i, j):
        self.position_x = i
        self.position_y = j
        

