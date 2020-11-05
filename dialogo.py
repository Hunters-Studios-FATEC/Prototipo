import pygame as pg
import sys
from cutscene_manager import CutSceneManager, Cutscene
import json


pg.init()
screen = pg.display.set_mode((1280, 720))
clock = pg.time.Clock()

# variável que permite rodar as cuscenes. Pórem ela é redundante, pois já tem uma no manager.
# A dúvida é, como pegar cuscene_manager.cutscene_running e fazer ela fazer o papel dessa variável.
# Só que quando ela fica no mesmo loop, ela roda direto a segundo, ou a ultima que foi colocada.

cutscene_playing = False

cutscene_manager = CutSceneManager(screen)

# Carregar os metadados da cutscene dos dicionários json. Encoding para exibir caracter português
cut1 = json.load(open('assets/cutscenes/cut25.json', encoding='utf-8'))
cutscene_one = Cutscene(cut1)

cut2 = json.load(open('assets/cutscenes/cut2.json', encoding='utf-8'))
cutscene_two = Cutscene(cut2)

cutscene_playing = True
while cutscene_playing:
    clock.tick(60)

    # Events
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

    # Quando a cutscene começa, o manager salva o nome para que não resete para os valores padrões.
    cutscene_manager.start_cutscene(cutscene_one)

    # Update em cada frame.
    cutscene_manager.update()

    # Em cada frame, o manager desenha a caixa de diálogo
    screen.fill((255, 255, 255))
    cutscene_manager.draw()

    # update do display
    pg.display.flip()

    # Acaba a cutscene para rodar o loop do jogo normalmente
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
