import pygame as pg


def draw_text(screen, text, size, color, x, y):
    font = pg.font.SysFont(None, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.topleft = (x, y)
    screen.blit(text_surface, text_rect)


class Button:
    def __init__(self, color, x, y, width, height, text=""):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw_button(self, screen):
        pg.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height), 0)

        if self.text != "":
            font = pg.font.SysFont(None, 50)
            text = font.render(self.text, 1, (0, 0, 0))
            screen.blit(text, (
            self.x + (self.width / 2 - text.get_width() / 2), self.y + (self.height / 2 - text.get_height() / 2)))


_atk = Button((255, 255, 255), 50, 560, 100, 40, "ATK")
_def = Button((255, 255, 255), 270, 560, 100, 40, "DEF")
_skill = Button((255, 255, 255), 50, 620, 100, 40, "SKL")
_run = Button((255, 255, 255), 270, 620, 100, 40, "RUN")


class BattleBox:
    def __init__(self, screen):
        self.screen = screen
        self.window_size = 0

    def update(self):
        if self.window_size < self.screen.get_height() * 0.3:
            self.window_size += 90

    def draw(self):
        if self.window_size < self.screen.get_height() * 0.3:
            pg.draw.rect(self.screen,
                         (255, 255, 255),
                         (0, 530, self.screen.get_width() * 0.5,
                          self.window_size))
        else:
            pg.draw.rect(self.screen,
                         (255, 255, 255),
                         (0, 530, self.screen.get_width() * 0.5,
                          self.window_size))

            _atk.draw_button(self.screen)
            _def.draw_button(self.screen)
            _skill.draw_button(self.screen)
            _run.draw_button(self.screen)


class BattleLog:
    def __init__(self, screen):
        self.screen = screen
        self.window_size = 0

    def update(self):
        if self.window_size < self.screen.get_height() * 0.3:
            self.window_size += 90

    def draw(self):
        if self.window_size < self.screen.get_height() * 0.3:
            pg.draw.rect(self.screen,
                         (220, 220, 220),
                         (self.screen.get_width() * 0.5, 530, self.screen.get_width() * 0.5,
                          self.window_size))
        else:
            pg.draw.rect(self.screen,
                         (220, 220, 220),
                         (self.screen.get_width() * 0.5, 530, self.screen.get_width() * 0.5,
                          self.window_size))

    def draw_text(self, text, screen):
        font = pg.font.SysFont(None, 40)
        text = font.render(text, 1, (0, 0, 0))
        screen.blit(text, ((self.screen.get_width() * 0.5) + 20, 540))
