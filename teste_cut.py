import pygame, sys
from pygame.locals import *
from assets.cutscenes import *
from cutscene_manager import CutSceneManager, Cutscene
import json

pygame.init()

fps = pygame.time.Clock()

# screen
SCREEN_H = 720
SCREEN_W = 1280
screen = pygame.display.set_mode((1280, 720))

cut1 = json.load(open("assets/cutscenes/cut25.json", encoding='utf-8'))
cutscene1 = Cutscene(cut1)
gerenciador = CutSceneManager(screen)

while True:
    fps.tick(60)
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    gerenciador.start_cutscene(cutscene1)
    gerenciador.draw()
    gerenciador.update()

    pygame.display.update()
