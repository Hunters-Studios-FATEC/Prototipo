import pygame, sys, random
from pygame.locals import *
from assets.cutscenes import *
from cutscene_manager import CutSceneManager, Cutscene
import json
from classes import *
from battle_ui import BattleBox, Button, BattleLog
from _thread import start_new_thread
import socket

# init
pygame.init()
pygame.mixer.init()

fps = pygame.time.Clock()

# screen
SCREEN_H = 720
SCREEN_W = 1280
screen = pygame.display.set_mode((1280, 720))
screen.fill((0, 0, 0))

# fonts
font_menu = pygame.font.Font("assets/fontes/Very Damaged.ttf", 100)
font_menu_2 = pygame.font.Font("assets/fontes/Very Damaged.ttf", 50)
font_menu_3 = pygame.font.Font("assets/fontes/Very Damaged.ttf", 24)
tfont = pygame.font.Font("assets/fontes/Very Damaged.ttf", 50)

# sfx
walk = pygame.mixer.Sound("assets/audio/Ambiente/passos.ogg")
walk_timer = 0
shot = pygame.mixer.Sound("assets/audio/Combate/pistol.wav")
melee = pygame.mixer.Sound("assets/audio/Combate/swish_2.wav")
run = pygame.mixer.Sound("assets/audio/Combate/run.ogg")
menu_st = pygame.mixer.Sound("assets/audio/Menus/clock_fundo.ogg")
enter = pygame.mixer.Sound("assets/audio/Menus/Enter.ogg")
enter.set_volume(0.4)
select = pygame.mixer.Sound("assets/audio/Menus/select.ogg")

# musica
# musicF1 = pygame.mixer.Sound("assets/audio/Musics/warzone.wav")
# musicF1.set_volume(0.05)
# musicF2 = pygame.mixer.Sound("assets/audio/Musics/wave animada.ogg")
# musicF2.set_volume(0.05)
# musicF3 = pygame.mixer.Sound("assets/audio/Musics/suspense.wav")
# musicF3.set_volume(0.05)
# musicHitler = pygame.mixer.Sound("assets/audio/Musics/hotler.ogg")
# musicHitler.set_volume(0.05)
count = 0

# channels
ch1 = pygame.mixer.Channel(0)
ch2 = pygame.mixer.Channel(1)

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
chronos_fase2 = False

# player info
direction = "R"
xpos = 1
salas = 0
party = [jacob]
chr_list = [jacob, kazi, kenji, barbara]
fase4 = False

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
cut14 = json.load(open("assets/cutscenes/cut14.json", encoding='utf-8'))
cut15 = json.load(open("assets/cutscenes/cut15.json", encoding='utf-8'))
cut16 = json.load(open("assets/cutscenes/cut16.json", encoding='utf-8'))
cut17 = json.load(open("assets/cutscenes/cut17.json", encoding='utf-8'))
cut18 = json.load(open("assets/cutscenes/cut18.json", encoding='utf-8'))
cut19 = json.load(open("assets/cutscenes/cut19.json", encoding='utf-8'))
cut20 = json.load(open("assets/cutscenes/cut20.json", encoding='utf-8'))
cut21 = json.load(open("assets/cutscenes/cut21.json", encoding='utf-8'))
cut22 = json.load(open("assets/cutscenes/cut22.json", encoding='utf-8'))
cut23 = json.load(open("assets/cutscenes/cut23.json", encoding='utf-8'))
cut24 = json.load(open("assets/cutscenes/cut24.json", encoding='utf-8'))
cut25 = json.load(open("assets/cutscenes/cut25.json", encoding='utf-8'))

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
cutscene14 = Cutscene(cut14)
cutscene15 = Cutscene(cut15)
cutscene16 = Cutscene(cut16)
cutscene17 = Cutscene(cut17)
cutscene18 = Cutscene(cut18)
cutscene19 = Cutscene(cut19)
cutscene20 = Cutscene(cut20)
cutscene21 = Cutscene(cut21)
cutscene22 = Cutscene(cut22)
cutscene23 = Cutscene(cut23)
cutscene24 = Cutscene(cut24)
cutscene25 = Cutscene(cut25)  # Pós Créditos

gerenciador = CutSceneManager(screen)

# boss
inacio = hitler

# transição
trans_state = "tutorial"

# rest_count and find_b
rest_c = True
find_b = True

# loaded_content
loaded_content = False

# score conditions
save_cnt = 0
rest_cnt = 0
bullet_cnt = 0
death_cnt = 0

# music is playing condition
music_is_playing = False

# Enemy gen lists and names
prmg_images = ['assets/sprites/inimigos/primeiraguerran1.png', 'assets/sprites/inimigos/primeiraguerran2.png']
prmg_names = ['soldado', 'cabo', 'atirador']
fut_images = ['assets/sprites/inimigos/nazi1.png', 'assets/sprites/inimigos/nazi2.png']
fut_names = ['nazista', 'nazista', 'nazista']

# Cutscene backgrounds
bg_cut1 = pygame.image.load('assets/backgrounds/cut1.jpeg')
bg_cut1_2 = pygame.image.load('assets/backgrounds/cut1_2.png')
bg_cut1_3 = pygame.image.load('assets/backgrounds/cut1_3.png')
bg_cut2 = pygame.image.load('assets/backgrounds/cut2.png')
bg_cut3 = pygame.image.load('assets/backgrounds/cut3.png')
bg_cut4 = pygame.image.load('assets/backgrounds/cut4.png')
bg_cut5 = pygame.image.load('assets/backgrounds/cut1.jpeg')
bg_cut6 = pygame.image.load('assets/backgrounds/cut6.png')
bg_cut7 = pygame.image.load('assets/backgrounds/cut7.png')
bg_cut7_2 = pygame.image.load('assets/backgrounds/cut7_2.png')
bg_cut8 = pygame.image.load('assets/backgrounds/cut8.png')
bg_cut8_2 = pygame.image.load('assets/backgrounds/cut8_2.png')
bg_cut9 = pygame.image.load('assets/backgrounds/cut9.png')
bg_cut10 = pygame.image.load('assets/backgrounds/cut10.png')
bg_cut11 = pygame.image.load('assets/backgrounds/cut11.png')
bg_cut12 = pygame.image.load('assets/backgrounds/cut12.png')
bg_cut13 = pygame.image.load('assets/backgrounds/cut13f1.png')
bg_cut13_2 = pygame.image.load('assets/backgrounds/cut13f2.png')
bg_cut14 = pygame.image.load('assets/backgrounds/cut14.png')
bg_cut15 = pygame.image.load('assets/backgrounds/cut15.png')
bg_cut16 = pygame.image.load('assets/backgrounds/cut16.png')
bg_cut17 = pygame.image.load('assets/backgrounds/cut1.jpeg')
bg_cut18 = pygame.image.load('assets/backgrounds/cut1.jpeg')
bg_cut19 = pygame.image.load('assets/backgrounds/cut1.jpeg')
bg_cut20 = pygame.image.load('assets/backgrounds/cut1.jpeg')
bg_cut21 = pygame.image.load('assets/backgrounds/cut1.jpeg')
bg_cut22 = pygame.image.load('assets/backgrounds/cut1.jpeg')
bg_cut23 = pygame.image.load('assets/backgrounds/cut1.jpeg')
bg_cut24 = pygame.image.load('assets/backgrounds/cut1.jpeg')
bg_cut25 = pygame.image.load('assets/backgrounds/cut1.jpeg')


def music(count):
    if count == 0:
        # musicF1.play(-1)
        pygame.mixer.music.load("assets/audio/Musics/warzone.wav")
    elif count == 1:
        # musicF2.play(-1)
        pygame.mixer.music.load("assets/audio/Musics/wave animada.ogg")
    elif count == 2:
        # musicF3.play(-1)
        pygame.mixer.music.load("assets/audio/Musics/suspense.wav")
    elif count == 3:
        # musicHitler.play(-1)
        pygame.mixer.music.load("assets/audio/Musics/hotler.ogg")
    elif count == 4:
        # musicHitler.play(-1)
        pygame.mixer.music.load("assets/audio/Musics/wave malvadeza.ogg")
    elif count == 5:
        # musicHitler.play(-1)
        pygame.mixer.music.load("assets/audio/Musics/epic.ogg")
    pygame.mixer.music.set_volume(0.05)
    pygame.mixer.music.play(-1)


