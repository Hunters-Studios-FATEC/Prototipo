import pygame
import random

pygame.mixer.init()

# Costante de cor
VERMELHO = (255, 0, 0)
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
VIOLETA = (138, 43, 226)
FUCHSIA = (255, 0, 255)

animations_jacobL = []
animations_jacobR = [pygame.image.load('assets/sprites/jacob/jacobandando0001.png'),
                   pygame.image.load('assets/sprites/jacob/jacobandando0002.png'),
                   pygame.image.load('assets/sprites/jacob/jacobandando0003.png'),
                   pygame.image.load('assets/sprites/jacob/jacobandando0004.png'),
                   pygame.image.load('assets/sprites/jacob/jacobandando0005.png'),
                   pygame.image.load('assets/sprites/jacob/jacobandando0006.png'),
                   pygame.image.load('assets/sprites/jacob/jacobandando0007.png'),
                   pygame.image.load('assets/sprites/jacob/jacobandando0008.png'),
                   pygame.image.load('assets/sprites/jacob/jacobandando0009.png'),
                   pygame.image.load('assets/sprites/jacob/jacobandando0010.png'),
                   pygame.image.load('assets/sprites/jacob/jacobandando0011.png'),
                   pygame.image.load('assets/sprites/jacob/jacobandando0012.png'),
                   pygame.image.load('assets/sprites/jacob/jacobandando0013.png'),
                   pygame.image.load('assets/sprites/jacob/jacobandando0014.png')]
for i in animations_jacobR:
    animations_jacobL.append(pygame.transform.flip(i, True, False))

class Allies:
    def __init__(self, vida, dano_m, dano_r, img, nome, lvl, xp, ammo, inc_mel, inc_ran, inc_vida, spritesR, spritesL):
        self.vida = vida
        self.vida_total = vida
        self.dano_recebido = 1
        self.barra = pygame.Surface((100 * self.dano_recebido, 10))
        self.barra.fill((255, 0, 0))
        self.ammo = ammo
        self.level = lvl
        self.nome = nome
        self.dano_m = dano_m
        self.dano_r = dano_r
        self.idle = pygame.image.load(img)
        self.img = pygame.image.load(img)
        self.dmg_red = 1

        self.xp = xp
        self.to_next_lvl = 25
        self.inc_mel = inc_mel
        self.inc_ran = inc_ran
        self.inc_vida = inc_vida

        self.is_animating = False
        self.current_sprite = 0
        self.spritesR = spritesR
        self.spritesL = spritesL

        self.atk_sound = pygame.mixer.Sound("assets/audio/Combate/swish_2.wav")
        self.gun_sound = pygame.mixer.Sound("assets/audio/Combate/pistol.wav")
        self.hit2 = pygame.mixer.Sound("assets/audio/Combate/hit2.wav")

    def attack(self, enemy):
        self.atk_sound.play()
        self.hit2.play()
        enemy.vida -= self.dano_m * enemy.dmg_red_e

    def skill(self, enemy):
        self.gun_sound.play()
        self.hit2.play()
        enemy.vida -= self.dano_r * enemy.dmg_red_e
        self.ammo -= 1

    def lvl_up(self, soma):
        self.xp += soma

        if self.xp >= self.to_next_lvl:
            self.level += 1
            self.xp = self.xp - self.to_next_lvl
            self.to_next_lvl = round(self.to_next_lvl * 1.5)

            self.vida_total += self.inc_vida
            self.dano_m += self.inc_mel
            self.dano_r += self.inc_ran

            print("-------------LEVEL UP!-------------")
            print("{} foi para o nivel {}".format(self.nome, self.level))
            print("ataque corpo a corpo {}".format(self.dano_m))
            print("ataque raged {}".format(self.dano_r))
            print("vida {}".format(self.vida_total))
            print("-----------------------------------")

    def life_update(self):
        self.dano_recebido = self.vida / self.vida_total
        self.barra = pygame.Surface((abs(100 * self.dano_recebido), 10))
        self.barra.fill((255, 0, 0))

    def rest(self):
        self.vida += 50
        if self.vida > self.vida_total:
            self.vida = self.vida_total

    def procurar(self):
        self.ammo += 5

    def load_stats(self):
        self.vida_total = 200 + (self.level - 1) * self.inc_vida
        self.to_next_lvl = round(self.to_next_lvl * 1.5 ** (self.level - 1))

    def animate(self):
        self.is_animating = True

    def stop(self, img, direct):
        self.idleL = pygame.transform.flip(self.idle, True, False)
        self.is_animating = False
        if direct == "R":
            self.img = self.idle
        else:
            self.img = self.idleL

    def update(self, speed, direct):

        if self.is_animating:
            self.current_sprite += speed

            if direct == "R":
                if self.current_sprite >= len(self.spritesR):
                    self.current_sprite = 0

                self.img = self.spritesR[int(self.current_sprite)]
            else:
                if self.current_sprite >= len(self.spritesL):
                    self.current_sprite = 0

                self.img = self.spritesL[int(self.current_sprite)]


