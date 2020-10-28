import pygame as pg
from pygame.locals import *
import sys
import json
from classes import *
from boss_f_1 import combate_boss
from cutscene_manager import CutSceneManager, Cutscene
import random
from assets.cutscenes import *
from battle_ui import BattleBox, Button, BattleLog

# pygame init
pg.init()

# player pos
xpos = 1

# fase/sala
fase_n = 1
sala_n = 1

# transição
transition = 'fora de batalha'

# screen setup
SCREEN_W = 1280
SCREEN_H = 720
screen = pg.display.set_mode((SCREEN_W, SCREEN_H))

# imgs setup
ground = pg.Surface((SCREEN_W, 150))
ground.fill((139, 69, 13))
battle_box = BattleBox(screen)
battle_log = BattleLog(screen)
seta = pg.image.load("assets/sprites/SETA1.png")
seta_vert = pg.image.load("assets/sprites/SETA1_vert.png")
tfont = pg.font.Font("assets/fontes/Very Damaged.ttf", 50)

# dialogos
cut9 = json.load(open("assets/cutscenes/cut9.json", encoding='utf-8'))
cut10 = json.load(open("assets/cutscenes/cut10.json", encoding='utf-8'))
cut11 = json.load(open("assets/cutscenes/cut11.json", encoding='utf-8'))
cut12 = json.load(open("assets/cutscenes/cut12.json", encoding='utf-8'))
cut13 = json.load(open("assets/cutscenes/cut13.json", encoding='utf-8'))

cutscene9 = Cutscene(cut9)
cutscene10 = Cutscene(cut10)
cutscene11 = Cutscene(cut11)
cutscene12 = Cutscene(cut12)
cutscene13 = Cutscene(cut13)

gerenciador = CutSceneManager(screen)

# Contagem de salas
salas = 0

# FPS
fps = pygame.time.Clock()

# Party
party = [jacob]