# main menu
def menu_start():
    menu_select = True
    game_select = False
    menu_st.play(-1)
    while True:

        global screen, salas, xpos, rest_c, find_b, loaded_content, fase4, save_cnt, rest_cnt, bullet_cnt, death_cnt

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if game_select:
                        game_select = False
                    else:
                        pygame.quit()
                        sys.exit()
                if event.key == pygame.K_s:
                    select.play()
                    menu_select = not menu_select
                if event.key == pygame.K_w:
                    select.play()
                    menu_select = not menu_select
                if event.key == pygame.K_RETURN:
                    if not game_select:
                        if menu_select:
                            game_select = True
                        else:
                            pass
                    else:
                        if menu_select:
                            pygame.mixer.stop()
                            enter.play()
                            cutscene(cutscene1, "tutorial", bg_cut1)
                            game_select = False
                        else:
                            loaded_data = load_file()
                            if loaded_data is not None:
                                for data in loaded_data['stats']:
                                    if data[3] == 0:
                                        # (vida, dano_m, dano_r, cor, nome, lvl, xp, ammo, inc_mel, inc_ran, inc_vida)
                                        jacob.vida = data[0]
                                        jacob.dano_m = data[1]
                                        jacob.dano_r = data[2]
                                        jacob.nome = "jacob"
                                        jacob.level = data[4]
                                        jacob.xp = data[5]
                                        jacob.ammo = data[6]
                                        jacob.inc_mel = data[7]
                                        jacob.inc_ran = data[8]
                                        jacob.inc_vida = data[9]
                                        jacob.load_stats()
                                    elif data[3] == 1:
                                        kazi.vida = data[0]
                                        kazi.dano_m = data[1]
                                        kazi.dano_r = data[2]
                                        kazi.nome = "kazi"
                                        kazi.level = data[4]
                                        kazi.xp = data[5]
                                        kazi.ammo = data[6]
                                        kazi.inc_mel = data[7]
                                        kazi.inc_ran = data[8]
                                        kazi.inc_vida = data[9]
                                        kazi.load_stats()
                                    elif data[3] == 2:
                                        kenji.vida = data[0]
                                        kenji.dano_m = data[1]
                                        kenji.dano_r = data[2]
                                        kenji.nome = "kenji"
                                        kenji.level = data[4]
                                        kenji.xp = data[5]
                                        kenji.ammo = data[6]
                                        kenji.inc_mel = data[7]
                                        kenji.inc_ran = data[8]
                                        kenji.inc_vida = data[9]
                                        kenji.load_stats()
                                    else:
                                        barbara.vida = data[0]
                                        barbara.dano_m = data[1]
                                        barbara.dano_r = data[2]
                                        barbara.nome = "barbara"
                                        barbara.level = data[4]
                                        barbara.xp = data[5]
                                        barbara.ammo = data[6]
                                        barbara.inc_mel = data[7]
                                        barbara.inc_ran = data[8]
                                        barbara.inc_vida = data[9]
                                        barbara.load_stats()
                                for character in loaded_data['party'][1:]:
                                    if character == "kazi":
                                        party.append(kazi)
                                    elif character == "kenji":
                                        party.append(kenji)
                                    else:
                                        party.append(barbara)
                                if loaded_data['lvl_room'][0] == 'fase2' or loaded_data['lvl_room'][0] == 'fase3':
                                    kazi.img = pygame.image.load("assets/sprites/peter/davidcombate.png")
                                salas = loaded_data['lvl_room'][1]
                                xpos = loaded_data['x_pos']
                                rest_c = loaded_data['rest_counter']
                                find_b = loaded_data['find_bullet']
                                loaded_content = True
                                save_cnt, rest_cnt, bullet_cnt, death_cnt = loaded_data['score_conds']
                                if len(loaded_data) > 7:
                                    fase4 = loaded_data['fase4']
                                trans(loaded_data['lvl_room'][0])

        screen.blit(bg, (0, 0))

        # buttons
        # screen.blit(text, (screen.get_width() / 2 - text.get_rect().width / 2, 100))
        if not game_select:
            screen.blit(play, (screen.get_width() / 2 - play.get_rect().width / 2, 300))
            screen.blit(options, (screen.get_width() / 2 - options.get_rect().width / 2, 380))
        else:
            screen.blit(new_game, (screen.get_width() / 2 - new_game.get_rect().width / 2, 300))
            screen.blit(load_game, (screen.get_width() / 2 - load_game.get_rect().width / 2, 380))

        # X mark
        if not game_select:
            if menu_select:
                screen.blit(X, (screen.get_width() / 2 - play.get_rect().width / 2 - X.get_rect().width, 300))
            else:
                screen.blit(X, (screen.get_width() / 2 - options.get_rect().width / 2 - X.get_rect().width, 380))
        else:
            if menu_select:
                screen.blit(X, (screen.get_width() / 2 - new_game.get_rect().width / 2 - X.get_rect().width, 300))
            else:
                screen.blit(X, (screen.get_width() / 2 - load_game.get_rect().width / 2 - X.get_rect().width, 380))

        pygame.display.update()


def combate_tutorial():
    jacob.img = pygame.image.load('assets/sprites/jacob/jacobcombate.png')
    bg = pygame.image.load('assets/backgrounds/placa_para_auschwitz.jpg')
    party = [jacob]
    global xpos, salas
    xpos -= 1

    # enemy/player list and positioning
    allies_pos = []
    enemy_pos = []
    for i in range(4):
        allies_pos.append((250 - (80 * i), SCREEN_H))
        enemy_pos.append((700 + (150 * i), SCREEN_H))

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
        cor = ['assets/sprites/inimigos/nazi1.png', 'assets/sprites/inimigos/nazi2.png']
        nomes = ["nazista", "nazista", "nazista"]

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
                    select.play()
                    if player_turn:
                        if battle_state == 'action':  # muda a seta de escolha de ação no eixo X
                            axisx = not axisx
                        elif enemy_select:  # muda a seta de escolha de inimigos
                            if event.key == K_d:
                                seta_vert_pos += 1
                            if event.key == K_a:
                                seta_vert_pos -= 1
                if event.key == K_w or event.key == K_s:
                    select.play()
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
            cutscene(cutscene5, "fase1", bg_cut5)

            for i in range(len(party)):
                party[0].lvl_up(soma_xp)

        if turno_inimigo >= len(enemy_list):  # retorna ao turno do jogador
            turno_inimigo = 0
            player_turn = True

        if not player_turn:
            if enemy_list[turno_inimigo].vida > 0:  # escolhe a ação inimiga com base em chance

                action_prob = random.randint(1, 10)
                while True:
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

        screen.blit(bg, (0, -190))  # background

        if party[0].vida > 0:  # desenha a imagem dos aliados caso estejam vivos
            screen.blit(party[0].img, (allies_pos[0][0], allies_pos[0][1] - 530))
            screen.blit(party[0].barra, (allies_pos[0][0] + 60, allies_pos[0][1] - 550))
            party[0].life_update()
        for e in range(len(enemy_list)):  # desenha a imagem dos inimigos caso estejam vivos
            screen.blit(enemy_list[e].img, (enemy_pos[e][0], enemy_pos[e][1] - 530))
            screen.blit(enemy_list[e].barra, (enemy_pos[e][0] + 80, enemy_pos[e][1] - 540))  # barra de vida
            enemy_list[e].life_update()

        # desenho do resto das imagens
        battle_log.update()
        battle_log.draw()
        battle_log.draw_text(log_text, screen)
        if player_turn:
            battle_box.update()
            battle_box.draw()
            if enemy_select:
                screen.blit(seta_vert, (enemy_pos[seta_vert_pos][0] + 100, enemy_pos[seta_vert_pos][1] - 630))
            if battle_state == 'action':
                screen.blit(seta, (setax, setay))
        pygame.display.update()


