import pygame, sys, random
from pygame.locals import *
from assets.cutscenes import *
from cutscene_manager import CutSceneManager, Cutscene
import json
from classes import *
from battle_ui import BattleBox, Button, BattleLog

# init
pygame.init()

fps = pygame.time.Clock()

# screen
SCREEN_H = 720
SCREEN_W = 1280
screen = pygame.display.set_mode((1280, 720))

# fonts
font_menu = pygame.font.Font("assets/fontes/Very Damaged.ttf", 100)
font_menu_2 = pygame.font.Font("assets/fontes/Very Damaged.ttf", 50)
font_menu_3 = pygame.font.Font("assets/fontes/Very Damaged.ttf", 24)
tfont = pygame.font.Font("assets/fontes/Very Damaged.ttf", 50)

# texts
# text = font.render("Teste", True, (255, 255, 255))
play = font_menu_2.render("Play", True, (255, 255, 255))
options = font_menu_2.render("Options", True, (255, 255, 255))
new_game = font_menu_2.render('New Game', True, (255, 255, 255))
load_game = font_menu_2.render('Load Game', True, (255, 255, 255))
X = font_menu_2.render("X", True, (0, 0, 0))
gam = font_menu.render("Game", True, (255, 255, 255))
opt = font_menu.render("Options", True, (255, 255, 255))
save_text = font_menu_2.render('Choose a slot:', True, (255, 255, 255))
slots = (font_menu_2.render('Slot 1', True, (255, 255, 255)), font_menu_2.render('Slot 2', True, (255, 255, 255)),
         font_menu_2.render('Slot 3', True, (255, 255, 255)))
mov_log_text = ""

# Bacgkground menu
bg = pygame.image.load("assets/backgrounds/bg.jpeg")

# battlebox
battle_box = BattleBox(screen)
battle_log = BattleLog(screen)

# ground
ground = pygame.Surface((SCREEN_W, 150))
ground.fill((139, 69, 13))

# player info
xpos = 1
salas = 0
party = [jacob]

# select seta
seta = pygame.image.load("assets/sprites/SETA1.png")
seta_vert = pygame.image.load("assets/sprites/SETA1_vert.png")

# Cutscenes
cut1 = json.load(open("assets/cutscenes/cut1.json", encoding='utf-8'))
cut2 = json.load(open("assets/cutscenes/cut2.json", encoding='utf-8'))
cut3 = json.load(open("assets/cutscenes/cut3.json", encoding='utf-8'))
cut4 = json.load(open("assets/cutscenes/cut4.json", encoding='utf-8'))
cut5 = json.load(open("assets/cutscenes/cut5.json", encoding='utf-8'))
cut6 = json.load(open("assets/cutscenes/cut6.json", encoding='utf-8'))
cut7 = json.load(open("assets/cutscenes/cut7.json", encoding='utf-8'))
cut8 = json.load(open("assets/cutscenes/cut8.json", encoding='utf-8'))
cut9 = json.load(open("assets/cutscenes/cut9.json", encoding='utf-8'))
cut10 = json.load(open("assets/cutscenes/cut10.json", encoding='utf-8'))
cut11 = json.load(open("assets/cutscenes/cut11.json", encoding='utf-8'))
cut12 = json.load(open("assets/cutscenes/cut12.json", encoding='utf-8'))
cut13 = json.load(open("assets/cutscenes/cut13.json", encoding='utf-8'))

cutscene1 = Cutscene(cut1)
cutscene2 = Cutscene(cut2)
cutscene3 = Cutscene(cut3)
cutscene4 = Cutscene(cut4)
cutscene5 = Cutscene(cut5)
cutscene6 = Cutscene(cut6)
cutscene7 = Cutscene(cut7)
cutscene8 = Cutscene(cut8)
cutscene9 = Cutscene(cut9)
cutscene10 = Cutscene(cut10)
cutscene11 = Cutscene(cut11)
cutscene12 = Cutscene(cut12)
cutscene13 = Cutscene(cut13)

gerenciador = CutSceneManager(screen)

# boss
inacio = hitler

# transição
trans_state = "tutorial"


