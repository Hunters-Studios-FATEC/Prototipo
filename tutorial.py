import pygame as pg
from pygame.locals import *
import sys
import json
from classes import Allies, Enemy, party, jacob
from cutscene_manager import CutSceneManager, Cutscene
from fase1 import mov_f_1
import random
from assets.cutscenes import *
from battle_ui import BattleBox, Button, BattleLog

# pygame init
pg.init()

# player pos
xpos = 1

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
cut2 = json.load(open("assets/cutscenes/cut2.json", encoding='utf-8'))
cut3 = json.load(open("assets/cutscenes/cut3.json", encoding='utf-8'))
cut4 = json.load(open("assets/cutscenes/cut4.json", encoding='utf-8'))
cut5 = json.load(open("assets/cutscenes/cut5.json", encoding='utf-8'))
cut6 = json.load(open("assets/cutscenes/cut6.json", encoding='utf-8'))
cut7 = json.load(open("assets/cutscenes/cut7.json", encoding='utf-8'))
cut8 = json.load(open("assets/cutscenes/cut8.json", encoding='utf-8'))

cutscene2 = Cutscene(cut2)
cutscene3 = Cutscene(cut3)
cutscene4 = Cutscene(cut4)
cutscene5 = Cutscene(cut5)
cutscene6 = Cutscene(cut6)
cutscene7 = Cutscene(cut7)
cutscene8 = Cutscene(cut8)

gerenciador = CutSceneManager(screen)

# Contagem de salas
salas = 0

# FPS
fps = pg.time.Clock()

enemy_list = []
party = [jacob]


# battle call
def combate_tutorial():
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

    # enemy generator

    def enemy_gen():
        vida = [50, 100, 150]
        dano = [8, 13, 18]
        cor = [(0, 0, 0), (50, 50, 50), (100, 100, 100)]
        nomes = ["nazi_melee", "nazi_atirador", "nazi_tank"]

        enemy_dict = {}
        for i in range(2):
            enemy_dict["enemy{0}".format(i)] = Enemy(random.choice(vida), random.choice(dano), random.choice(cor),
                                                     random.choice(nomes), random.randint(6, 10))
        for enemy in range(len(enemy_dict)):
            enemy_list.append(enemy_dict["enemy{0}".format(enemy)])

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
        if salas == 6 and jacob.vida <= 100:
            cutscene(cutscene5)

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
                                    salas -= 1
                                    mov_tutorial()
                            elif enemy_select:  # caso a ação escolhida seja ataque, seleciona o inimigo
                                if battle_state == 'attack':
                                    party[ally_index].attack(enemy_list[seta_vert_pos])
                                    log_text = "{} atacou por {}".format(party[ally_index].nome,
                                                                         party[ally_index].dano_m)
                                    ally_index += 1
                                    enemy_select = False
                                    battle_state = 'action'
                                if battle_state == 'skill':
                                    party[ally_index].skill(enemy_list[seta_vert_pos])
                                    log_text = "{} atirou por {}".format(party[ally_index].nome,
                                                                         party[ally_index].dano_m)
                                    ally_index += 1
                                    enemy_select = False
                                    battle_state = 'action'
                        else:  # checa se o jogador atual está morto ou não
                            log_text = "{} está morto".format(party[ally_index].nome)
                            ally_index += 1  # aumenta em 1 a variavel que determina qual aliado ataca

        if party[0].vida > 0:  # desenha a imagem dos aliados caso estejam vivos
            screen.blit(party[0].img, allies_pos[0])
        for e in range(len(enemy_list)):  # desenha a imagem dos inimigos caso estejam vivos
            screen.blit(enemy_list[e].img, enemy_pos[e])
            screen.blit(enemy_list[e].barra, (enemy_pos[e][0] - 25, enemy_pos[e][1] - 20))  # barra de vida
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
            if party[0].vida < 0:
                party[0].vida = 0
            enemy_life += enemy_list[i].vida  # cria uma variavel da vida total dos inimigos
            party_life += party[0].vida  # cria uma variavel da vida total da party

        if party_life <= jacob.vida / 2:  # retorna ao movimento em caso de vitória ou derrota
            cutscene(cutscene5)

            for i in range(len(party)):
                party[0].lvl_up(soma_xp)

            mov_tutorial()

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
        pg.display.update()


# mov call
def mov_tutorial():
    global xpos, salas, gerenciador, enemy_list
    enemy_list.clear()
    xchange = 0
    salas += 1

    while True:
        if salas == 1:
            cutscene(cutscene2)
            salas -= 1

        if salas == 4:
            cutscene(cutscene3)
            salas -= 1

        if salas == 6:
            cutscene(cutscene4)

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
            trans_tutorial()
        if xpos <= 0:
            xpos = 0

        xpos += xchange

        # draw
        screen.blit(ground, (0, SCREEN_H - 150))
        screen.blit(jacob.img, (xpos, SCREEN_H - 200))
        pg.display.update()


# Transição
def trans_tutorial():
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
        mov_tutorial()


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
            if cut == cutscene4:
                combate_tutorial()

            elif cut == cutscene5:
                cutscene(cutscene6)

            elif cut == cutscene6:
                cutscene(cutscene7)

            elif cut == cutscene7:
                cutscene(cutscene8)

            elif cut == cutscene8:
                mov_f_1()

            else:
                trans_tutorial()
