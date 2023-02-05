from random import *
from classe_monde import *
import pygame


class Mouton:
    def __init__(self, position_x, position_y):
        self.gain_nourriture = 4
        self.position_x = position_x
        self.position_y = position_y
        self.energie = randint(1,2*self.gain_nourriture)
        self.taux_reproduction = 4
        a = randint(0,100)
        if a <= 50:
            self.sexe = 0
        else:
            self.sexe = 1
        
    def variationEnergie(self,tableau):
        if tableau.getCoefCarte(self.position_x, self.position_y) > 0:
            tableau.herbeMangee(self.position_x,self.position_y)
            self.energie += self.gain_nourriture
        else:
            self.energie -= 1
        return self.energie

    def deplacement(self,tableau):
        dx = randint(-1, 1)
        dy = randint(-1, 1)
        self.position_x = (self.position_x + dx) % tableau.dimension
        self.position_y = (self.position_y + dy) % tableau.dimension
        return self.position_x,self.position_y
          


    def placeMouton(self, i, j,window,dimension):
        self.position_x = i
        self.position_y = j
        