# main menu
def menu_start():
    menu_select = True
    game_select = False
    load_file = -1
    while True:

        global screen
        screen.blit(bg, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.VIDEORESIZE:
                screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if game_select and load_file == -1:
                        game_select = False
                    elif game_select and load_file >= 0:
                        load_file = -1
                    else:
                        pygame.quit()
                        sys.exit()
                if event.key == pygame.K_s:
                    if load_file == -1:
                        menu_select = not menu_select
                    else:
                        if load_file < 2:
                            load_file += 1
                        else:
                            load_file = 0
                if event.key == pygame.K_w:
                    if load_file == -1:
                        menu_select = not menu_select
                    else:
                        if load_file > 0:
                            load_file -= 1
                        else:
                            load_file = 2
                if event.key == pygame.K_RETURN:
                    if not game_select:
                        if menu_select:
                            game_select = True
                        else:
                            pass
                    else:
                        if load_file == -1:
                            if menu_select:
                                cutscene(cutscene1, "tutorial")
                                game_select = False
                            else:
                                load_file = 0
                        else:
                            if load_file == 0:
                                load = open('save00.txt', 'r')
                                pass
                                load.close()
                            elif load_file == 1:
                                load = open('save01.txt', 'r')
                                pass
                                load.close()
                            else:
                                load = open('save02.txt', 'r')
                                pass
                                load.close()

        # buttons
        # screen.blit(text, (screen.get_width() / 2 - text.get_rect().width / 2, 100))
        if not game_select:
            screen.blit(play, (screen.get_width() / 2 - play.get_rect().width / 2, 300))
            screen.blit(options, (screen.get_width() / 2 - options.get_rect().width / 2, 380))
        else:
            if load_file == -1:
                screen.blit(new_game, (screen.get_width() / 2 - new_game.get_rect().width / 2, 300))
                screen.blit(load_game, (screen.get_width() / 2 - load_game.get_rect().width / 2, 380))
            else:
                for pos, slt in enumerate(slots):
                    screen.blit(slt, (screen.get_width() / 2 - slt.get_rect().width / 2, 300 + 80 * pos))

        # X mark
        if not game_select:
            if menu_select:
                screen.blit(X, (screen.get_width() / 2 - play.get_rect().width / 2 - X.get_rect().width, 300))
            else:
                screen.blit(X, (screen.get_width() / 2 - options.get_rect().width / 2 - X.get_rect().width, 380))
        else:
            if load_file == -1:
                if menu_select:
                    screen.blit(X, (screen.get_width() / 2 - new_game.get_rect().width / 2 - X.get_rect().width, 300))
                else:
                    screen.blit(X, (screen.get_width() / 2 - load_game.get_rect().width / 2 - X.get_rect().width, 380))
            else:
                screen.blit(X, (screen.get_width() / 2 - slots[0].get_rect().width / 2
                                - X.get_rect().width, 300 + 80 * load_file))

        pygame.display.update()


def combate_tutorial():
    party = [jacob]
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

    def enemy_gen_tutorial():
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

    enemy_gen_tutorial()

    # texto que aparece na caixa de log, é mudado a cada ação
    log_text = None

    ground_2 = pygame.Surface((SCREEN_W, SCREEN_H * 0.3))
    ground_2.fill((139, 69, 13))

    soma_xp = 0

    for i in range(len(enemy_list)):
        soma_xp += enemy_list[i].xp_drop

    print(soma_xp)

    while True:

        screen.fill((0, 255, 255))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
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
                                    if party[ally_index].ammo > 0:
                                        battle_state = 'skill'
                                        enemy_select = True
                                    else:
                                        log_text = "{} está sem munnição".format(party[ally_index])
                                elif not axisx and axisy:
                                    party[ally_index].dmg_red = 0.5
                                    log_text = "{} defende".format(party[ally_index].nome)
                                    ally_index += 1
                                else:
                                    log_text = "não pode fugir judeu"
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
                                                                         party[ally_index].dano_r)
                                    ally_index += 1
                                    enemy_select = False
                                    battle_state = 'action'
                        else:  # checa se o jogador atual está morto ou não
                            log_text = "{} está morto".format(party[ally_index].nome)
                            ally_index += 1  # aumenta em 1 a variavel que determina qual aliado ataca

        if party[0].vida > 0:  # desenha a imagem dos aliados caso estejam vivos
            screen.blit(party[0].img, allies_pos[0])
            screen.blit(party[0].barra, (allies_pos[0][0] - 25, allies_pos[0][1] - 20))
            party[0].life_update()
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

        if jacob.vida <= jacob.vida_total / 2:  # retorna ao movimento em caso de vitória ou derrota
            cutscene(cutscene5, "fase1")

            for i in range(len(party)):
                party[0].lvl_up(soma_xp)

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
                pygame.time.wait(1000)

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
        pygame.display.update()


