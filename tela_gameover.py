import pygame
import sys
from menu import menu_start

pygame.init()

WIDTH = 1280
HEIGHT = 720

screen = pygame.display.set_mode((WIDTH, HEIGHT))

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
