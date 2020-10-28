import pygame as pg
from pygame.locals import *
import sys
import json
from classes import *
from cutscene_manager import CutSceneManager, Cutscene
import random
from assets.cutscenes import *
from battle_ui import BattleBox, Button, BattleLog

# pygame init
pg.init()

# player pos
xpos = 1

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
cut12 = json.load(open("assets/cutscenes/cut12.json", encoding='utf-8'))
cut13 = json.load(open("assets/cutscenes/cut13.json", encoding='utf-8'))

cutscene12 = Cutscene(cut12)
cutscene13 = Cutscene(cut13)

gerenciador = CutSceneManager(screen)

# FPS
fps = pygame.time.Clock()

#boss
inacio = hitler

party = [jacob, kazi]

def combate_boss():
    global xpos, inacio
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

    # texto que aparece na caixa de log, é mudado a cada ação
    log_text = None

    ground_2 = pg.Surface((SCREEN_W, SCREEN_H * 0.3))
    ground_2.fill((139, 69, 13))

    soma_xp = 0
    soma_xp += hitler2.xpdrop

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
                                    log_text = "SIFUDEU KKK"
                            elif enemy_select:  # caso a ação escolhida seja ataque, seleciona o inimigo
                                if battle_state == 'attack':
                                    party[ally_index].attack(inacio)
                                    log_text = "{} atacou por {}".format(party[ally_index].nome,
                                                                         party[ally_index].dano_m)
                                    ally_index += 1
                                    enemy_select = False
                                    battle_state = 'action'
                                if battle_state == 'skill':
                                    party[ally_index].skill(inacio)
                                    log_text = "{} atirou por {}".format(party[ally_index].nome,
                                                                         party[ally_index].dano_m)
                                    ally_index += 1
                                    enemy_select = False
                                    battle_state = 'action'
                        else:  # checa se o jogador atual está morto ou não
                            log_text = "{} está morto".format(party[ally_index].nome)
                            ally_index += 1  # aumenta em 1 a variavel que determina qual aliado ataca

        for i in range(len(party)):
            if party[i].vida > 0:  # desenha a imagem dos aliados caso estejam vivos
                screen.blit(party[i].img, allies_pos[i])

        screen.blit(inacio.img, enemy_pos[0])
        screen.blit(inacio.barra, (enemy_pos[0][0] - 25, enemy_pos[0][1] - 20))  # barra de vida
        inacio.life_update()

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

        if inacio.vida < 0:  # impede a vida dos grupos de ficar negativa
            inacio.vida = 0
        enemy_life += inacio.vida  # cria uma variavel da vida total dos inimigos

        for i in range(len(party)):
            if party[i].vida < 0:
                party[i].vida = 0
            party_life += party[i].vida  # cria uma variavel da vida total da party

        if inacio == hitler and enemy_life <= inacio.vida_total / 2:
            inacio = hitler2
            cutscene(cutscene12)

        if enemy_life <= 0:  # retorna ao movimento em caso de vitória ou derrota
            for i in range(len(party)):
                party[i].lvl_up(soma_xp)
            cutscene(cutscene13)



        if not player_turn:
            if inacio.vida > 0:  # escolhe a ação inimiga com base em chance

                action_prob = random.randint(1, 10)
                for i in range(len(party)):
                    chosen_player = random.randint(0, len(party) - 1)
                    if party[chosen_player].vida > 0:
                        break
                pg.time.wait(1000)

                if inacio.vida > inacio.vida * 0.4:
                    if 1 <= action_prob <= 7:
                        inacio.ataque(party[chosen_player])
                        log_text = "inimigo {} atacou {} por {}".format(inacio.nome,
                                                                        party[chosen_player].nome,
                                                                        inacio.dano)
                    else:
                        inacio.enemy_def()
                        log_text = "inimigo {} defende".format(inacio.nome)
                else:
                    if 1 <= action_prob <= 5:
                        inacio.ataque(party[chosen_player])
                        log_text = "inimigo {} atacou {} por {}".format(inacio.nome,
                                                                        party[chosen_player].nome,
                                                                        inacio.dano)
                    else:
                        inacio.enemy_def()
                        log_text = "inimigo {} defende".format(inacio.nome)
            player_turn = True

        if enemy_select:  # seta de seleção inimigo
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
        #mov_f_1()

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
            if cut == cutscene12:
                combate_boss()

            else:
                trans()