# battle call
def combate():

    global xpos, salas
    xpos -= 1

    # enemy/player list and positioning
    allies_pos = []
    enemy_pos = []
    for i in range(4):
        allies_pos.append((250 - (80 * i), SCREEN_H - 250))
        enemy_pos.append((770 + (150 * i), SCREEN_H - 250))

    # index na lista de inimigos/posição da seta da seleção de inimigos
    seta_vert_pos = 0

    # select arrow positioning
    setax = 0
    setay = 0
    axisx = True
    axisy = True
    battle_state = 'action'
    player_turn = True

    # index do aliado na lista party
    ally_index = 0
    enemy_select = False

    # inimigo atacando
    turno_inimigo = 0
    chosen_player = 0

    # random enemy generator
    enemy_gen()

    # texto que aparece na caixa de log, é mudado a cada ação
    log_text = None

    ground_2 = pg.Surface((SCREEN_W, SCREEN_H * 0.3))
    ground_2.fill((139, 69, 13))

    soma_xp = 0

    for i in range(len(enemy_list)):
        soma_xp += enemy_list[i].xp_drop

    print(soma_xp)

    while True:
        screen.fill((0, 255, 255))

        for event in pg.event.get():
            if event.type == QUIT:
                pg.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    if player_turn:
                        if battle_state != 'action':  # sair da seleção de inimigos
                            battle_state = 'action'
                            enemy_select = False
                if event.key == K_d or event.key == K_a:
                    if player_turn:
                        if battle_state == 'action':  # muda a seta de escolha de ação no eixo X
                            axisx = not axisx
                        elif enemy_select:  # muda a seta de escolha de inimigos
                            if event.key == K_d:
                                seta_vert_pos += 1
                            if event.key == K_a:
                                seta_vert_pos -= 1
                if event.key == K_w or event.key == K_s:
                    if player_turn:
                        if battle_state == 'action':  # muda a seta de escolha de ação no eixo Y
                            axisy = not axisy
                if event.key == K_RETURN:
                    if player_turn:
                        if party[ally_index].vida > 0:
                            if battle_state == 'action':  # seleciona a ação escolhida
                                if axisx and axisy:
                                    battle_state = 'attack'
                                    enemy_select = True
                                elif axisx and not axisy:
                                    battle_state = 'skill'
                                    enemy_select = True
                                elif not axisx and axisy:
                                    party[ally_index].dmg_red = 0.5
                                    log_text = "{} defende".format(party[ally_index].nome)
                                    ally_index += 1
                                else:
                                    if salas == 5:
                                        log_text = "SIFODE AE OTARIO"
                                    else:
                                        salas -= 1
                                        mov_f_1()

                            elif enemy_select:  # caso a ação escolhida seja ataque, seleciona o inimigo
                                if battle_state == 'attack':
                                    party[ally_index].attack(enemy_list[seta_vert_pos])
                                    log_text = "{} atacou por {}".format(party[ally_index].nome, party[ally_index].dano_m)
                                    ally_index += 1
                                    enemy_select = False
                                    battle_state = 'action'
                                if battle_state == 'skill':
                                    party[ally_index].skill(enemy_list[seta_vert_pos])
                                    log_text = "{} atirou por {}".format(party[ally_index].nome, party[ally_index].dano_m)
                                    ally_index += 1
                                    enemy_select = False
                                    battle_state = 'action'
                        else:  # checa se o jogador atual está morto ou não
                            log_text = "{} está morto".format(party[ally_index].nome)
                            ally_index += 1  # aumenta em 1 a variavel que determina qual aliado ataca

        for i in range(len(party)):
            if party[i].vida > 0:  # desenha a imagem dos aliados caso estejam vivos
                screen.blit(party[i].img, allies_pos[i])
        for e in range(len(enemy_list)):  # desenha a imagem dos inimigos caso estejam vivos
            screen.blit(enemy_list[e].img, enemy_pos[e])
            screen.blit(enemy_list[e].barra, (enemy_pos[e][0] - 25, enemy_pos[e][1] - 20)) # barra de vida
            enemy_list[e].life_update()

        for i in range(len(enemy_list)):  # remove da lista de inimigos os que morreram
            if enemy_list[i].vida <= 0:
                enemy_list.pop(i)
                break

        # action select
        if battle_state == 'action':  # define a posição x da seta de ação
            if axisx:
                setax = 150
            else:
                setax = 370

        if battle_state == 'action':  # define a posição y da seta de ação
            if axisy:
                setay = 560
            else:
                setay = 620

        if ally_index >= len(party):  # reseta o turno dos aliados
            ally_index = 0
            player_turn = False

        enemy_life = 0
        party_life = 0
        for i in range(len(enemy_list)):
            if enemy_list[i].vida < 0:  # impede a vida dos grupos de ficar negativa
                enemy_list[i].vida = 0
            enemy_life += enemy_list[i].vida  # cria uma variavel da vida total dos inimigos

        for i in range(len(party)):
            if party[i].vida < 0:
                party[i].vida = 0
            party_life += party[i].vida  # cria uma variavel da vida total da party

        if enemy_life <= 0 or party_life <= 0:  # retorna ao movimento em caso de vitória ou derrota
            if salas == 5:
                cutscene(cutscene10)

            salas -= 1

            for i in range(len(party)):
                party[i].lvl_up(soma_xp)

            mov_f_1()

        if turno_inimigo >= len(enemy_list):  # retorna ao turno do jogador
            turno_inimigo = 0
            player_turn = True

        if not player_turn:
            if enemy_list[turno_inimigo].vida > 0:  # escolhe a ação inimiga com base em chance

                action_prob = random.randint(1, 10)
                for i in range(len(party)):
                    chosen_player = random.randint(0, len(party) - 1)
                    if party[chosen_player].vida > 0:
                        break
                pg.time.wait(1000)

                if enemy_list[turno_inimigo].vida > enemy_list[turno_inimigo].vida * 0.4:
                    if 1 <= action_prob <= 7:
                        enemy_list[turno_inimigo].ataque(party[chosen_player])
                        log_text = "inimigo {} atacou {} por {}".format(enemy_list[turno_inimigo].nome,
                                                                        party[chosen_player].nome,
                                                                        enemy_list[turno_inimigo].dano)
                    else:
                        enemy_list[turno_inimigo].enemy_def()
                        log_text = "inimigo {} defende".format(enemy_list[turno_inimigo].nome)
                else:
                    if 1 <= action_prob <= 5:
                        enemy_list[turno_inimigo].ataque(party[chosen_player])
                        log_text = "inimigo {} atacou {} por {}".format(enemy_list[turno_inimigo].nome,
                                                                        party[chosen_player].nome,
                                                                        enemy_list[turno_inimigo].dano)
                    else:
                        enemy_list[turno_inimigo].enemy_def()
                        log_text = "inimigo {} defende".format(enemy_list[turno_inimigo].nome)
            turno_inimigo += 1

        if enemy_select:  # seta de seleção inimigo
            if seta_vert_pos < 0:
                seta_vert_pos = len(enemy_list) - 1
            if seta_vert_pos > len(enemy_list) - 1:
                seta_vert_pos = 0

        # desenho do resto das imagens
        screen.blit(ground_2, (0, SCREEN_H - 200))
        battle_log.update()
        battle_log.draw()
        battle_log.draw_text(log_text, screen)
        if player_turn:
            battle_box.update()
            battle_box.draw()
            if enemy_select:
                screen.blit(seta_vert, (enemy_pos[seta_vert_pos][0] + 5, enemy_pos[seta_vert_pos][1] - 100))
            if battle_state == 'action':
                screen.blit(seta, (setax, setay))

        if salas == 5 and enemy_life == 0:
            cutscene(cutscene10)

        pg.display.update()


