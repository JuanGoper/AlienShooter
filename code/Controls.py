import sys

import pygame
from pygame import Surface, Rect, KEYDOWN, K_ESCAPE
from pygame.font import Font

from code.Const import C_BLACK, C_CYAN, C_PURPLE, CONTROLS_POS, C_PLAYER1, WIN_WIDTH, C_PLAYER2


class Controls:

    def __init__(self, window: Surface):
        self.window = window
        self.surf = pygame.image.load('./asset/ScoreBg.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)
        pygame.mixer_music.load('./asset/Score.mp3')
        pygame.mixer_music.play(-1)
        pass

    def show(self):
        self.window.blit(source=self.surf, dest=self.rect)
        self.controls_teletext(48, 'CONTROLS', C_BLACK, CONTROLS_POS['Title'])
        self.labels_text(20, 'Player 1', C_PURPLE, CONTROLS_POS['Label1'])
        self.labels_text(20, 'Player 2', C_CYAN, CONTROLS_POS['Label2'])

        for i in range(len(C_PLAYER1)):
            self.controls_text(20, C_PLAYER1[i], C_BLACK, (WIN_WIDTH / 3, 110 + 20 * i))

        for i in range(len(C_PLAYER2)):
            self.controls_text(20, C_PLAYER2[i], C_BLACK, ((WIN_WIDTH / 3 * 2), 110 + 20 * i))

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        return
            pygame.display.flip()

    def controls_teletext(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name='FoundationOne', size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)

    def labels_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name='Sylfaen', size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)

    def controls_text(self, text_size: int, text: tuple, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name='Sylfaen', size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
