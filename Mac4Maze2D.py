import pygame
import position1 as Position
import perso1 as Perso
from random import randint
from labyManager1 import LabyManager
from pygame.locals import *
from constantes import*
from time import sleep

#playloop = True
#win = False
cases = [False, True]

def gameLoop(perso, lm, shadow):
    global cases
    playloop = True
    win = False
    cases = [False, True]

    while not (perso.pos == lm.exitPosition) and perso.alive and cases[1]:
        #cases = [win, playloop]
        lm.displayLaby(shadow)
        pygame.display.set_caption("MacGyver have: " + lm.nbInGameObjets() + "/3 objects. Use arrows to move")
        #lm.message_display("Utilisez les flêches du clavier pour vous déplacer!", shadow)
        pygame.display.flip()
        pygame.key.set_repeat(400,30)
        for event in pygame.event.get():
            if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                cases[1] = False
            elif event.type == KEYDOWN:
                if event.key == K_LEFT :
                    perso.goLeft()
                elif event.key == K_RIGHT:
                    perso.goRight()
                elif event.key == K_UP:
                    perso.goUp()
                elif event.key == K_DOWN:
                    perso.goDown()
        cases[0] = perso.alive #=TRUE EXCEPT IF GUARD KILL MAC
    if not cases[0] and cases[1]:
        lm.message_display("You are DEAD, try again!", shadow)
        pygame.display.flip()
        sleep(3)
    elif cases[0] and not cases[1]:
        lm.message_display("Are you LIVING?! Tape y or n.", shadow)
        pygame.display.flip()
        flag = 1
        while flag:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_y:
                        cases[0] = True
                        cases[1] = False
                        lm.displayLaby(shadow)
                        lm.message_display("Yes, OK The game is stopping!", shadow)
                        pygame.display.flip()
                        sleep(2)
                        flag = 0
                    elif event.key == K_n:
                        cases[0] = False
                        cases[1] = True
                        lm.displayLaby(shadow)
                        lm.message_display("No, OK the game restarts!", shadow)
                        pygame.display.flip()
                        sleep(2)
                        flag = 0
    elif cases[0] and cases[1]:
        lm.message_display("The Guard is DOWN! Go OUT? Tape y or n.", shadow)
        pygame.display.flip()
        flag = 1
        while flag:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_y:
                        cases[0] = True
                        cases[1] = True
                        lm.displayLaby(shadow)
                        lm.message_display("Yes, OK you are going out!", shadow)
                        pygame.display.flip()
                        sleep(2)
                        flag = 0
                    elif event.key == K_n:
                        cases[0] = False
                        cases[1] = True
                        lm.displayLaby(shadow)
                        lm.message_display("No, OK the game restarts!", shadow)
                        pygame.display.flip()
                        sleep(2)
                        flag = 0
    
        
def main():
######FONCTION PRINCIPALE##############
    pygame.init()
    shadow = pygame.display.set_mode((cote_fenetre, cote_fenetre))
    lm = LabyManager()
    while not cases[0] and cases[1]:
        """Récupération du fichier texte laby nettoyé"""
        lm.initializeGame()
        perso = Perso.Perso(lm.initPosition, lm)
        lm.displayLaby(shadow)
        """affiche l'écran avec les éléments du blit dans l'ordre du code"""
        pygame.display.set_caption('MacGyver Maze')
        pygame.display.flip()
        pygame.key.set_repeat(400,30) 
        gameLoop(perso, lm, shadow)
    if cases[0] and cases[1]:
        lm.displayLaby(shadow)
        pygame.display.set_caption('MacGyver win')
        lm.message_display("Congrats ! You are out alive !", shadow)
        pygame.display.flip()
        sleep(2)
    elif cases[0] and not cases[1]:
        lm.displayLaby(shadow)
        pygame.display.set_caption('MacGyver win')
        lm.message_display("Thanks for playing! See you soon!", shadow)
        pygame.display.flip()
        sleep(2)

if __name__ == "__main__":
    main()