def combate_fase1():
    global xpos, salas
    xpos -= 1

    # enemy/player list and positioning
    allies_pos = []
    enemy_pos = []
    for i in range(4):
        allies_pos.append((510 - (150 * i), SCREEN_H - 250))
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
    enemy_gen([10, 20, 30], [5, 7, 10])

    # texto que aparece na caixa de log, é mudado a cada ação
    log_text = None

    ground_2 = pygame.Surface((SCREEN_W, SCREEN_H * 0.3))
    ground_2.fill((139, 69, 13))

    soma_xp = 0

    for i in range(len(enemy_list)):
        soma_xp += enemy_list[i].xp_drop

    print(soma_xp)

    while True:
        screen.fill((0, 255, 255))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
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
                                    if party[ally_index].ammo > 0:
                                        battle_state = 'skill'
                                        enemy_select = True
                                    else:
                                        log_text = "{} está sem munnição".format(party[ally_index])
                                elif not axisx and axisy:
                                    party[ally_index].dmg_red = 0.5
                                    log_text = "{} defende".format(party[ally_index].nome)
                                    pygame.time.wait(500)
                                    battle_log.update()
                                    battle_log.draw()
                                    battle_log.draw_text(log_text, screen)
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
                                    log_text = "{} atacou por {}".format(party[ally_index].nome,
                                                                         party[ally_index].dano_m)
                                    ally_index += 1
                                    enemy_select = False
                                    battle_state = 'action'
                                if battle_state == 'skill':
                                    party[ally_index].skill(enemy_list[seta_vert_pos])
                                    log_text = "{} atirou por {}".format(party[ally_index].nome,
                                                                         party[ally_index].dano_r)
                                    ally_index += 1
                                    enemy_select = False
                                    battle_state = 'action'
                        else:  # checa se o jogador atual está morto ou não
                            log_text = "{} está morto".format(party[ally_index].nome)
                            ally_index += 1  # aumenta em 1 a variavel que determina qual aliado ataca

        for i in range(len(party)):
            if party[i].vida > 0:  # desenha a imagem dos aliados caso estejam vivos
                screen.blit(party[i].img, allies_pos[i])
                screen.blit(party[i].barra, (allies_pos[i][0] - 25, allies_pos[i][1] - 20))
                party[i].life_update()
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

        if enemy_life <= 0:  # retorna ao movimento em caso de vitória ou derrota
            if salas == 5:
                cutscene(cutscene10, "fase1")

            salas -= 1

            for i in range(len(party)):
                party[i].lvl_up(soma_xp)

            mov_f_1()
        elif party_life <= 0:
            fim_jogo()

        if turno_inimigo >= len(enemy_list):  # retorna ao turno do jogador
            turno_inimigo = 0
            ally_index = 0
            player_turn = True

        if not player_turn:
            if enemy_list[turno_inimigo].vida > 0:  # escolhe a ação inimiga com base em chance

                action_prob = random.randint(1, 10)
                for i in range(len(party)):
                    chosen_player = random.randint(0, len(party) - 1)
                    if party[chosen_player].vida > 0:
                        break
                pygame.time.wait(1000)

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

        if ally_index >= len(party):  # reseta o turno dos aliados
            ally_index = 0
            player_turn = False

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
            cutscene(cutscene10, "fase1")

        pygame.display.update()


