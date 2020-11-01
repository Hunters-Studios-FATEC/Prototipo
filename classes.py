import pygame
import random

# Costante de cor
VERMELHO = (255, 0, 0)
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
VIOLETA = (138, 43, 226)
FUCHSIA = (255, 0, 255)


class Allies:
    def __init__(self, vida, dano_m, dano_r, cor, nome, lvl, xp, inc_mel, inc_ran, inc_vida):
        self.vida = vida
        self.vida_total = vida
        self.dano_recebido = 1
        self.barra = pygame.Surface((100 * self.dano_recebido, 10))
        self.barra.fill((255, 0, 0))
        self.ammo = 20
        self.level = lvl
        self.nome = nome
        self.dano_m = dano_m
        self.dano_r = dano_r
        self.img = pygame.Surface((50, 50))
        self.img.fill(cor)
        self.dmg_red = 1

        self.xp = xp
        self.to_next_lvl = 25
        self.inc_mel = inc_mel
        self.inc_ran = inc_ran
        self.inc_vida = inc_vida

    def attack(self, enemy):
        enemy.vida -= self.dano_m * enemy.dmg_red_e

    def skill(self, enemy):
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
        self.to_next_lvl = round(self.to_next_lvl * 1.5) * (self.level - 1)


jacob = Allies(200, 20, 30, (255, 0, 0), "jacob", 1, 0, 4, 2, 50)
barbara = Allies(200, 15, 35, (0, 0, 255), "barbara", 1, 0, 2, 4, 30)
kazi = Allies(200, 20, 30, (0, 255, 0), "kazi", 1, 0, 3, 5, 30)
kenji = Allies(200, 25, 25, (255, 150, 0), "kenji", 1, 0, 5, 2, 40)
party = [jacob, kazi, kenji, barbara]


class Enemy:
    def __init__(self, vida, dano, cor, nome, xp_drop):
        self.multiplier = jacob.level
        self.vida = vida + (50 * self.multiplier)
        self.vida_total = vida + (50 * self.multiplier)
        self.dano_recebido = 1
        self.barra = pygame.Surface((100 * self.dano_recebido, 10))
        self.barra.fill((255, 0, 0))
        self.dano = dano + (2 * jacob.level)
        self.img = pygame.Surface((50, 50))
        self.img.fill(cor)
        self.dmg_red_e = 1
        self.nome = nome
        self.xp_drop = xp_drop

    def ataque(self, player):
        player.vida -= self.dano * player.dmg_red

    def enemy_def(self):
        self.dmg_red_e = 0.5

    def life_update(self):
        self.dano_recebido = self.vida / self.vida_total
        self.barra = pygame.Surface((abs(100 * self.dano_recebido), 10))
        self.barra.fill((255, 0, 0))


class Boss:
    def __init__(self, vida, dano, cor, nome, xpdrop):
        self.vida = vida
        self.vida_total = vida
        self.dano_recebido = 0.75
        self.barra = pygame.Surface((100 * self.dano_recebido, 10))
        self.barra.fill(VERMELHO)
        self.dano = dano
        self.img = pygame.Surface((50, 50))
        self.img.fill(cor)
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


hitler = Boss(400, 30, PRETO, "Hitler", 0)
hitler2 = Boss(410, 32, PRETO, "TRUE HITLER: INACIO", 500)

antonio = Boss(500, 10, VIOLETA, "Mussolinius", 0)
antonio2 = Boss(600, 15, VIOLETA, "Enraged Mussolinius", 1000)
joseph = Boss(400, 25, VERMELHO, "Joseph Ducai Zhe", 0)
joseph2 = Boss(500, 25, VERMELHO, "Mecha Joseph", 2000)
chronos = Boss(550, 30, FUCHSIA, "Cronos", 0)
chronos2 = Boss(600, 30, FUCHSIA, "Cronos", 9999)


def enemy_gen(vidas, danos):
    vida = vidas
    dano = danos
    cor = [(0, 0, 0), (50, 50, 50), (100, 100, 100)]
    nomes = ["nazi caréca", "nazi bigodudo", "nazi manco"]

    enemy_dict = {}
    for i in range(random.randint(1, 4)):
        enemy_dict["enemy{0}".format(i)] = Enemy(random.choice(vida), random.choice(dano), random.choice(cor),
                                                 random.choice(nomes), random.randint(6, 10))
    for enemy in range(len(enemy_dict)):
        enemy_list.append(enemy_dict["enemy{0}".format(enemy)])


enemy_list = []