def combate_fase1():
    bg = pygame.image.load('assets/backgrounds/no man_s land.png')
    jacob.img = pygame.image.load('assets/sprites/jacob/jacobcombate.png')
    global xpos, salas, death_cnt
    xpos -= 1

    # enemy/player list and positioning
    allies_pos = []
    enemy_pos = []
    for i in range(4):
        allies_pos.append((510 - (150 * i), SCREEN_H))
        enemy_pos.append((700 + (150 * i), SCREEN_H))

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
    enemy_gen([10, 20, 30], [5, 7, 10], prmg_images, prmg_names)

    # texto que aparece na caixa de log, é mudado a cada ação
    log_text = None

    ground_2 = pygame.Surface((SCREEN_W, SCREEN_H * 0.3))
    ground_2.fill((139, 69, 13))

    soma_xp = 0

    for i in range(len(enemy_list)):
        soma_xp += enemy_list[i].xp_drop

    print(soma_xp)

    while True:

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
                    ch1.play(select)
                    if player_turn:
                        if battle_state == 'action':  # muda a seta de escolha de ação no eixo X
                            axisx = not axisx
                        elif enemy_select:  # muda a seta de escolha de inimigos
                            if event.key == K_d:
                                seta_vert_pos += 1
                            if event.key == K_a:
                                seta_vert_pos -= 1
                if event.key == K_w or event.key == K_s:
                    ch1.play(select)
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
                                    if salas == 5 and not fase4:
                                        log_text = "SIFODE AE OTARIO"
                                    else:
                                        salas -= 1
                                        ch1.play(run)
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
            if salas == 5 and not fase4:
                cutscene(cutscene10, "fase1")

            if salas == 5:
                cutscene(cutscene10, "fase1", bg_cut10)
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
                while True:
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
                        if party[chosen_player].vida <= 0:
                            death_cnt += 1
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

        screen.blit(bg, (0, -190))

        for i in range(len(party)):
            if party[i].vida > 0:  # desenha a imagem dos aliados caso estejam vivos
                screen.blit(party[i].img, (allies_pos[i][0], allies_pos[i][1] - 530))
                screen.blit(party[i].barra, (allies_pos[i][0] + 60, allies_pos[i][1] - 550))
                party[i].life_update()
        for e in range(len(enemy_list)):  # desenha a imagem dos inimigos caso estejam vivos
            screen.blit(enemy_list[e].img, (enemy_pos[e][0], enemy_pos[e][1] - 530))
            screen.blit(enemy_list[e].barra, (enemy_pos[e][0] + 80, enemy_pos[e][1] - 540))  # barra de vida
            enemy_list[e].life_update()

        # desenho do resto das imagens
        battle_log.update()
        battle_log.draw()
        battle_log.draw_text(log_text, screen)
        battle_box.update()
        battle_box.draw()
        if player_turn:
            if enemy_select:
                screen.blit(seta_vert, (enemy_pos[seta_vert_pos][0] + 100, enemy_pos[seta_vert_pos][1] - 630))
            if battle_state == 'action':
                screen.blit(seta, (setax, setay))

        if salas == 5 and enemy_life == 0:
            cutscene(cutscene10, "fase1", bg_cut10)

        pygame.display.update()


def combate_boss():
    pygame.mixer.stop()
    count = 3
    bg = pygame.image.load('assets/backgrounds/no man_s land.png')
    jacob.img = pygame.image.load('assets/sprites/jacob/jacobcombate.png')
    global xpos, inacio, death_cnt, music_is_playing
    xpos -= 1

    # enemy/player list and positioning
    allies_pos = []
    enemy_pos = []
    for i in range(4):
        allies_pos.append((510 - (150 * i), SCREEN_H))
        enemy_pos.append((700 + (150 * i), SCREEN_H))

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
    if fase4:
        inacio = hitler2
    else:
        inacio = hitler

    soma_xp = 0
    soma_xp += inacio.xpdrop

    print(soma_xp)

    while True:
        if not music_is_playing:
            start_new_thread(music, (count,))
            music_is_playing = True

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
                    ch1.play(select)
                    if player_turn:
                        if battle_state == 'action':  # muda a seta de escolha de ação no eixo X
                            axisx = not axisx
                        elif enemy_select:  # muda a seta de escolha de inimigos
                            if event.key == K_d:
                                seta_vert_pos += 1
                            if event.key == K_a:
                                seta_vert_pos -= 1
                if event.key == K_w or event.key == K_s:
                    ch1.play(select)
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
                                        log_text = "{} está sem munição".format(party[ally_index].nome)
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

        if enemy_life <= 0 and not fase4:  # retorna ao movimento em caso de vitória ou derrota
            for i in range(len(party)):
                party[i].lvl_up(soma_xp)
            cutscene(cutscene12, "fase2", bg_cut12)

        if enemy_life <= 0 and fase4:  # retorna ao movimento em caso de vitória ou derrota
            cutscene(cutscene24, "boss4", bg_cut24)

        if party_life <= 0:
            fim_jogo()

        if not player_turn:
            if inacio.vida > 0:  # escolhe a ação inimiga com base em chance

                action_prob = random.randint(1, 10)
                while True:
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
                        if party[chosen_player].vida <= 0:
                            death_cnt += 1
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

        screen.blit(bg, (0, -190))

        for i in range(len(party)):
            if party[i].vida > 0:  # desenha a imagem dos aliados caso estejam vivos
                screen.blit(party[i].img, (allies_pos[i][0], allies_pos[i][1] - 530))
                screen.blit(party[i].barra, (allies_pos[i][0] + 60, allies_pos[i][1] - 550))
                party[i].life_update()
        screen.blit(inacio.img,(enemy_pos[0][0], enemy_pos[0][1] - 530))
        screen.blit(inacio.barra, (enemy_pos[0][0] + 90, enemy_pos[0][1] - 550))  # barra de vida
        inacio.life_update()

        # desenho do resto das imagens
        battle_log.update()
        battle_log.draw()
        battle_log.draw_text(log_text, screen)
        battle_box.update()
        battle_box.draw()
        if player_turn:
            if enemy_select:
                screen.blit(seta_vert, (enemy_pos[seta_vert_pos][0] + 100, enemy_pos[seta_vert_pos][1] - 650))
            if battle_state == 'action':
                screen.blit(seta, (setax, setay))

        pygame.display.update()


def combate_fase2():
    bg = pygame.image.load('assets/backgrounds/nazi cyberpunk.png')
    jacob.img = pygame.image.load('assets/sprites/jacob/jacobcombate.png')
    global xpos, salas, death_cnt
    xpos -= 1

    # enemy/player list and positioning
    allies_pos = []
    enemy_pos = []
    for i in range(4):
        allies_pos.append((510 - (150 * i), SCREEN_H))
        enemy_pos.append((700 + (150 * i), SCREEN_H))

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
    enemy_gen([10, 20, 30], [5, 7, 10], fut_images, fut_names)

    # texto que aparece na caixa de log, é mudado a cada ação
    log_text = None

    ground_2 = pygame.Surface((SCREEN_W, SCREEN_H * 0.3))
    ground_2.fill((139, 69, 13))

    soma_xp = 0

    for i in range(len(enemy_list)):
        soma_xp += enemy_list[i].xp_drop

    print(soma_xp)

    while True:

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
                    ch1.play(select)
                    if player_turn:
                        if battle_state == 'action':  # muda a seta de escolha de ação no eixo X
                            axisx = not axisx
                        elif enemy_select:  # muda a seta de escolha de inimigos
                            if event.key == K_d:
                                seta_vert_pos += 1
                            if event.key == K_a:
                                seta_vert_pos -= 1
                if event.key == K_w or event.key == K_s:
                    ch1.play(select)
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
                                        ch1.play(run)
                                        mov_f_2()

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

            salas -= 1

            for i in range(len(party)):
                party[i].lvl_up(soma_xp)

            mov_f_2()
        elif party_life <= 0:
            fim_jogo()

        if turno_inimigo >= len(enemy_list):  # retorna ao turno do jogador
            turno_inimigo = 0
            ally_index = 0
            player_turn = True

        if not player_turn:
            if enemy_list[turno_inimigo].vida > 0:  # escolhe a ação inimiga com base em chance

                action_prob = random.randint(1, 10)
                while True:
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
                        if party[chosen_player].vida <= 0:
                            death_cnt += 1
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

        screen.blit(bg, (0, -190))

        for i in range(len(party)):
            if party[i].vida > 0:  # desenha a imagem dos aliados caso estejam vivos
                screen.blit(party[i].img, ((allies_pos[i][0], allies_pos[i][1] - 530)))
                screen.blit(party[i].barra, (allies_pos[i][0] + 60, allies_pos[i][1] - 550))
                party[i].life_update()
        for e in range(len(enemy_list)):  # desenha a imagem dos inimigos caso estejam vivos
            screen.blit(enemy_list[e].img, (enemy_pos[e][0], enemy_pos[e][1] - 530))
            screen.blit(enemy_list[e].barra, (enemy_pos[e][0] + 80, enemy_pos[e][1] - 540))  # barra de vida
            enemy_list[e].life_update()

        # desenho do resto das imagens
        battle_log.update()
        battle_log.draw()
        battle_log.draw_text(log_text, screen)
        battle_box.update()
        battle_box.draw()
        if player_turn:
            if enemy_select:
                screen.blit(seta_vert, (enemy_pos[seta_vert_pos][0] + 100, enemy_pos[seta_vert_pos][1] - 630))
            if battle_state == 'action':
                screen.blit(seta, (setax, setay))

        pygame.display.update()