# mov call
def mov_f_1():
    enemy_list.clear()
    global xpos, salas, gerenciador
    xchange = 0
    salas += 1

    while True:
        if salas == 5:
            party.append(kazi)
            cutscene(cutscene9)

        if salas == 9:
            cutscene(cutscene11)

        #if salas == 6:
            #cutscene(cutscene4)
            #salas -= 1

        screen.fill((0, 255, 255))

        # key events
        for event in pg.event.get():
            if event.type == QUIT:
                pg.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_d:
                    xchange = +1
                if event.key == K_a:
                    xchange = -1
            if event.type == KEYUP:
                if event.key == K_a or K_d:
                    xchange = 0

        # player movement
        if xpos >= 1230:
            xpos = 1
            trans()
        if xpos <= 0:
            xpos = 0

        xpos += xchange

        # random encounter
        if ((xpos / 100) % 1) == 0 and xpos is not 0:
            chance = random.randint(1, 50)
            if chance == 1:
                pg.time.wait(1000)
                combate()

        # draw
        screen.blit(ground, (0, SCREEN_H - 150))
        screen.blit(jacob.img, (xpos, SCREEN_H - 200))
        print(salas)
        #print(jacob.level, jacob.xp)
        pg.display.update()


# Transição
def trans():
    screen.fill((20, 20, 20))
    texto = tfont.render("Carregando...", True, (230, 230, 230))
    texto_rect = texto.get_rect()
    texto_rect.topleft = (640 - (texto_rect.w / 2), 360 - (texto_rect.h / 2))
    print(texto_rect.size)
    while True:
        for event in pg.event.get():
            if event.type == QUIT:
                pg.quit()
                sys.exit()

        screen.blit(texto, texto_rect)
        pg.display.update()
        pg.time.wait(1500)
        mov_f_1()


def cutscene(cut):
    global salas
    screen.fill((0, 0, 0))
    while True:
        fps.tick(60)
        for event in pg.event.get():
            if event.type == QUIT:
                pg.quit()
                sys.exit()

        gerenciador.start_cutscene(cut)
        gerenciador.draw()
        gerenciador.update()
        pg.display.update()
        if not gerenciador.cutscene_running:
            if cut == cutscene9:
                combate()

            if cut == cutscene11:
                combate_boss()

            else:
                trans()

mov_f_1()