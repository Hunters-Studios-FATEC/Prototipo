import pygame as pg
import sys
from cutscene_manager import CutSceneManager, Cutscene
import json


pg.init()
screen = pg.display.set_mode((1280, 720))
clock = pg.time.Clock()

cutscene_playing = False

cutscene_manager = CutSceneManager(screen)

cut1 = json.load(open('assets/cutscenes/cut25.json', encoding='utf-8'))
cutscene_one = Cutscene(cut1)

cut2 = json.load(open('assets/cutscenes/cut2.json', encoding='utf-8'))
cutscene_two = Cutscene(cut2)

cutscene_playing = True
while cutscene_playing:
    clock.tick(60)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

    cutscene_manager.start_cutscene(cutscene_one)

    cutscene_manager.update()

    screen.fill((255, 255, 255))
    cutscene_manager.draw()

    pg.display.flip()

    if not cutscene_manager.cutscene_running:
        cutscene_playing = False
        break


cutscene_playing = True
while cutscene_playing:
    clock.tick(60)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

    cutscene_manager.start_cutscene(cutscene_two)

    cutscene_manager.update()

    screen.fill((255, 255, 255))
    cutscene_manager.draw()

    pg.display.flip()

    if not cutscene_manager.cutscene_running:
        cutscene_playing = False
        break
