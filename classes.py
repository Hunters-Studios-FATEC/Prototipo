import pygame
import random


class Allies:
    def __init__(self, vida, dano_m, dano_r, cor, nome):
        self.vida = vida
        self.nome = nome
        self.dano_m = dano_m
        self.dano_r = dano_r
        self.img = pygame.Surface((50, 50))
        self.img.fill(cor)
        self.dmg_red = 1

    def attack(self, enemy):
        enemy.vida -= self.dano_m * enemy.dmg_red_e

    def skill(self, enemy):
        enemy.vida -= self.dano_r * enemy.dmg_red_e


jacob = Allies(200, 20, 30, (255, 0, 0), "jacob")
barbara = Allies(200, 15, 35, (0, 0, 255), "barbara")
kazi = Allies(200, 30, 10, (0, 255, 0), "kazi")
kenji = Allies(200, 25, 25, (255, 150, 0), "kenji")
party = [jacob, kazi, kenji, barbara]


class Enemy:
    def __init__(self, vida, dano, cor, nome):
        self.vida = vida
        self.vida_total = vida
        self.dano_recebido = 1
        self.barra = pygame.Surface((100 * self.dano_recebido, 10))
        self.barra.fill((255, 0, 0))
        self.dano = dano
        self.img = pygame.Surface((50, 50))
        self.img.fill(cor)
        self.dmg_red_e = 1
        self.nome = nome

    def ataque(self, player):
        player.vida -= self.dano * player.dmg_red

    def enemy_def(self):
        self.dmg_red_e = 0.5

    def life_update(self):
        self.dano_recebido = self.vida / self.vida_total
        self.barra = pygame.Surface((abs(100 * self.dano_recebido), 10))
        self.barra.fill((255, 0, 0))


def enemy_gen():
    vida = [100, 150, 200]
    dano = [10, 15, 20]
    cor = [(0, 0, 0), (50, 50, 50), (100, 100, 100)]
    nomes = ["nazi_melee", "nazi_atirador", "nazi_tank"]
    enemy_dict = {}
    for i in range(random.randint(1, 4)):
        enemy_dict["enemy{0}".format(i)] = Enemy(random.choice(vida), random.choice(dano), random.choice(cor),
                                                 random.choice(nomes))
    for enemy in range(len(enemy_dict)):
        enemy_list.append(enemy_dict["enemy{0}".format(enemy)])





enemy_list = []