def combate_boss2():
    pygame.mixer.stop()
    bg = pygame.image.load('assets/backgrounds/nazi cyberpunk.png')
    jacob.img = pygame.image.load('assets/sprites/jacob/jacobcombate.png')
    global xpos, inacio, death_cnt, music_is_playing
    count = 4
    xpos -= 1

    # enemy/player list and positioning
    allies_pos = []
    enemy_pos = []
    for i in range(4):
        allies_pos.append((510 - (150 * i), SCREEN_H))
        enemy_pos.append((700 + (150 * i), SCREEN_H))

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
    inacio = antonio

    ground_2 = pygame.Surface((SCREEN_W, SCREEN_H * 0.3))
    ground_2.fill((139, 69, 13))

    soma_xp = 0
    soma_xp += inacio.xpdrop

    print(soma_xp)

    while True:

        if not music_is_playing:
            start_new_thread(music, (count,))
            music_is_playing = True

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
                    ch1.play(select)
                    if player_turn:
                        if battle_state == 'action':  # muda a seta de escolha de ação no eixo X
                            axisx = not axisx
                        elif enemy_select:  # muda a seta de escolha de inimigos
                            if event.key == K_d:
                                seta_vert_pos += 1
                            if event.key == K_a:
                                seta_vert_pos -= 1
                if event.key == K_w or event.key == K_s:
                    ch1.play(select)
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

        if enemy_life <= 0:  # retorna ao movimento em caso de vitória ou derrota
            for i in range(len(party)):
                party[i].lvl_up(soma_xp)
            cutscene(cutscene16, "fase3", bg_cut16)

        if party_life <= 0:
            fim_jogo()

        if not player_turn:
            if inacio.vida > 0:  # escolhe a ação inimiga com base em chance

                action_prob = random.randint(1, 10)
                while True:
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
                        if party[chosen_player].vida <= 0:
                            death_cnt += 1
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

        screen.blit(bg, (0, -190))

        for i in range(len(party)):
            if party[i].vida > 0:  # desenha a imagem dos aliados caso estejam vivos
                screen.blit(party[i].img, ((allies_pos[i][0], allies_pos[i][1] - 530)))
                screen.blit(party[i].barra, (allies_pos[i][0] + 50, allies_pos[i][1] - 550))
                party[i].life_update()
        screen.blit(inacio.img, (enemy_pos[0][0], enemy_pos[0][1] - 530))
        screen.blit(inacio.barra, (enemy_pos[0][0] + 150, enemy_pos[0][1] - 550))  # barra de vida
        inacio.life_update()

        # desenho do resto das imagens
        battle_log.update()
        battle_log.draw()
        battle_log.draw_text(log_text, screen)
        battle_box.update()
        battle_box.draw()
        if player_turn:
            if enemy_select:
                screen.blit(seta_vert, (enemy_pos[seta_vert_pos][0] + 150, enemy_pos[seta_vert_pos][1] - 650))
            if battle_state == 'action':
                screen.blit(seta, (setax, setay))

        pygame.display.update()


def combate_boss3():
    jacob.img = pygame.image.load('assets/sprites/jacob/jacobcombate.png')
    global xpos, inacio, chronos_fase2, death_cnt, music_is_playing
    count = 5
    xpos -= 1

    # enemy/player list and positioning
    allies_pos = []
    enemy_pos = []
    for i in range(4):
        allies_pos.append((510 - (150 * i), SCREEN_H))
        enemy_pos.append((700 + (150 * i), SCREEN_H))

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
    if not chronos_fase2:
        inacio = chronos

    ground_2 = pygame.Surface((SCREEN_W, SCREEN_H * 0.3))
    ground_2.fill((139, 69, 13))

    soma_xp = 0
    soma_xp += inacio.xpdrop

    print(soma_xp)

    while True:

        if not music_is_playing:
            start_new_thread(music, (count,))
            music_is_playing = True

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
                    ch1.play(select)
                    if player_turn:
                        if battle_state == 'action':  # muda a seta de escolha de ação no eixo X
                            axisx = not axisx
                        elif enemy_select:  # muda a seta de escolha de inimigos
                            if event.key == K_d:
                                seta_vert_pos += 1
                            if event.key == K_a:
                                seta_vert_pos -= 1
                if event.key == K_w or event.key == K_s:
                    ch1.play(select)
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

        if inacio == chronos:
            if enemy_life <= inacio.vida_total / 2:
                inacio = chronos2
                chronos_fase2 = True
                cutscene(cutscene20, "boss3", bg_cut20)

        if inacio == chronos2:
            if enemy_life <= 0:  # retorna ao movimento em caso de vitória ou derrota
                for i in range(len(party)):
                    party[i].lvl_up(soma_xp)
                cutscene(cutscene21, "fase4", bg_cut21)

        if party_life <= 0:
            fim_jogo()

        if not player_turn:
            if inacio.vida > 0:  # escolhe a ação inimiga com base em chance

                action_prob = random.randint(1, 10)
                while True:
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
                        if party[chosen_player].vida <= 0:
                            death_cnt += 1
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

        for i in range(len(party)):
            if party[i].vida > 0:  # desenha a imagem dos aliados caso estejam vivos
                screen.blit(party[i].img, (allies_pos[i][0], allies_pos[i][1] - 530))
                screen.blit(party[i].barra, (allies_pos[i][0] + 60, allies_pos[i][1] - 550))
                party[i].life_update()
        screen.blit(inacio.img, (enemy_pos[0][0], enemy_pos[0][1] - 530))
        screen.blit(inacio.barra, (enemy_pos[0][0] + 90, enemy_pos[0][1] - 550))  # barra de vida
        inacio.life_update()

        # desenho do resto das imagens
        screen.blit(ground_2, (0, SCREEN_H - 200))
        battle_log.update()
        battle_log.draw()
        battle_log.draw_text(log_text, screen)
        battle_box.update()
        battle_box.draw()
        if player_turn:
            if enemy_select:
                screen.blit(seta_vert, (enemy_pos[seta_vert_pos][0] + 115, enemy_pos[seta_vert_pos][1] - 650))
            if battle_state == 'action':
                screen.blit(seta, (setax, setay))

        pygame.display.update()


def combate_fase3():
    jacob.img = pygame.image.load('assets/sprites/jacob/jacobcombate.png')
    global xpos, salas, death_cnt
    xpos -= 1

    # enemy/player list and positioning
    allies_pos = []
    enemy_pos = []
    for i in range(4):
        allies_pos.append((510 - (150 * i), SCREEN_H))
        enemy_pos.append((700 + (150 * i), SCREEN_H))

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
    enemy_gen([10, 20, 30], [5, 7, 10], fut_images, fut_names)

    # texto que aparece na caixa de log, é mudado a cada ação
    log_text = None

    ground_2 = pygame.Surface((SCREEN_W, SCREEN_H * 0.3))
    ground_2.fill((139, 69, 13))

    soma_xp = 0

    for i in range(len(enemy_list)):
        soma_xp += enemy_list[i].xp_drop

    print(soma_xp)

    while True:

        screen.fill((130, 130, 130))

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
                    ch1.play(select)
                    if player_turn:
                        if battle_state == 'action':  # muda a seta de escolha de ação no eixo X
                            axisx = not axisx
                        elif enemy_select:  # muda a seta de escolha de inimigos
                            if event.key == K_d:
                                seta_vert_pos += 1
                            if event.key == K_a:
                                seta_vert_pos -= 1
                if event.key == K_w or event.key == K_s:
                    ch1.play(select)
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
                                        ch1.play(run)
                                        mov_f_3()

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

            salas -= 1

            for i in range(len(party)):
                party[i].lvl_up(soma_xp)

            mov_f_3()
        elif party_life <= 0:
            fim_jogo()

        if turno_inimigo >= len(enemy_list):  # retorna ao turno do jogador
            turno_inimigo = 0
            ally_index = 0
            player_turn = True

        if not player_turn:
            if enemy_list[turno_inimigo].vida > 0:  # escolhe a ação inimiga com base em chance

                action_prob = random.randint(1, 10)
                while True:
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
                        if party[chosen_player].vida <= 0:
                            death_cnt += 1
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

        for i in range(len(party)):
            if party[i].vida > 0:  # desenha a imagem dos aliados caso estejam vivos
                screen.blit(party[i].img, ((allies_pos[i][0], allies_pos[i][1] - 530)))
                screen.blit(party[i].barra, (allies_pos[i][0] + 60, allies_pos[i][1] - 550))
                party[i].life_update()
        for e in range(len(enemy_list)):  # desenha a imagem dos inimigos caso estejam vivos
            screen.blit(enemy_list[e].img, (enemy_pos[e][0], enemy_pos[e][1] - 530))
            screen.blit(enemy_list[e].barra, (enemy_pos[e][0] + 80, enemy_pos[e][1] - 540))  # barra de vida
            enemy_list[e].life_update()

        # desenho do resto das imagens
        screen.blit(ground_2, (0, SCREEN_H - 200))
        battle_log.update()
        battle_log.draw()
        battle_log.draw_text(log_text, screen)
        battle_box.update()
        battle_box.draw()
        if player_turn:
            if enemy_select:
                screen.blit(seta_vert, (enemy_pos[seta_vert_pos][0] + 100, enemy_pos[seta_vert_pos][1] - 630))
            if battle_state == 'action':
                screen.blit(seta, (setax, setay))

        pygame.display.update()