jacob = Allies(200, 50, 30, "assets/sprites/jacob/jacob parado.png", "jacob",
               1, 0, 20, 4, 2, 50, animations_jacobR, animations_jacobL)
barbara = Allies(200, 15, 35, "assets/sprites/gotica/barbara gótica.png", "barbara",
                 1, 0, 20, 2, 4, 30, animations_jacobR, animations_jacobL)
kazi = Allies(200, 20, 30, "assets/sprites/peter/peter.png", "kazi", 1, 0, 20,
              3, 5, 30, animations_jacobR, animations_jacobL)
kenji = Allies(200, 25, 25, "assets/sprites/kenji/kenji futuro.png", "kenji", 1, 0, 20,
               5, 2, 40, animations_jacobR, animations_jacobL)
party = [jacob, kazi, kenji, barbara]


class Enemy:
    def __init__(self, vida, dano, img, nome, xp_drop):
        self.multiplier = jacob.level
        self.vida = vida + (50 * self.multiplier)
        self.vida_total = vida + (50 * self.multiplier)
        self.dano_recebido = 1
        self.barra = pygame.Surface((100 * self.dano_recebido, 10))
        self.barra.fill((255, 0, 0))
        self.dano = dano + (2 * jacob.level)
        self.img = pygame.image.load(img)
        self.dmg_red_e = 1
        self.nome = nome
        self.xp_drop = xp_drop

        self.gun_sound = pygame.mixer.Sound("assets/audio/Combate/pistol.wav")


    def ataque(self, player):
        self.gun_sound.play()
        player.vida -= self.dano * player.dmg_red

    def enemy_def(self):
        self.dmg_red_e = 0.5

    def life_update(self):
        self.dano_recebido = self.vida / self.vida_total
        self.barra = pygame.Surface((abs(100 * self.dano_recebido), 10))
        self.barra.fill((255, 0, 0))


class Boss:
    def __init__(self, vida, dano, img, nome, xpdrop):
        self.vida = vida
        self.vida_total = vida
        self.dano_recebido = 0.75
        self.barra = pygame.Surface((100 * self.dano_recebido, 10))
        self.barra.fill(VERMELHO)
        self.dano = dano
        self.img = pygame.image.load(img)
        self.dmg_red_e = 1
        self.nome = nome
        self.xpdrop = xpdrop

    def ataque(self, player):
        player.vida -= self.dano * player.dmg_red

    def enemy_def(self):
        self.dmg_red_e = 0.5

    def life_update(self):
        self.dano_recebido = self.vida / self.vida_total
        self.barra = pygame.Surface((abs(100 * self.dano_recebido), 10))
        self.barra.fill(VERMELHO)


hitler = Boss(400, 30, 'assets/sprites/antonius/antonius.png', "Hitler", 0)
hitler2 = Boss(450, 40, 'assets/sprites/antonius/antonius.png', "TRUE HITLER: INACIO", 500)
antonio = Boss(500, 10, 'assets/sprites/antonius/antonius.png', "Mussolinius", 0)
chronos = Boss(550, 30, 'assets/sprites/antonius/antonius.png', "Cronos", 0)
chronos2 = Boss(600, 30, 'assets/sprites/antonius/antonius.png', "Cronos", 9999)


def enemy_gen(vidas, danos):
    vida = vidas
    dano = danos
    cor = ['assets/sprites/hitler/hitler.png']
    nomes = ["nazi caréca", "nazi bigodudo", "nazi manco"]

    enemy_dict = {}
    for i in range(random.randint(1, 4)):
        enemy_dict["enemy{0}".format(i)] = Enemy(random.choice(vida), random.choice(dano), random.choice(cor),
                                                 random.choice(nomes), random.randint(6, 10))
    for enemy in range(len(enemy_dict)):
        enemy_list.append(enemy_dict["enemy{0}".format(enemy)])


enemy_list = []