def combate_boss():
    global xpos, inacio
    xpos -= 1

    # enemy/player list and positioning
    allies_pos = []
    enemy_pos = []
    for i in range(4):
        allies_pos.append((510 - (150 * i), SCREEN_H - 250))
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

    ground_2 = pygame.Surface((SCREEN_W, SCREEN_H * 0.3))
    ground_2.fill((139, 69, 13))

    soma_xp = 0
    soma_xp += hitler2.xpdrop

    print(soma_xp)

    while True:
        screen.fill((0, 255, 255))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
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
                                    if party[ally_index].ammo > 0:
                                        battle_state = 'skill'
                                        enemy_select = True
                                    else:
                                        log_text = "{} está sem munnição".format(party[ally_index])
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
                                                                         party[ally_index].dano_r)
                                    ally_index += 1
                                    enemy_select = False
                                    battle_state = 'action'
                        else:  # checa se o jogador atual está morto ou não
                            log_text = "{} está morto".format(party[ally_index].nome)
                            ally_index += 1  # aumenta em 1 a variavel que determina qual aliado ataca

        for i in range(len(party)):
            if party[i].vida > 0:  # desenha a imagem dos aliados caso estejam vivos
                screen.blit(party[i].img, allies_pos[i])
                screen.blit(party[i].barra, (allies_pos[i][0] - 25, allies_pos[i][1] - 20))
                party[i].life_update()

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
            cutscene(cutscene12, "boss1")

        if enemy_life <= 0:  # retorna ao movimento em caso de vitória ou derrota
            for i in range(len(party)):
                party[i].lvl_up(soma_xp)
            cutscene(cutscene13, "boss1")

        if party_life <= 0:
            fim_jogo()

        if not player_turn:
            if inacio.vida > 0:  # escolhe a ação inimiga com base em chance

                action_prob = random.randint(1, 10)
                for i in range(len(party)):
                    chosen_player = random.randint(0, len(party) - 1)
                    if party[chosen_player].vida > 0:
                        break
                pygame.time.wait(1000)

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

        if ally_index >= len(party):  # reseta o turno dos aliados
            ally_index = 0
            player_turn = False

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

        pygame.display.update()


def mov_tutorial():
    rest_count = True
    global xpos, salas, gerenciador, enemy_list, mov_log_text
    enemy_list.clear()
    mov_log_text = ""
    xchange = 0
    salas += 1

    while True:
        if salas == 1:
            cutscene(cutscene2, "tutorial")
            salas -= 1

        if salas == 4:
            cutscene(cutscene3, "tutorial")
            salas -= 1

        if salas == 6:
            cutscene(cutscene4, "tutorial")

        screen.fill((0, 255, 255))

        # key events
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_d:
                    xchange = +1
                if event.key == K_a:
                    xchange = -1
                if event.key == K_v:
                    for i in range(len(party)):
                        party[i].procurar()
                        mov_log_text = "o grupo recuperou 5 balas cada"
                if rest_count:
                    if event.key == K_c:
                        for i in range(len(party)):
                            party[i].rest()
                            rest_count = False
                            mov_log_text = "o grupo recuperou 50 de vida"
            if event.type == KEYUP:
                if event.key == K_a or K_d:
                    xchange = 0

        # player movement
        if xpos >= 1230:
            xpos = 1
            trans("tutorial")
        if xpos <= 0:
            xpos = 0

        xpos += xchange

        mov_log = font_menu_3.render(mov_log_text, True, (0, 0, 0))

        # draw
        screen.blit(ground, (0, SCREEN_H - 150))
        screen.blit(jacob.img, (xpos, SCREEN_H - 200))
        screen.blit(mov_log, (0, 0))
        pygame.display.update()


def mov_f_1():
    rest_count = True
    enemy_list.clear()
    global xpos, salas, gerenciador, trans_state, mov_log_text
    if trans_state == "fase1":
        salas = 0
        trans_state = "standby"
    mov_log_text = ""
    xchange = 0
    salas += 1

    while True:
        if salas == 5:
            party.append(kazi)
            cutscene(cutscene9, "fase1")

        if salas == 9:
            cutscene(cutscene11, "fase1")

        # if salas == 6:
        # cutscene(cutscene4)
        # salas -= 1

        screen.fill((0, 255, 255))

        # key events
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_d:
                    xchange = +1
                if event.key == K_a:
                    xchange = -1
                if event.key == K_SPACE:
                    for i in range(len(party)):
                        print(party[i].xp, party[i].to_next_lvl)
                if event.key == K_v:
                    for i in range(len(party)):
                        party[i].procurar()
                        mov_log_text = "o grupo recuperou 5 balas cada"
                if rest_count:
                    if event.key == K_c:
                        for i in range(len(party)):
                            party[i].rest()
                            rest_count = False
                            mov_log_text = "o grupo recuperou 50 de vida"
            if event.type == KEYUP:
                if event.key == K_a or K_d:
                    xchange = 0

        # player movement
        if xpos >= 1230:
            xpos = 1
            trans("fase1")
        if xpos <= 0:
            xpos = 0

        xpos += xchange

        # random encounter
        if ((xpos / 100) % 1) == 0 and xpos is not 0:
            chance = random.randint(1, 30)
            if chance == 1:
                pygame.time.wait(1000)
                combate_fase1()

        mov_log = font_menu_3.render(mov_log_text, True, (0, 0, 0))

        # draw
        screen.blit(ground, (0, SCREEN_H - 150))
        screen.blit(jacob.img, (xpos, SCREEN_H - 200))
        screen.blit(mov_log, (0, 0))
        pygame.display.update()