def mov_tutorial():
    bg = pygame.image.load('assets/backgrounds/varsóvia.png')
    rest_count = True
    find_bullet = True
    blit_bg = True
    global xpos, salas, gerenciador, enemy_list, mov_log_text, loaded_content, direction, walk_timer
    if loaded_content:
        rest_count = rest_c
        find_bullet = find_b
        loaded_content = False
    enemy_list.clear()
    mov_log_text = ""
    xchange = 0
    salas += 1

    while True:
        if salas == 1:
            cutscene(cutscene2, "tutorial", bg_cut2)
            salas -= 1

        if salas == 4:
            cutscene(cutscene3, "tutorial", bg_cut3)
            salas -= 1

        if salas == 6:
            cutscene(cutscene4, "tutorial", bg_cut4)

        if walk_timer > 0:
            walk_timer -= 1

        # key events
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_d:
                    xchange = +4.5
                    jacob.animate()
                    direction = "R"
                if event.key == K_a:
                    xchange = -4.5
                    jacob.animate()
                    direction = "L"
                if event.key == K_v:
                    if find_bullet:
                        for i in range(len(party)):
                            party[i].procurar()
                        find_bullet = False
                        mov_log_text = "o grupo recuperou 5 balas cada"
                if event.key == K_s:
                    # (self, vida, dano_m, dano_r, cor, nome, lvl, xp, ammo, inc_mel, inc_ran, inc_vida)
                    save_game(stats=[(chr_list[stats].vida, chr_list[stats].dano_m, chr_list[stats].dano_r,
                                      stats, chr_list[stats].level, chr_list[stats].xp, chr_list[stats].ammo,
                                      chr_list[stats].inc_mel, chr_list[stats].inc_ran, chr_list[stats].inc_vida)
                                     for stats in range(len(chr_list))], party=[character.nome for character in party],
                              lvl_room=(0, salas - 1), x_pos=xpos, rest_count=rest_count, find_bullet=find_bullet,
                              score_conds=(save_cnt, rest_cnt, bullet_cnt, death_cnt))
                    blit_bg = True
                if rest_count:
                    if event.key == K_c:
                        for i in range(len(party)):
                            party[i].rest()
                        rest_count = False
                        mov_log_text = "o grupo recuperou 50 de vida"
            if event.type == KEYUP:
                if event.key == K_a or K_d:
                    xchange = 0
                    jacob.stop("assets/sprites/jacob/jacob parado.png", direction)

        if xchange != 0:
            if walk_timer == 0:
                walk_timer = 28
                ch1.play(walk)

        # player movement
        if xpos >= 1230:
            xpos = 1
            trans("tutorial")
        if xpos <= 0:
            xpos = 0

        xpos += xchange

        # draw
        if blit_bg:
            screen.blit(bg, (0, 0))
            blit_bg = False
        else:
            screen.blit(bg, (xpos - 30, SCREEN_H - jacob.img.get_height()),
                        (xpos - 30, SCREEN_H - jacob.img.get_height(),
                         jacob.img.get_width() + 50, jacob.img.get_height()))
        screen.blit(jacob.img, (xpos, SCREEN_H - jacob.img.get_height()))
        jacob.update(0.25, direction)
        mov_log = font_menu_3.render(mov_log_text, True, (0, 0, 0))
        screen.blit(bg, (0, 0), (0, 0, mov_log.get_width(), mov_log.get_height()))
        screen.blit(mov_log, (0, 0))
        fps.tick(60)
        pygame.display.update()


def mov_f_1():
    count = 0
    bg = pygame.image.load("assets/backgrounds/no man_s land.png")
    rest_count = True
    find_bullet = True
    blit_bg = True
    enemy_list.clear()
    global xpos, salas, gerenciador, trans_state, mov_log_text, loaded_content, \
        rest_cnt, bullet_cnt, direction, walk_timer, ch1, music_is_playing
    if loaded_content:
        rest_count = rest_c
        find_bullet = find_b
        loaded_content = False
    if trans_state == "fase1":
        salas = 0
        trans_state = "standby"
    mov_log_text = ""
    xchange = 0
    salas += 1

    while True:
        if not music_is_playing:
            start_new_thread(music, (count,))
            music_is_playing = True

        if walk_timer > 0:
            walk_timer -= 1

        if salas == 5 and not fase4:
            cutscene(cutscene9, "fase1", bg_cut9)

        if salas == 9 and not fase4:
            cutscene(cutscene11, "fase1", bg_cut11)

        if salas == 9 and fase4:
            cutscene(cutscene23, "boss1", bg_cut23)

        # key events
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_d:
                    xchange = +4.5
                    jacob.animate()
                    direction = "R"
                if event.key == K_a:
                    xchange = -4.5
                    jacob.animate()
                    direction = "L"
                if event.key == K_SPACE:
                    for i in range(len(party)):
                        print(party[i].xp, party[i].to_next_lvl)
                if event.key == K_v:
                    if find_bullet:
                        bullet_cnt += 1
                        for i in range(len(party)):
                            party[i].procurar()
                        find_bullet = False
                        mov_log_text = "o grupo recuperou 5 balas cada"
                if event.key == K_s:
                    # (self, vida, dano_m, dano_r, cor, nome, lvl, xp, ammo, inc_mel, inc_ran, inc_vida)
                    save_game(stats=[(chr_list[stats].vida, chr_list[stats].dano_m, chr_list[stats].dano_r,
                                      stats, chr_list[stats].level, chr_list[stats].xp, chr_list[stats].ammo,
                                      chr_list[stats].inc_mel, chr_list[stats].inc_ran, chr_list[stats].inc_vida)
                                     for stats in range(len(chr_list))], party=[character.nome for character in party],
                              lvl_room=(1, salas - 1), x_pos=xpos, rest_count=rest_count, find_bullet=find_bullet,
                              score_conds=(save_cnt + 1, rest_cnt, bullet_cnt, death_cnt), fase4=fase4)
                    blit_bg = True
                if rest_count:
                    if event.key == K_c:
                        rest_cnt += 1
                        for i in range(len(party)):
                            party[i].rest()
                        rest_count = False
                        mov_log_text = "o grupo recuperou 50 de vida"
            if event.type == KEYUP:
                if event.key == K_a or K_d:
                    xchange = 0
                    jacob.stop("assets/sprites/jacob/jacob parado.png", direction)

        if xchange != 0:
            if walk_timer == 0:
                walk_timer = 28
                ch1.play(walk)

        # player movement
        if xpos >= 1230:
            xpos = 1
            trans("fase1")
        if xpos <= 0:
            xpos = 0

        xpos += xchange

        # random encounter
        if ((xpos / 10) % 1) == 0 and xpos is not 0:
            chance = random.randint(1, 30)
            if chance == 1:
                pygame.time.wait(1000)
                combate_fase1()

        # draw
        if blit_bg:
            screen.blit(bg, (0, 0))
            blit_bg = False
        else:
            screen.blit(bg, (xpos - 30, SCREEN_H - jacob.img.get_height()),
                        (xpos - 30, SCREEN_H - jacob.img.get_height(),
                         jacob.img.get_width() + 50, jacob.img.get_height()))
        screen.blit(jacob.img, (xpos, SCREEN_H - jacob.img.get_height()))
        jacob.update(0.25, direction)
        mov_log = font_menu_3.render(mov_log_text, True, (0, 0, 0))
        screen.blit(bg, (0, 0), (0, 0, mov_log.get_width(), mov_log.get_height()))
        screen.blit(mov_log, (0, 0))
        fps.tick(60)
        pygame.display.update()


