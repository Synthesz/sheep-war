import pygame
import ctypes
import time
import os, pathlib
from random import *
from classe_monde import *
from classe_mouton import*
from classe_lou import *
from classe_chasseur import *
import matplotlib.pyplot as plt
import numpy as nb 
from pygame import mixer

nbreMouton=int(input("Combien de Mouton ? -> "))
nbreLoup=int(input('Combien de Loup ? -> '))
nbreChasseur= int(input("combien de chasseur ? -> "))
dureeRepousse=int(input('Choisissez une durée de repousse -> '))
findumonde=int(input("A partir de combien d'exécution voulez vous arrêter la simulation ? -> "))
maxmouton=int(input("Combien de mouton au maximum dans la simulation ? -> "))

user32 = ctypes.windll.user32
width = user32.GetSystemMetrics(0)
height = user32.GetSystemMetrics(1)
SIZE = (width,height)


pygame.init()
pygame.mouse.set_visible(False)
screen = pygame.display.set_mode(SIZE)
filePath = pathlib.Path(__file__).resolve().parent / 'background.wav'
mixer.music.load(filePath)
mixer.music.play(-1)
class Simulation:
    
    global screen
    def __init__(self, nombre_moutons, nombre_lou, nombre_chasseur, fin_du_monde, monde, max_moutons):
        self.nombre_lou = nombre_lou
        self.nombre_moutons = nombre_moutons
        self.nombre_chasseur = nombre_chasseur
        self.horloge = 0
        self.fin_du_monde = fin_du_monde
        self.mouton = []
        for i in range(nombre_moutons):
            self.mouton.append(Mouton(randint(0,monde.dimension-1),randint(0,monde.dimension-1)))
        self.lou = []
        for i in range(nombre_lou):
            self.lou.append(Loup(randint(0,monde.dimension-1),randint(0,monde.dimension-1)))
        self.chasseur = []
        for i in range(nombre_chasseur):
            self.chasseur.append(Chasseur(randint(0,monde.dimension-1),randint(0,monde.dimension-1)))
        self.monde = monde
        self.resultats_herbe = []
        self.resultats_moutons = []
        self.resultats_lou = []
        self.resultats_chasseur = []
        self.max_moutons = max_moutons
        self.window = pygame.display.set_mode((1920,1080))
    
    def affichageMouton(self):
        for i in range(0,len(self.mouton)):
            pos_x = self.mouton[i].position_x
            pos_y = self.mouton[i].position_y
            filePath = pathlib.Path(__file__).resolve().parent / 'Sheep_1.png'
            image = pygame.image.load(filePath)
            scaled_image = pygame.transform.scale(image, (1048//self.monde.dimension, 1048//self.monde.dimension))
            screen.blit(scaled_image,(400+pos_x*1048//self.monde.dimension+1,12+pos_y*1048//self.monde.dimension+1))
    
    def affichageLoup(self):
        for i in range(0,len(self.lou)):
            pos_x = self.lou[i].position_x
            pos_y = self.lou[i].position_y
            filePath = pathlib.Path(__file__).resolve().parent / 'Wolf_1.png'
            image = pygame.image.load(filePath)
            scaled_image = pygame.transform.scale(image, (1048//self.monde.dimension, 1048//self.monde.dimension))
            screen.blit(scaled_image,(400+pos_x*1048//self.monde.dimension+1,12+pos_y*1048//self.monde.dimension+1))    
    
    def affichageHunter(self):
        for i in range(0,len(self.chasseur)):
            pos_x = self.chasseur[i].position_x
            pos_y = self.chasseur[i].position_y
            filePath = pathlib.Path(__file__).resolve().parent / 'hunter_1.png'
            image = pygame.image.load(filePath)
            scaled_image = pygame.transform.scale(image, (1048//self.monde.dimension, 1048//self.monde.dimension))
            screen.blit(scaled_image,(400+pos_x*1048//self.monde.dimension+1,12+pos_y*1048//self.monde.dimension+1))    
    
    def affichageDirt(self):
        for i in range(self.monde.dimension):
            for j in range(self.monde.dimension):
                if self.monde.is_empty(i,j)==True:
                    dirt=pygame.Rect(400+i*1048//self.monde.dimension+1,12+j*1048//self.monde.dimension+1,1048//self.monde.dimension,1048//self.monde.dimension )
                    pygame.draw.rect(screen,(88,41,0),dirt)

    def horloge_1(self):
        self.horloge += 1
    
    def herbepousse(self):
        self.monde.herbePousse()
        
    def vie_mouton(self):
        for i in self.mouton:
            i.variationEnergie(self.monde)
            if i.energie== 0:
                self.mouton.remove(i)
                
    def vie_lou(self):
        for i in self.lou:
            if i.energie == 0:
                self.lou.remove(i)
                  
    def reproduction(self):
        l = len(self.mouton)
        for i in range(l):
            x = randint(0,100)
            if x <= 4:
                self.mouton.append(Mouton(self.mouton[i].position_x,self.mouton[i].position_y))
                
    def reproduction_lou(self):
        l = len(self.lou)
        for i in range(l):
            x = randint(0,100)
            if x <= 5:
                self.lou.append(Loup(self.lou[i].position_x,self.lou[i].position_y))        
       

    def deplace(self):
        for i in self.mouton:
            i.deplacement(self.monde)
            
    def deplace_lou(self):
        for j in self.lou:
            for i in self.mouton:
                a = randint(0,100)
                if a <= 10:
                    j.adjacentes_lou(i,self.monde,screen)
                else:
                    j.deplacement_lou(self.monde,screen)
        for i in self.lou:
            i.deplacement_lou(self.monde,screen)
        
    def deplace_chasseur(self):
        for j in self.chasseur:
            for i in self.lou:
                j.adjacentes_lou(i,self.monde,screen)
        for i in self.lou:
            i.deplacement_lou(self.monde,screen)
        
    
    def resultat(self):
        self.resultats_herbe.append(self.monde.nbHerbe())
        self.resultats_moutons.append(len(self.mouton))
        self.resultats_lou.append (len(self.lou))
        self.resultats_chasseur.append(len(self.chasseur))
    
    def mouton_manger(self):
        for j in self.lou:
            for i in self.mouton:
                if i.position_x ==  j.position_x and i.position_y == j.position_y:
                    self.mouton.remove(i)
                    j.energie += j.gain_nourriture
                else:
                    j.energie -= 1
                    
    def tue_lou(self):
        for j in self.chasseur:
            for i in self.lou:
                if i.position_x ==  j.position_x and i.position_y == j.position_y:
                    a = randint(0,100)
                    if a <= 70:
                        self.lou.remove(i)
                  
    def sim(self):
        while self.max_moutons > len(self.mouton) and self.horloge < self.fin_du_monde:
            self.horloge_1()
            self.herbepousse()
            self.vie_mouton()
            self.reproduction()
            self.reproduction_lou()
            self.deplace_lou()
            self.deplace()
            self.resultat()
            self.tue_lou()
            self.deplace_chasseur()
            self.mouton_manger()
            self.vie_lou()
        return self.resultats_herbe , self.resultats_moutons, self.resultats_lou, self.resultats_chasseur
    
    def nbreMouton(self):
        return len(self.mouton)
    
    def nbreLoup(self):
        return len(self.lou)
    
    def nbreHerbe(self):
        cpt=0
        for i in range(self.monde.dimension):
            for j in range(self.monde.dimension):
                if self.monde.is_empty(i,j)==False:
                    cpt+=1
        return cpt          


    def simPygame(self):
        self.affichageMouton()
        self.affichageLoup()
        self.affichageHunter()
        self.horloge_1()
        self.herbepousse()
        self.vie_mouton()
        self.reproduction()
        self.reproduction_lou()
        self.tue_lou()
        self.mouton_manger()
        self.vie_lou()
        self.deplace()
        self.deplace_lou()
        self.deplace_chasseur()
        pygame.display.flip()
        self.affichageMouton()
        self.affichageLoup()
        self.affichageHunter()
        

        
    
    def graphe(self):
        x = [i for i in range (self.fin_du_monde)]
        y1= nb.array(self.resultats_herbe)
        y2 = nb.array(self.resultats_moutons)
        y3 = nb.array(self.resultats_lou)
        plt.plot(y1,label='herbes')
        plt.plot(y2,label='moutons')
        plt.plot(y3,label='loup')
        plt.legend()
        plt.show()
        return ()


pygame.display.set_caption("SheepWar simulation")
font = pygame.font.Font(None, 32)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
fps=0
start_time=0
def boutton_quitter():
    Button = pygame.Rect(1635, 950, 255, 100)
    pygame.draw.rect(screen, (103,126,89), Button)
    # Définir le texte à afficher sur le bouton
    Font = pygame.font.Font(None, 45)
    Text = Font.render("Quitter ", 1, (255,255,255))
    Textpos = Text.get_rect(centerx=Button.centerx, centery=Button.centery)
    screen.blit(Text, Textpos)
    #bordure boutton quitter
    return pygame.draw.rect(screen, (0, 0, 0), (1635, 950, 255, 100), 5)
boutton_q=boutton_quitter()
def compteurFPS():
    font = pygame.font.Font(None, 36)
    text = font.render('FPS: ' + str(fps), True, (255, 0, 0))
    screen.blit(text, (12, 8))
    pygame.display.update()


def ecran():
    filePath = pathlib.Path(__file__).resolve().parent / 'logo.png'
    logo = pygame.image.load(filePath)
    screen.blit(logo, [0, 0])
    rectangle = pygame.Rect(0, 0, 1920, 1080)
    # Dégradé de couleur
    color1 = (122, 203, 101)
    color2 = (55, 132, 68)
    for y in range(rectangle.height):
    # Calcul de la couleur en fonction de la ligne courante
      ratio = y/rectangle.height
      red = int(color1[0] + ratio * (color2[0] - color1[0]))
      green = int(color1[1] + ratio * (color2[1] - color1[1]))
      blue = int(color1[2] + ratio * (color2[2] - color1[2]))
      color = (red, green, blue)
      # Dessin de la ligne courante
      pygame.draw.line(screen, color, (rectangle.left, rectangle.top+y), (rectangle.right, rectangle.top+y))
    screen.blit(logo, [0, 0])
    mat=font.render("Entrez la taille de matrice souhaitée:", True, (0,0,0))
    screen.blit(mat,(100, 670))
    boutton_quitter()
input_matrice = pygame.Rect(100, 700, 140, 32)
color_inactive = (100,100,100)
color_active = pygame.Color(0,0,0)
color = color_inactive
active = False
text = ''
clock = pygame.time.Clock() 
done = False

while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        matrice=text
                        done=True
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode
                if event.key == pygame.K_ESCAPE:
                    done = True

            if event.type == pygame.MOUSEBUTTONDOWN:
                
                if input_matrice.collidepoint(event.pos):
                    
                    active = not active
                else:
                    active = False
                
                color = color_active if active else color_inactive
            if event.type == pygame.MOUSEBUTTONDOWN:
                if boutton_q.collidepoint(pygame.mouse.get_pos()):
                    done = True
                else:
                    pass
            
        screen.fill((30, 30, 30))
        txt_surface = font.render(text, True, color)
        width = max(200, txt_surface.get_width()+10)
        input_matrice.w = width
        
        clock.tick(30)
        current_time = time.time()
        elapsed_time = current_time - start_time
        
        
        ecran() 
        if elapsed_time > 1:
            fps = int(clock.get_fps())
            start_time = current_time
        compteurFPS()
        
        pygame.draw.rect(screen, color, input_matrice, 2)
        screen.blit(txt_surface, (input_matrice.x+5, input_matrice.y+5))
        pygame.draw.circle(screen, WHITE, (pygame.mouse.get_pos()), 10)
        pygame.display.flip()
        

matrice=int(matrice)
pygame.mouse.set_visible(True)
def fond():
    screen.fill((179,252,187))
    carre = pygame.Rect(12, 30, 350, 340)
    couleur_bordure = (0, 0, 0)
    pygame.draw.rect(screen, (217, 217, 217), carre) #carre gris
    pygame.draw.rect(screen, (139, 139, 139), (12, 30, 350, 340), 5)  #bordure carre gris
    rectangle = pygame.Rect(400, 12, 1050, 1050)
    # Dégradé de couleur
    color1 = (122, 203, 101)
    color2 = (55, 132, 68)
    for y in range(rectangle.height):
      ratio = y/rectangle.height
      red = int(color1[0] + ratio * (color2[0] - color1[0]))
      green = int(color1[1] + ratio * (color2[1] - color1[1]))
      blue = int(color1[2] + ratio * (color2[2] - color1[2]))
      color = (red, green, blue)
      pygame.draw.line(screen, color, (rectangle.left, rectangle.top+y), (rectangle.right, rectangle.top+y))
    #boucle quadrillage Longueur
    j=0
    i=0
    while i<matrice:
     collone = pygame.Rect(400+j,12,1050//matrice,1050)
     pygame.draw.rect(screen, (59, 114, 54), collone,1)
     j=j+1050//matrice
     i=i+1
    #boucle quadrillage Largeur
    j=0
    i=0
    while i<matrice:
      collone = pygame.Rect(400,12+j,1050,1050//matrice)
      pygame.draw.rect(screen, (59, 114, 54), collone,1)
      j=j+1050//matrice
      i=i+1
    pygame.draw.rect(screen, (0, 0, 0), (400, 12, 1050, 1050), 1) #bordure gros carré



police = pygame.font.Font('freesansbold.ttf', 30)

def afficher_nbre_herbe(jeu):
    nbre = police.render(str(jeu.nbreHerbe()), True, (238,125,43))
    titre = police.render("Nbre Herbe :", True, BLACK)
    screen.blit(nbre, (220,40))
    screen.blit(titre, (26,38))

def afficher_nbre_mouton(jeu):
    nbre = police.render(str(jeu.nbreMouton()), True, (238,125,43))
    titre = police.render("Nbre Mouton :", True, BLACK)
    screen.blit(nbre, (250,70))
    screen.blit(titre, (26,70))

def afficher_nbre_loup(jeu):
    nbre = police.render(str(jeu.nbreLoup()), True, (238,125,43))
    titre = police.render("Nbre Loup :", True, BLACK)
    screen.blit(nbre, (250,100))
    screen.blit(titre, (26,100))

def afficher_horloge(jeu):
    nbre = police.render(str(jeu.horloge), True, (238,125,43))
    titre = police.render("Horloge :", True, BLACK)
    screen.blit(nbre, (250,130))
    screen.blit(titre, (26,130))
def resultat(jeu):
        jeu.resultats_herbe.append(jeu.monde.nbHerbe())
        jeu.resultats_moutons.append(len(jeu.mouton))
        jeu.resultats_lou.append (len(jeu.lou))
        jeu.resultats_chasseur.append(len(jeu.chasseur))
        

m=Monde(matrice,dureeRepousse)
jeu = Simulation(nbreMouton,nbreLoup,nbreChasseur,findumonde,m,100)
done=False
while not done:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN: 
            if boutton_q.collidepoint(pygame.mouse.get_pos()):
                done = True
            else:
                pass
    clock.tick()  
    fond()
    jeu.affichageDirt()
    afficher_nbre_mouton(jeu)
    afficher_nbre_loup(jeu)
    boutton_quitter()
    afficher_nbre_herbe(jeu)
    afficher_horloge(jeu)
    jeu.simPygame()
    if jeu.max_moutons<jeu.nbreMouton():
        done=True
    if jeu.fin_du_monde==jeu.horloge:
        done=True
    resultat(jeu)

    
    pygame.time.delay(1000)
    pygame.display.flip()
done=False
while not done: 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN: 
            if boutton_q.collidepoint(pygame.mouse.get_pos()):
                done = True
            else:
                pass
  
    # remplir l'écran avec du noir 
    screen.fill(BLACK) 
  
    # afficher GAME OVER 
    font = pygame.font.SysFont('Calibri', 128, True, False) 
    text = font.render("GAME OVER", True, WHITE) 
    screen.blit(text, [621, 463]) 
    boutton_quitter() 
    pygame.display.flip() 
  
    clock.tick(60)
    

pygame.quit()




jeu.graphe()