def trans(fase):
    screen.fill((20, 20, 20))
    texto = tfont.render("Carregando...", True, (230, 230, 230))
    texto_rect = texto.get_rect()
    texto_rect.topleft = (640 - (texto_rect.w / 2), 360 - (texto_rect.h / 2))
    print(texto_rect.size)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        screen.blit(texto, texto_rect)
        pygame.display.update()
        pygame.time.wait(1500)
        if fase == "tutorial":
            mov_tutorial()
        elif fase == "fase1":
            mov_f_1()
        elif fase == "boss1":
            combate_boss()


def cutscene(cut, fase):
    global salas, trans_state
    screen.fill((0, 0, 0))
    while True:
        fps.tick(60)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        gerenciador.start_cutscene(cut)
        gerenciador.draw()
        gerenciador.update()
        pygame.display.update()

        if not gerenciador.cutscene_running:
            if cut == cutscene4:
                combate_tutorial()

            elif cut == cutscene5:
                cutscene(cutscene6, "fase1")

            elif cut == cutscene6:
                cutscene(cutscene7, "fase1")

            elif cut == cutscene7:
                cutscene(cutscene8, "fase1")

            elif cut == cutscene8:
                trans_state = "fase1"
                mov_f_1()

            elif cut == cutscene9:
                combate_fase1()

            elif cut == cutscene11:
                combate_boss()

            if cut == cutscene12:
                combate_boss()

            else:
                trans(fase)


def fim_jogo():
    PRETO = (0, 0, 0)
    BRANCO = (255, 255, 255)

    # variaveis de gameover

    fonte = pygame.font.Font("assets/fontes/Very Damaged.ttf", 100)
    fonte_botao = pygame.font.Font("assets/fontes/Very Damaged.ttf", 30)

    load_game = fonte_botao.render("Carregar Jogo Salvo", True, BRANCO)
    return_menu = fonte_botao.render("Voltar ao Menu", True, BRANCO)

    flavor_text = fonte_botao.render("Então você perdeu a oportunidade...", True, BRANCO)

    X = fonte_botao.render("X", True, BRANCO)

    game_over = fonte.render("GAME OVER", True, BRANCO)

    fim_de_jogo = True
    selector = True
    while fim_de_jogo:
        # regras

        screen.fill(PRETO)

        # eventos

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_s:
                    selector = False

                if e.key == pygame.K_w:
                    selector = True

                if e.key == pygame.K_RETURN:
                    if not selector:
                        menu_start()
                    else:
                        pass

        # desenhar telas e botoes
        screen.blit(game_over, (screen.get_width() / 2 - game_over.get_rect().width / 2, 100))
        screen.blit(flavor_text, (screen.get_width() / 2 - flavor_text.get_rect().width / 2, 300))
        screen.blit(load_game, (screen.get_width() / 2 - load_game.get_rect().width / 2, 450))
        screen.blit(return_menu, (screen.get_width() / 2 - return_menu.get_rect().width / 2, 530))

        if selector:
            screen.blit(X, (screen.get_width() / 2 - load_game.get_rect().width / 2 - X.get_rect().width - 10, 450))
        else:
            screen.blit(X, (screen.get_width() / 2 - return_menu.get_rect().width / 2 - X.get_rect().width - 10, 530))

        pygame.display.update()


mov_f_1()
