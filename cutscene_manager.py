import pygame as pg

def draw_text(screen, text, size, color, x, y):
    font = pg.font.SysFont(None, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.topleft = (x, y)
    screen.blit(text_surface, text_rect)


class Cutscene:
    def __init__(self, cutscene_metadata):

        self.cutscene = cutscene_metadata

        self.name = self.cutscene['name']

        self.final_step = self.cutscene['final_step']
        self.cur_step = 0

        self.dialogue = ''
        self.text_speed = 0
        self.dialogue_position = 0

        self.size = None
        self.rgb_color = ()
        self.pos_x = None
        self.pos_y = None

        self.cutscene_running = True

        self.__set_dialogue(self.cur_step)

        self.chr_displayed = -3

    def __set_dialogue(self, cur_step):
        cur_event = self.cutscene['events'][cur_step]
        self.dialogue = cur_event['text']
        self.text_speed = cur_event['speed']

        self.size = cur_event['size']
        self.rgb_color = tuple(cur_event['rgb_color'])
        self.pos_x = cur_event['pos_x']
        self.pos_y = cur_event['pos_y']

        self.dialogue_position = 0

    def update_metadata(self):
        pressed = pg.key.get_pressed()
        space = pressed[pg.K_SPACE]

        if int(self.dialogue_position) < len(self.dialogue):
            self.dialogue_position += self.text_speed
        else:
            if space:
                if self.cur_step == self.final_step:
                    self.cutscene_running = False
                else:
                    self.cur_step += 1
                    self.chr_displayed = -3
                    self.__set_dialogue(self.cur_step)

        return self.cutscene_running


class CutSceneManager:

    def __init__(self, screen):
        self.cutscenes_complete = []
        self.cutscene = None
        self.cutscene_running = False

        self.screen = screen
        self.window_size = 0

        self.is_dialogue_screen_draw = False

        self.surf = pg.Surface((int(self.screen.get_width()), int(self.window_size)))

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
        if self.cutscene_running:
            if self.window_size < self.screen.get_height() * 0.3:
                self.window_size += 4

            if self.is_dialogue_screen_draw is True:
                self.cutscene_running = self.cutscene.update_metadata()
        else:
            self.end_cutscene()

    def draw(self):
        if self.cutscene_running:
            if self.window_size < self.screen.get_height() * 0.3:

                self.surf = pg.Surface((int(self.screen.get_width()), int(self.window_size)))
                self.surf.fill((158, 161, 154))
                self.surf.set_alpha(180)
                self.screen.blit(self.surf, (0, 0))
            else:
                self.is_dialogue_screen_draw = True

                self.surf = pg.Surface((int(self.screen.get_width()), int(self.window_size)))
                self.surf.fill((158, 161, 154))
                self.surf.set_alpha(180)
                self.screen.blit(self.surf, (0, 0))

                dialogue_displayed = self.cutscene.dialogue[0:int(self.cutscene.dialogue_position)]

                if int(self.cutscene.dialogue_position) >= self.cutscene.chr_displayed + 4:
                    self.ch.play(self.sound)
                    self.cutscene.chr_displayed += 4

                draw_text(
                    self.screen,
                    dialogue_displayed,
                    self.cutscene.size,
                    self.cutscene.rgb_color,
                    self.cutscene.pos_x,
                    self.cutscene.pos_y
                )