def mov_f_2():
    count = 1
    bg = pygame.image.load("assets/backgrounds/nazi cyberpunk.png")
    rest_count = True
    find_bullet = True
    blit_bg = True
    enemy_list.clear()
    global xpos, salas, gerenciador, trans_state, mov_log_text, loaded_content, rest_cnt, bullet_cnt, direction, walk_timer, \
        music_is_playing
    if loaded_content:
        rest_count = rest_c
        find_bullet = find_b
        loaded_content = False
    if trans_state == "fase2":
        salas = 0
        trans_state = "standby"
    mov_log_text = ""
    xchange = 0
    salas += 1
    print(trans_state)

    while True:
        if not music_is_playing:
            start_new_thread(music, (count,))
            music_is_playing = True

        if walk_timer > 0:
            walk_timer -= 1

        if salas == 5:
            cutscene(cutscene14, "fase2", bg_cut14)
        elif salas == 9:
            cutscene(cutscene15, "boss2", bg_cut15)

        # key events
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_d:
                    xchange = +4.5
                    jacob.animate()
                    direction = "R"
                if event.key == K_a:
                    xchange = -4.5
                    jacob.animate()
                    direction = "L"
                if event.key == K_SPACE:
                    for i in range(len(party)):
                        print(party[i].xp, party[i].to_next_lvl)
                if event.key == K_v:
                    if find_bullet:
                        bullet_cnt += 1
                        for i in range(len(party)):
                            party[i].procurar()
                        find_bullet = False
                        mov_log_text = "o grupo recuperou 5 balas cada"
                if event.key == K_s:
                    # (self, vida, dano_m, dano_r, cor, nome, lvl, xp, ammo, inc_mel, inc_ran, inc_vida)
                    save_game(stats=[(chr_list[stats].vida, chr_list[stats].dano_m, chr_list[stats].dano_r,
                                      stats, chr_list[stats].level, chr_list[stats].xp, chr_list[stats].ammo,
                                      chr_list[stats].inc_mel, chr_list[stats].inc_ran, chr_list[stats].inc_vida)
                                     for stats in range(len(chr_list))], party=[character.nome for character in party],
                              lvl_room=(2, salas - 1), x_pos=xpos, rest_count=rest_count, find_bullet=find_bullet,
                              score_conds=(save_cnt + 1, rest_cnt, bullet_cnt, death_cnt))
                    blit_bg = True
                if rest_count:
                    if event.key == K_c:
                        rest_cnt += 1
                        for i in range(len(party)):
                            party[i].rest()
                        rest_count = False
                        mov_log_text = "o grupo recuperou 50 de vida"
            if event.type == KEYUP:
                if event.key == K_a or K_d:
                    xchange = 0
                    jacob.stop("assets/sprites/jacob/jacob parado.png", direction)

        if xchange != 0:
            if walk_timer == 0:
                walk_timer = 28
                ch1.play(walk)

        # player movement
        if xpos >= 1230:
            xpos = 1
            trans("fase2")
        if xpos <= 0:
            xpos = 0

        xpos += xchange

        # random encounter
        if ((xpos / 10) % 1) == 0 and xpos is not 0:
            chance = random.randint(1, 30)
            if chance == 1:
                pygame.time.wait(1000)
                combate_fase2()

        mov_log = font_menu_3.render(mov_log_text, True, (0, 0, 0))

        # draw
        if blit_bg:
            screen.blit(bg, (0, 0))
            blit_bg = False
        else:
            screen.blit(bg, (xpos - 30, SCREEN_H - jacob.img.get_height()),
                        (xpos - 30, SCREEN_H - jacob.img.get_height(),
                         jacob.img.get_width() + 50, jacob.img.get_height()))
        screen.blit(jacob.img, (xpos, SCREEN_H - jacob.img.get_height()))
        jacob.update(0.25, direction)
        screen.blit(bg, (0, 0), (0, 0, mov_log.get_width(), mov_log.get_height()))
        screen.blit(mov_log, (0, 0))
        fps.tick(60)
        pygame.display.update()


def mov_f_3():
    count = 2
    rest_count = True
    find_bullet = True
    blit_bg = True
    enemy_list.clear()
    global xpos, salas, gerenciador, trans_state, mov_log_text, loaded_content, rest_cnt, bullet_cnt, direction, walk_timer, \
        music_is_playing
    if loaded_content:
        rest_count = rest_c
        find_bullet = find_b
        loaded_content = False
    if trans_state == "fase3":
        salas = 0
        trans_state = "standby"
    mov_log_text = ""
    xchange = 0
    salas += 1
    print(trans_state)

    while True:
        if not music_is_playing:
            start_new_thread(music, (count,))
            music_is_playing = True

        if walk_timer > 0:
            walk_timer -= 1

        if salas == 5:
            cutscene(cutscene18, "fase3", bg_cut18)

        if salas == 9:
            cutscene(cutscene19, "fase3", bg_cut19)

        # key events
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_d:
                    xchange = + 4.5
                    jacob.animate()
                    direction = "R"
                if event.key == K_a:
                    xchange = - 4.5
                    jacob.animate()
                    direction = "L"
                if event.key == K_SPACE:
                    for i in range(len(party)):
                        print(party[i].xp, party[i].to_next_lvl)
                if event.key == K_v:
                    if find_bullet:
                        bullet_cnt += 1
                        for i in range(len(party)):
                            party[i].procurar()
                        find_bullet = False
                        mov_log_text = "o grupo recuperou 5 balas cada"
                if event.key == K_s:
                    # (self, vida, dano_m, dano_r, cor, nome, lvl, xp, ammo, inc_mel, inc_ran, inc_vida)
                    save_game(stats=[(chr_list[stats].vida, chr_list[stats].dano_m, chr_list[stats].dano_r,
                                      stats, chr_list[stats].level, chr_list[stats].xp, chr_list[stats].ammo,
                                      chr_list[stats].inc_mel, chr_list[stats].inc_ran, chr_list[stats].inc_vida)
                                     for stats in range(len(chr_list))], party=[character.nome for character in party],
                              lvl_room=(3, salas - 1), x_pos=xpos, rest_count=rest_count, find_bullet=find_bullet,
                              score_conds=(save_cnt + 1, rest_cnt, bullet_cnt, death_cnt))
                    blit_bg = True
                if rest_count:
                    rest_cnt += 1
                    if event.key == K_c:
                        for i in range(len(party)):
                            party[i].rest()
                        rest_count = False
                        mov_log_text = "o grupo recuperou 50 de vida"
            if event.type == KEYUP:
                if event.key == K_a or K_d:
                    xchange = 0
                    jacob.stop("assets/sprites/jacob/jacob parado.png", direction)

        if xchange != 0:
            if walk_timer == 0:
                walk_timer = 28
                ch1.play(walk)

        # player movement
        if xpos >= 1230:
            xpos = 1
            trans("fase3")
        if xpos <= 0:
            xpos = 0

        xpos += xchange

        # random encounter
        if ((xpos / 10) % 1) == 0 and xpos is not 0:
            chance = random.randint(1, 30)
            if chance == 1:
                pygame.time.wait(1000)
                combate_fase3()

        mov_log = font_menu_3.render(mov_log_text, True, (0, 0, 0))

        # draw
        if blit_bg:
            screen.blit(bg, (0, 0))
            blit_bg = False
        else:
            screen.blit(bg, (xpos - 30, SCREEN_H - jacob.img.get_height()),
                        (xpos - 30, SCREEN_H - jacob.img.get_height(),
                         jacob.img.get_width() + 50, jacob.img.get_height()))
        screen.blit(jacob.img, (xpos, SCREEN_H - jacob.img.get_height()))
        jacob.update(0.25, direction)
        screen.blit(bg, (0, 0), (0, 0, mov_log.get_width(), mov_log.get_height()))
        screen.blit(mov_log, (0, 0))
        fps.tick(60)
        pygame.display.update()


def trans(fase):
    menu_st.stop()
    screen.fill((20, 20, 20))
    texto = tfont.render("Carregando...", True, (230, 230, 230))
    texto_rect = texto.get_rect()
    texto_rect.topleft = (640 - (texto_rect.w / 2), 360 - (texto_rect.h / 2))
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        screen.blit(texto, texto_rect)
        pygame.display.update()
        ch1.play(run)
        pygame.time.wait(1500)
        if fase == "tutorial":
            mov_tutorial()
        elif fase == "fase1":
            mov_f_1()
        elif fase == "fase2":
            mov_f_2()
        elif fase == "fase3":
            mov_f_3()
        elif fase == "boss1":
            combate_boss()
        elif fase == "boss2":
            combate_boss2()
        elif fase == "boss3":
            combate_boss3()


