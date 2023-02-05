from random import *
import pygame


class Chasseur:
    
    def __init__(self, position_x, position_y):
        self.position_x = position_x
        self.position_y = position_y
        
    def deplacement(self,tableau,window):
        dx = randint(-1, 1)
        dy = randint(-1, 1)
        self.position_x = (self.position_x + dx) % tableau.dimension
        self.position_y = (self.position_y + dy) % tableau.dimension
        return self.position_x, self.position_y
    
    def adjacentes_lou(self,loup,monde,window):
        if self.position_x == 0 and self.position_y == 0:# coin en haut à gauche
            if (self.position_x, self.position_y + 1) == (loup.position_x, loup.position_y):
                (self.position_x, self.position_y) = (loup.position_x, loup.position_y)
            elif (self.position_x + 1, self.position_y + 1) == (loup.position_x, loup.position_y):
                (self.position_x, self.position_y) = (loup.position_x, loup.position_y)
            elif (self.position_x + 1, self.position_y + 1) == (loup.position_x, loup.position_y):
                (self.position_x, self.position_y) = (loup.position_x, loup.position_y)
        if self.position_x == 0 and self.position_y == monde.dimension - 1: # coin en haut à droite
            if (self.position_x - 1, self.position_y - 1) == (loup.position_x, loup.position_y):
                (self.position_x, self.position_y) = (self.position_x - 1, self.position_y - 1)
            elif (self.position_x + 1, self.position_y + 1) == (loup.position_x, loup.position_y):
                (self.position_x, self.position_y) = (self.position_x + 1, self.position_y + 1)
            elif (self.position_x + 1, self.position_y - 1) == (loup.position_x, loup.position_y):
                (self.position_x, self.position_y) = (loup.position_x, loup.position_y)
        if self.position_x == monde.dimension - 1 and self.position_y == 0: #coin en bas à gauche
            if (self.position_x + 1, self.position_y ) == (loup.position_x, loup.position_y):
                (self.position_x, self.position_y) = (loup.position_x, loup.position_y)
            if (self.position_x + 1, self.position_y + 1 ) == (loup.position_x, loup.position_y):
                (self.position_x, self.position_y) = (loup.position_x, loup.position_y)
            if (self.position_x , self.position_y + 1 ) == (loup.position_x, loup.position_y):
                (self.position_x, self.position_y) = (loup.position_x, loup.position_y)
        if self.position_x == monde.dimension - 1 and self.position_y == monde.dimension - 1:
            if (self.position_x , self.position_y -1) == (loup.position_x, loup.position_y):# coin en bas à droite
                (self.position_x, self.position_y) = (loup.position_x, loup.position_y)
            if (self.position_x - 1, self.position_y - 1 ) == (loup.position_x, loup.position_y):
                (self.position_x, self.position_y) = (loup.position_x, loup.position_y)
            if (self.position_x -1 , self.position_y) == (loup.position_x, loup.position_y):
                (self.position_x, self.position_y) = (loup.position_x, loup.position_y)
        if self.position_x == 0 and self.position_y != 0 and self.position_y != monde.dimension - 1: #le chasseur sur une case du haut hormis 0,0 et 0,dimension
            if (self.position_x , self.position_y -1) == (loup.position_x, loup.position_y):
                (self.position_x, self.position_y) = (loup.position_x, loup.position_y)
            if (self.position_x + 1, self.position_y - 1 ) == (loup.position_x, loup.position_y):
                (self.position_x, self.position_y) = (loup.position_x, loup.position_y)
            if (self.position_x + 1, self.position_y) == (loup.position_x, loup.position_y):
                (self.position_x, self.position_y) = (loup.position_x, loup.position_y)
            if (self.position_x + 1, self.position_y + 1) == (loup.position_x, loup.position_y):
                (self.position_x, self.position_y) = (loup.position_x, loup.position_y)
            if (self.position_x, self.position_y + 1 ) == (loup.position_x, loup.position_y):
                (self.position_x, self.position_y) = (loup.position_x, loup.position_y)
        if self.position_x == monde.dimension - 1 and self.position_y != 0 and self.position_y != monde.dimension - 1: #le chasseur sur une case du bas  hormis dimension,0 et dismension,dimension
            if (self.position_x , self.position_y -1) == (loup.position_x, loup.position_y):
                (self.position_x, self.position_y) = (loup.position_x, loup.position_y)
            if (self.position_x, self.position_y + 1 ) == (loup.position_x, loup.position_y):
                (self.position_x, self.position_y) = (loup.position_x, loup.position_y)
            if (self.position_x - 1, self.position_y - 1) == (loup.position_x, loup.position_y):
                (self.position_x, self.position_y) = (loup.position_x, loup.position_y)
            if (self.position_x - 1, self.position_y) == (loup.position_x, loup.position_y):
                (self.position_x, self.position_y) = (loup.position_x, loup.position_y)
            if (self.position_x - 1, self.position_y + 1 ) == (loup.position_x, loup.position_y):
                (self.position_x, self.position_y) = (loup.position_x, loup.position_y)
        if self.position_y == 0 and self.position_x != 0 and self.position_x != monde.dimension - 1: #le chasseur sur une case à gauche  hormis dimension,0 et 0,0
            if (self.position_x - 1, self.position_y) == (loup.position_x, loup.position_y):
                (self.position_x, self.position_y) = (loup.position_x, loup.position_y)
            if (self.position_x - 1, self.position_y + 1 ) == (loup.position_x, loup.position_y):
                (self.position_x, self.position_y) = (loup.position_x, loup.position_y)
            if (self.position_x, self.position_y + 1) == (loup.position_x, loup.position_y):
                (self.position_x, self.position_y) = (loup.position_x, loup.position_y)
            if (self.position_x + 1, self.position_y + 1) == (loup.position_x, loup.position_y):
                (self.position_x, self.position_y) = (loup.position_x, loup.position_y)
            if (self.position_x + 1, self.position_y) == (loup.position_x, loup.position_y):
                (self.position_x, self.position_y) = (loup.position_x, loup.position_y)
        if self.position_y == monde.dimension and self.position_x != 0 and self.position_x != monde.dimension - 1: #le chasseur sur une case à droite  hormis 0,dimension et dimension,dimension
            if (self.position_x - 1, self.position_y) == (loup.position_x, loup.position_y):
                (self.position_x, self.position_y) = (loup.position_x, loup.position_y)
            if (self.position_x - 1, self.position_y - 1 ) == (loup.position_x, loup.position_y):
                (self.position_x, self.position_y) = (loup.position_x, loup.position_y)
            if (self.position_x, self.position_y - 1) == (loup.position_x, loup.position_y):
                (self.position_x, self.position_y) = (loup.position_x, loup.position_y)
            if (self.position_x + 1, self.position_y - 1) == (loup.position_x, loup.position_y):
                (self.position_x, self.position_y) = (loup.position_x, loup.position_y)
            if (self.position_x + 1, self.position_y) == (loup.position_x, loup.position_y):
                (self.position_x, self.position_y) = (loup.position_x, loup.position_y)
        else:
            self.deplacement(monde,window)
    
    def placeChasseur(self, i, j,dimension, window):
        self.position_x = i
        self.position_y = j
        