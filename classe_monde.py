from random import *

class Monde:
    def __init__(self,dimension,duree_repousse):
        self.dimension = dimension
        self.carte = [[randint(0,duree_repousse*2) for i in range (dimension)] for j in range (dimension)]
        self.duree_repousse = duree_repousse
        
    def herbePousse(self): # fait pour pousser l'herbe en fonction de la durée de repousse
        for i in range (len(self.carte)):
            for j in range (len(self.carte)):
                if self.carte[i][j] < self.duree_repousse:
                    self.carte[i][j] +=1
        return self.carte
                    
    def is_empty(self,i,j): # prédicat pour savoir s'il y a de l'herbe sur case(i;j)
        return self.carte[i][j] < self.duree_repousse
    
    def herbeMangee(self,i,j):
        if not self.is_empty(i,j):
            self.carte[i][j] = 0
    
    def nbHerbe(self): #methode pour compter le nombre d'herbe sur le mponde
        cmpt = 0
        for i in range (len(self.carte)):
            for j in range (len(self.carte)):
                if self.carte[i][j] > self.duree_repousse:
                    cmpt +=1
        return cmpt
    
    def getCoefCarte(self,i,j): #donne le coéficient à la position i,j
        return self.carte[i][j] 