import pygame as pg

# Método para desenhar o texto. Chamado no manager.

def draw_text(screen, text, size, color, x, y):
    font = pg.font.SysFont(None, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.topleft = (x, y)
    screen.blit(text_surface, text_rect)


class Cutscene:

    def __init__(self, cutscene_metadata):
        # Armazena o metadado json na classe
        self.cutscene = cutscene_metadata

        self.timer = pg.time.get_ticks()
        self.name = self.cutscene['name']

        # passos (steps) de cada cutscene. Cada passo é uma fala. Inicia no 0.
        self.final_step = self.cutscene['final_step']
        self.cur_step = 0

        # Dialogo
        self.dialogue = ''
        self.text_speed = 0
        self.dialogue_position = 0

        # parametros da imagem
        self.size = None
        self.rgb_color = ()
        self.pos_x = None
        self.pos_y = None

        self.cutscene_running = True

        # Coloca o step atual de fala na cutscene, iniciando no 0
        self.__set_dialogue(self.cur_step)

    def __set_dialogue(self, cur_step):
        # Extraindo o dado do metadado e armazenando na memoria
        cur_event = self.cutscene['events'][cur_step]
        self.dialogue = cur_event['text']
        self.text_speed = cur_event['speed']

        self.size = cur_event['size']
        # Necessário importar como tuple, pois no json é uma lista
        self.rgb_color = tuple(cur_event['rgb_color'])
        self.pos_x = cur_event['pos_x']
        self.pos_y = cur_event['pos_y']

        # coloca a posição de volta no 0 para o proximo dialogo
        self.dialogue_position = 0

    def update_metadata(self):
        pressed = pg.key.get_pressed()
        space = pressed[pg.K_SPACE]

        # Se dialogue_position é maior que o lenght da string do dialogo, a cutscene
        # acabou de exibir todos os caracteres.
        # Serve para mostrar os caracteres um de cada vez, percorrendo a len da string.
        # Velocidade definida no json.
        if int(self.dialogue_position) < len(self.dialogue):
            self.dialogue_position += self.text_speed
        else:
            if space:
                # Se estiver no final_step, acaba a cutscene.
                # Se não, incrementa + 1 no passo, e mostra a próximo step/item do json e proxima fala.
                if self.cur_step == self.final_step:
                    self.cutscene_running = False
                else:
                    self.cur_step += 1
                    self.__set_dialogue(self.cur_step)

        return self.cutscene_running

class CutSceneManager:

    def __init__(self, screen):
        self.cutscenes_complete = []
        self.cutscene = None
        self.cutscene_running = False

        # Variáveis de desenho
        self.screen = screen
        self.window_size = 0

        # Condição para mostrar o diálogo só quando a caixa desenhar
        self.is_dialogue_screen_draw = False

        self.surf = pg.Surface((int(self.screen.get_width()), int(self.window_size)))
        self.timer = 0
        self.sound = pg.mixer.Sound("assets/audio/Cutscenes/dialogue.wav")
        self.sound.set_volume(0.4)
        self.ch = pg.mixer.Channel(2)

    def start_cutscene(self, cutscene):
        if cutscene.name not in self.cutscenes_complete:
            self.cutscenes_complete.append(cutscene.name)
            self.cutscene = cutscene
            self.cutscene_running = True

    def end_cutscene(self):
        self.cutscene = None
        self.cutscene_running = False

    def update(self):
        if self.timer > 0:
            self.timer -= 1

        if self.timer == 0:
            self.timer = 10
            self.ch.play(self.sound)

        if self.cutscene_running:
            if self.window_size < self.screen.get_height() * 0.3:
                self.window_size += 4

            if self.is_dialogue_screen_draw is True:
                self.cutscene_running = self.cutscene.update_metadata()
        else:
            self.end_cutscene()

    def draw(self):
        if self.cutscene_running:
            # Desenha a caixa. Depois exibe o diálogo. Ela ocupa 1/3 da tela
            if self.window_size < self.screen.get_height() * 0.3:

                self.surf = pg.Surface((int(self.screen.get_width()), int(self.window_size)))
                self.surf.fill((158, 161, 154))
                self.surf.set_alpha(180)
                self.screen.blit(self.surf, (0, 0))
                #  pg.draw.rect(self.screen,
                #        (158, 161, 154), #5F665C. Cor da caixa
                #       (0, 0, self.screen.get_width(),
                #      self.window_size))
            else:
                # Condição de checagem se desenhou completamente a caixa
                self.is_dialogue_screen_draw = True

                self.surf = pg.Surface((int(self.screen.get_width()), int(self.window_size)))
                self.surf.fill((158, 161, 154))
                self.surf.set_alpha(180)
                self.screen.blit(self.surf, (0, 0))

                # pg.draw.rect(self.screen,
                #        (158, 161, 154), #5F665C
                #        (0, 0, self.screen.get_width(),
                #        self.window_size))

                # Desenha o diálogo. indice zero do dicionario da cutscene no json.
                dialogue_displayed = self.cutscene.dialogue[0:int(self.cutscene.dialogue_position)]

                # Linha de teste para testar velocidade do diálogo e posição. Ignorar.
                # print(self.window_size, self.cutscene.dialogue_position, dialogue_displayed)

                draw_text(
                    self.screen,
                    dialogue_displayed,
                    self.cutscene.size,
                    self.cutscene.rgb_color,
                    self.cutscene.pos_x,
                    self.cutscene.pos_y
                )
