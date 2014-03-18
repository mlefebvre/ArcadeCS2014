#!/usr/bin/env python
#coding: utf8

import pygame
from effects.effect import Effect
import random

TRAIL_SIZE = 50


class DogeText(Effect):

    words = ["Much beer", "Such drunk", "Wow",
             "So thirsty", "Very drunk", "Wow",
             "Much alcohol", "Such degrise" ]
    word_id = 0

    colors = [(255, 0, 0), (200, 0, 200), (0, 0, 255)]

    font = None

    draw_pos = None

    def __init__(self, gameboard, duration):
        Effect.__init__(self,
                        None,
                        self._create_text(gameboard),
                        gameboard,
                        duration)

    def blit(self):
        #alpha = int((1.0 - (pygame.time.get_ticks() - self.start_time) / float(self.duration)) * 255)
        #self.image.set_alpha(alpha)
        self.gameboard.blit(self.image, self.draw_pos)

    def _create_text(self, gameboard):
        if not DogeText.font:
            DogeText.font = pygame.font.SysFont("Comic Sans MS", int(gameboard.width * 0.05))

        word = self.words[DogeText.word_id]
        DogeText.word_id = (DogeText.word_id + 1) % len(DogeText.words)

        text = DogeText.font.render(word, 1, random.choice(DogeText.colors))
        text = pygame.transform.rotate(text, random.randint(-15, 15))

        self.draw_pos = ((DogeText.word_id % 3) * 0.33 * gameboard.width,
                         random.random() * 0.3 * gameboard.height)

        return text