def cutscene(cut, fase, background):
    global salas, trans_state, fase4, dialogue_timer, music_is_playing
    bg = background
    blit_bg = True
    pygame.mixer.music.stop()
    while True:
        fps.tick(60)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        if blit_bg:
            screen.blit(bg, (0, 0))
            blit_bg = False
        else:
            screen.blit(bg, (0, 0), (0, 0, SCREEN_W, SCREEN_H * 0.3))
        gerenciador.start_cutscene(cut)
        gerenciador.draw()
        gerenciador.update()
        pygame.display.update()

        if cut == cutscene1:
            if cutscene1.cur_step == 7:
                bg = bg_cut1_2
                screen.blit(bg, (0, 0))
            elif cutscene1.cur_step == 8:
                bg = bg_cut1_3
                screen.blit(bg, (0, 0))

        elif cut == cutscene7:
            if cutscene7.cur_step == 21:
                bg = bg_cut7_2
                screen.blit(bg, (0, 0))

        elif cut == cutscene8:
            if cutscene8.cur_step == 2:
                bg = bg_cut8_2
                screen.blit(bg, (0, 0))

        elif cut == cutscene13:
            if cutscene13.cur_step == 10:
                bg = bg_cut13_2
                screen.blit(bg, (0, 0))

        if not (int(cut.dialogue_position) < len(cut.dialogue)):
            gerenciador.sound.stop()

        if not gerenciador.cutscene_running:
            if cut == cutscene4:
                combate_tutorial()

            elif cut == cutscene5:
                cutscene(cutscene6, "fase1", bg_cut6)

            elif cut == cutscene6:
                cutscene(cutscene7, "fase1", bg_cut7)

            elif cut == cutscene7:
                cutscene(cutscene8, "fase1", bg_cut8)

            elif cut == cutscene8:
                trans_state = "fase1"
                jacob.vida = jacob.vida_total
                pygame.mixer.stop()
                mov_f_1()

            elif cut == cutscene9:
                party.append(kazi)
                start_new_thread(music, (0,))
                combate_fase1()

            elif cut == cutscene11:
                music_is_playing = False
                combate_boss()

            elif cut == cutscene12:
                cutscene(cutscene13, "fase2", bg_cut13)

            elif cut == cutscene13:
                trans_state = "fase2"
                party.pop(1)
                party.append(kenji)
                for i in range(len(party)):
                    party[i].vida = party[i].vida_total
                    party[i].ammo = 10
                pygame.mixer.stop()
                music_is_playing = False
                mov_f_2()

            elif cut == cutscene14:
                party.append(barbara)
                party.append(kazi)
                kazi.vida = kazi.vida_total
                kazi.img = pygame.image.load("assets/sprites/peter/davidcombate.png")
                music_is_playing = False
                trans(fase)

            elif cut == cutscene15:
                music_is_playing = False
                combate_boss2()

            elif cut == cutscene16:
                cutscene(cutscene17, "fase3", bg_cut17)

            elif cut == cutscene17:
                trans_state = "fase3"
                for i in range(len(party)):
                    party[i].vida = party[i].vida_total
                    party[i].ammo = 10
                pygame.mixer.stop()
                music_is_playing = False
                mov_f_3()

            elif cut == cutscene19:
                music_is_playing = False
                combate_boss3()

            elif cut == cutscene20:
                music_is_playing = False
                combate_boss3()

            elif cut == cutscene21:
                cutscene(cutscene22, "fase1", bg_cut22)

            elif cut == cutscene22:
                fase4 = True
                party.remove(kenji)
                party.remove(barbara)
                party.remove(kazi)
                trans_state = "fase1"
                for i in range(len(party)):
                    party[i].vida = party[i].vida_total
                    party[i].ammo = 10
                pygame.mixer.stop()
                music_is_playing = False
                mov_f_1()

            elif cut == cutscene24:
                screen.fill((0, 0, 0))
                pygame.display.update()
                # tocar som da arma
                submmit_score(save_cnt, rest_cnt, bullet_cnt, death_cnt)

            else:
                music_is_playing = False
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
    global salas, xpos, rest_c, find_b, loaded_content, fase4, save_cnt, rest_cnt, bullet_cnt, death_cnt
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
                        loaded_data = load_file()
                        if loaded_data is not None:
                            for data in loaded_data['stats']:
                                if data[3] == 0:
                                    # (vida, dano_m, dano_r, cor, nome, lvl, xp, ammo, inc_mel, inc_ran, inc_vida)
                                    jacob.vida = data[0]
                                    jacob.dano_m = data[1]
                                    jacob.dano_r = data[2]
                                    jacob.nome = "jacob"
                                    jacob.level = data[4]
                                    jacob.xp = data[5]
                                    jacob.ammo = data[6]
                                    jacob.inc_mel = data[7]
                                    jacob.inc_ran = data[8]
                                    jacob.inc_vida = data[9]
                                    jacob.load_stats()
                                    party[0] = jacob
                                elif data[3] == 1:
                                    kazi.vida = data[0]
                                    kazi.dano_m = data[1]
                                    kazi.dano_r = data[2]
                                    kazi.nome = "kazi_past"
                                    kazi.level = data[4]
                                    kazi.xp = data[5]
                                    kazi.ammo = data[6]
                                    kazi.inc_mel = data[7]
                                    kazi.inc_ran = data[8]
                                    kazi.inc_vida = data[9]
                                    kazi.load_stats()
                                elif data[3] == 2:
                                    kenji.vida = data[0]
                                    kenji.dano_m = data[1]
                                    kenji.dano_r = data[2]
                                    kenji.nome = "kenji"
                                    kenji.level = data[4]
                                    kenji.xp = data[5]
                                    kenji.ammo = data[6]
                                    kenji.inc_mel = data[7]
                                    kenji.inc_ran = data[8]
                                    kenji.inc_vida = data[9]
                                    kenji.load_stats()
                                else:
                                    barbara.vida = data[0]
                                    barbara.dano_m = data[1]
                                    barbara.dano_r = data[2]
                                    barbara.nome = "barbara"
                                    barbara.level = data[4]
                                    barbara.xp = data[5]
                                    barbara.ammo = data[6]
                                    barbara.inc_mel = data[7]
                                    barbara.inc_ran = data[8]
                                    barbara.inc_vida = data[9]
                                    barbara.load_stats()
                            for character in loaded_data['party'][1:]:
                                if character == "kazi":
                                    party.append(kazi)
                                elif character == "kenji":
                                    party.append(kenji)
                                else:
                                    party.append(barbara)
                            if loaded_data['lvl_room'][0] == 'fase2' or loaded_data['lvl_room'][0] == 'fase3':
                                kazi.img = pygame.image.load("assets/sprites/peter/davidcombate.png")
                            salas = loaded_data['lvl_room'][1]
                            xpos = loaded_data['x_pos']
                            rest_c = loaded_data['rest_counter']
                            find_b = loaded_data['find_bullet']
                            loaded_content = True
                            save_cnt, rest_cnt, bullet_cnt, death_cnt = loaded_data['score_conds']
                            if len(loaded_data) > 7:
                                fase4 = loaded_data['fase4']
                            trans(loaded_data['lvl_room'][0])

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


