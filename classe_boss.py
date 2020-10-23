import pygame

VERMELHO = (255, 0, 0)
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
VIOLETA = (138, 43, 226)
FUCHSIA = (255, 0, 255)


class Boss:
    def __init__(self, vida, dano, cor, nome):
        self.vida = vida
        self.vida_total = vida
        self.dano_recebido = 0.75
        self.barra = pygame.Surface((100 * self.dano_recebido, 10))
        self.barra.fill(VERMELHO)
        self.dano = dano
        self.img = pygame.Surface((100, 100))
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
        self.barra.fill(VERMELHO)


hitler = Boss(350, 20, PRETO, "Hitler")
hitler2 = Boss(350, 30, PRETO, "Hitler")
antonio = Boss(500, 10, VIOLETA, "Mussolinius")
antonio2 = Boss(600, 15, VIOLETA, "Enraged Mussolinius")
joseph = Boss(400, 25, VERMELHO, "Joseph Ducai Zhe")
joseph2 = Boss(500, 25, VERMELHO, "Mecha Joseph")
chronos = Boss(550, 30, FUCHSIA, "Cronos")
chronos2 = Boss(600, 30, FUCHSIA, "Cronos")