def save_game(**dados):
    """
    Inicializa a tela de salvamento de progresso.

    Parâmetros a serem passados:
    stats -> status dos personagens (exemplo: vida, balas, etc)
    party -> personagens da party
    lvl_room -> nível e sala
    x_pos -> posição x do jogador
    rest_count -> variável local rest_count
    find_bullet -> variável local find_bullet
    score_conds -> condições de pontuação
    fase4 -> variável global fase4
    """

    save_text = font_menu_2.render('Escolha um slot:', True, (255, 255, 255))
    X = font_menu_2.render("X", True, (255, 255, 255))
    slots = (font_menu_2.render('Slot 1', True, (255, 255, 255)), font_menu_2.render('Slot 2', True, (255, 255, 255)),
             font_menu_2.render('Slot 3', True, (255, 255, 255)))

    global save_cnt
    save_screen = True
    slot_select = 0

    while save_screen:
        screen.fill((0, 0, 0))

        # slots
        screen.blit(save_text, (screen.get_width() // 2 - save_text.get_rect().width // 2, 100))
        for pos, slt in enumerate(slots):
            screen.blit(slt, (screen.get_width() // 2 - slt.get_rect().width // 2, 300 + 80 * pos))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    save_screen = False
                if event.key == pygame.K_s:
                    if slot_select < 2:
                        slot_select += 1
                    else:
                        slot_select = 0
                if event.key == pygame.K_w:
                    if slot_select > 0:
                        slot_select -= 1
                    else:
                        slot_select = 2
                if event.key == pygame.K_RETURN:

                    if dados['lvl_room'][0] != 0:
                        save_cnt += 1
                    save = open(f'save0{slot_select}.txt', 'w')
                    for data in dados:
                        save.write(str(dados[f'{data}']) + '\n')
                    save.close()
                    save_screen = False

        # X mark
        screen.blit(X, (screen.get_width() // 2 - slots[0].get_rect().width // 2
                        - X.get_rect().width, 300 + 80 * slot_select))

        pygame.display.update()


def load_file():
    """
    Inicializa a tela de load file do jogo.
    Retorna uma lista com todas as informações contidas no arquivo txt escolhido.
    Cada linha do arquivo é uma string da lista.
    """

    load_text = font_menu_2.render('Escolha um slot para carregar:', True, (255, 255, 255))
    X = font_menu_2.render("X", True, (255, 255, 255))
    slots = (font_menu_2.render('Slot 1', True, (255, 255, 255)), font_menu_2.render('Slot 2', True, (255, 255, 255)),
             font_menu_2.render('Slot 3', True, (255, 255, 255)))
    empty_slot = font_menu_2.render(' -> Vazio', True, (255, 255, 255))

    load_screen = True
    slot_select = 0
    show_text = False

    info = list()

    while load_screen:
        screen.fill((0, 0, 0))

        # slots
        screen.blit(load_text, (screen.get_width() // 2 - load_text.get_rect().width // 2, 100))
        for pos, slt in enumerate(slots):
            screen.blit(slt, (screen.get_width() // 2 - slt.get_rect().width // 2, 300 + 80 * pos))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return None
                if event.key == pygame.K_s:
                    select.play()
                    if slot_select < 2:
                        slot_select += 1
                    else:
                        slot_select = 0
                    if show_text:
                        show_text = False
                if event.key == pygame.K_w:
                    select.play()
                    if slot_select > 0:
                        slot_select -= 1
                    else:
                        slot_select = 2
                    if show_text:
                        show_text = False
                if event.key == pygame.K_RETURN:
                    enter.play()
                    try:
                        save = open(f'save0{slot_select}.txt', 'r')
                    except FileNotFoundError:
                        show_text = True
                    else:
                        for linha in save:
                            info.append(linha[:-1])
                        return string_converter(info)

        # X mark
        screen.blit(X, (screen.get_width() // 2 - slots[0].get_rect().width // 2
                        - X.get_rect().width, 300 + 80 * slot_select))
        if show_text:
            screen.blit(empty_slot, (screen.get_width() // 2 + slots[0].get_rect().width // 2, 300 + 80 * slot_select))

        pygame.display.update()


def string_converter(info):
    """
    Converte todos os dados de string coletados ao carregar um arquivo de save.
    Retorna um dicionário com os dados convertidos.

    Parâmetro a ser passado:
    info -> lista com os dados carregados do arquivo txt
    """

    converted_data = dict()

    # Converte a primeira linha do arquivo txt
    data = info[0][1:-1]
    stats = list()
    avaiable_tuples = True
    start_point = 0
    end_point = 0
    while avaiable_tuples:
        start = data.find('(', start_point)
        start_point = start + 1

        fim = data.find(')', end_point)
        end_point = fim + 1

        if start == -1:
            avaiable_tuples = False
        else:
            valores = data[start + 1:fim]
            stats.append(list(map(int, valores.split(', '))))
    converted_data['stats'] = stats

    # Converte a segunda linha do arquivo txt
    data = info[1][1:-1]
    party_chrs = list(data.split(', '))
    for name in range(len(party_chrs)):
        party_chrs[name] = party_chrs[name][1:-1]
    converted_data['party'] = party_chrs

    # Converte a terceira linha do arquivo txt
    data = info[2][1:-1]
    lvl_room = list(map(int, data.split(', ')))
    if lvl_room[0] == 0:
        lvl_room[0] = 'tutorial'
    elif lvl_room[0] == 1:
        lvl_room[0] = 'fase1'
    elif lvl_room[0] == 2:
        lvl_room[0] = 'fase2'
    elif lvl_room[0] == 3:
        lvl_room[0] = 'fase3'
    lvl_room = tuple(lvl_room)
    converted_data['lvl_room'] = lvl_room

    # Converte a quarta linha do arquivo txt
    data = info[3]
    x_position = int(float(data))
    converted_data['x_pos'] = x_position

    # Converte a quinta linha do arquivo txt
    data = info[4]
    if data == 'True':
        rest_c = True
    else:
        rest_c = False
    converted_data['rest_counter'] = rest_c

    # Converte a sexta linha do arquivo txt
    data = info[5]
    if data == 'True':
        find_b = True
    else:
        find_b = False
    converted_data['find_bullet'] = find_b

    # Converte a sétima linha do arquivo txt
    data = info[6][1:-1]
    scr_conds = list(map(int, data.split(', ')))
    converted_data['score_conds'] = scr_conds

    # Converte a oitava linha do arquivo txt (se houver)
    if len(info) > 7:
        data = info[7]
        if data == 'True':
            fase_quatro = True
        else:
            fase_quatro = False
        converted_data['fase4'] = fase_quatro

    return converted_data


scoreboard = list()


def submmit_score(sv_c, rst_c, blt_c, dth_c):
    res = 5000
    if sv_c > 4:
        res -= 500 * (sv_c - 4)
    if rst_c > 25:
        res -= 200 * (rst_c - 25)
    if blt_c > 20:
        res -= 180 * (rst_c - 20)
    res -= 800 * dth_c
    if res < 0:
        res = 0

    if res >= 4500:
        rank = 'SS'
    elif res >= 3500:
        rank = 'S'
    elif res >= 2500:
        rank = 'A'
    elif res >= 1500:
        rank = 'B'
    else:
        rank = 'C'

    text1 = font_menu_2.render('Digite suas iniciais: ', True, (255, 255, 255))
    text2 = font_menu_2.render(f'Quantidades de saves: {sv_c}x', True, (255, 255, 255))
    text3 = font_menu_2.render(f'Recuperações de vida: {rest_cnt}x', True, (255, 255, 255))
    text4 = font_menu_2.render(f'Recargas de munição: {blt_c}x', True, (255, 255, 255))
    text5 = font_menu_2.render(f'Mortes em batalha: {dth_c}x', True, (255, 255, 255))

    user_input = ''
    running = True
    while running:
        if len(user_input) < 3:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        user_input += 'Q'
                    if event.key == pygame.K_w:
                        user_input += 'W'
                    if event.key == pygame.K_e:
                        user_input += 'E'
                    if event.key == pygame.K_r:
                        user_input += 'R'
                    if event.key == pygame.K_t:
                        user_input += 'T'
                    if event.key == pygame.K_u:
                        user_input += 'U'
                    if event.key == pygame.K_i:
                        user_input += 'I'
                    if event.key == pygame.K_o:
                        user_input += 'O'
                    if event.key == pygame.K_p:
                        user_input += 'P'
                    if event.key == pygame.K_a:
                        user_input += 'A'
                    if event.key == pygame.K_s:
                        user_input += 'S'
                    if event.key == pygame.K_d:
                        user_input += 'D'
                    if event.key == pygame.K_f:
                        user_input += 'F'
                    if event.key == pygame.K_g:
                        user_input += 'G'
                    if event.key == pygame.K_h:
                        user_input += 'H'
                    if event.key == pygame.K_j:
                        user_input += 'J'
                    if event.key == pygame.K_k:
                        user_input += 'K'
                    if event.key == pygame.K_l:
                        user_input += 'L'
                    if event.key == pygame.K_z:
                        user_input += 'Z'
                    if event.key == pygame.K_x:
                        user_input += 'X'
                    if event.key == pygame.K_c:
                        user_input += 'C'
                    if event.key == pygame.K_v:
                        user_input += 'V'
                    if event.key == pygame.K_b:
                        user_input += 'B'
                    if event.key == pygame.K_n:
                        user_input += 'N'
                    if event.key == pygame.K_m:
                        user_input += 'M'
        else:
            running = False

        screen.fill((0, 0, 0))
        screen.blit(text1, (screen.get_width() // 2 - text1.get_width() // 2, 100))
        screen.blit(text2, (screen.get_width() // 2 - text2.get_width() // 2, 300))
        screen.blit(text3, (screen.get_width() // 2 - text3.get_width() // 2, 380))
        screen.blit(text4, (screen.get_width() // 2 - text4.get_width() // 2, 460))
        screen.blit(text5, (screen.get_width() // 2 - text5.get_width() // 2, 540))
        user_name = font_menu_2.render(user_input, True, (255, 255, 255))
        screen.blit(user_name, (screen.get_width() // 2 - user_name.get_width() // 2, 200))
        pygame.display.update()

    return scores_screen(user_input, res, rank)


def scores_screen(name, result, rank):
    text1 = font_menu_2.render('LEADERBOARD', True, (255, 255, 255))
    uploading = True

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        if uploading:
            start_new_thread(upload_data, ((name, result, rank),))
            uploading = False

        screen.fill((0, 0, 0))
        screen.blit(text1, (screen.get_width() // 2 - text1.get_width() // 2, 20))

        y = 0
        for info in scoreboard:
            screen.blit(info, (screen.get_width() // 2 - info.get_width() // 2, 100 + 80 * y))
            y += 1

        pygame.display.update()


def upload_data(scr):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = '127.0.0.1'
    port = 55000

    try:
        client_socket.connect((host, port))
    except socket.error as e:
        print(str(e))

    client_socket.sendall(str(scr).encode('ascii'))
    while True:
        try:
            data = client_socket.recv(1024)
        except socket.error as e:
            print(str(e))
            break
        else:
            info = data.decode('ascii')

            scores_list = list()
            scr_info = info[1:-1]
            start_point = 0
            end_point = 0
            avaiable_info = True
            while avaiable_info:
                start = scr_info.find('(', start_point)
                start_point = start + 1
                if start == -1:
                    avaiable_info = False
                if avaiable_info:
                    end = scr_info.find(')', end_point)
                    end_point = end + 1
                    converted_info = scr_info[start + 1:end].split(', ')
                    converted_info[0] = converted_info[0][1:-1]
                    converted_info[2] = converted_info[2][1:-1]
                    scores_list.append(converted_info)
            scores_list.sort(key=lambda scr_data: int(scr_data[1]), reverse=True)

            pos = 1
            scoreboard.clear()
            for score in range(len(scores_list)):
                text = f'{pos}. {scores_list[score][0]}: {scores_list[score][1]} pontos ' \
                       f'(Rank {scores_list[score][2]})'
                scoreboard.append(font_menu_2.render(text, True, (255, 255, 255)))
                pos += 1
    client_socket.close()


menu_start()