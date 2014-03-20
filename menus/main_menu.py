#!/usr/bin/env python
#coding: utf8

import pygame
from pygame.surface import Surface


class MainMenu(Surface):
    fire_files = ['images/menus/top/fire1.gif',
                  'images/menus/top/fire2.gif',
                  'images/menus/top/fire3.gif',
                  'images/menus/top/fire4.gif']
    background_files = ['images/menus/mainmenu/mainmenu0.png',
                        'images/menus/mainmenu/mainmenu1.png',
                        'images/menus/mainmenu/mainmenu2.png',
                        'images/menus/mainmenu/mainmenu3.png']

    star_file = 'images/menus/mainmenu/star.png'
    back1_file = 'images/menus/mainmenu/back1.png'
    back2_file = 'images/menus/mainmenu/back2.png'
    arrowh_file = 'images/menus/mainmenu/arrowh.png'
    arrowv_file = 'images/menus/mainmenu/arrowv.png'

    fire_images = []
    background_images = []
    star_image = None
    back1_image = None
    back2_image = None
    arrowh_image = None
    arrowv_image = None

    column_selected = False
    column_id = 0
    row_id = 0

    switch = False
    select = False

    schools = [['ETS', 'Brock', 'Concordia', 'Guelph', 'Laval', 'Manitoba'],
               ['McGill', 'Ottawa', 'Poly', 'Queen\'s', 'Rochester', 'Sherbrooke'],
               ['Shippensburg', 'Toronto', 'UDEM', 'UQAC', 'UQAM', 'UQAR'],
               ['UQO', 'Windsor', 'York']]

    def __init__(self, size, game):
        Surface.__init__(self, size)
        self.width, self.height = size
        self.game = game
        self._load_images()
        self.font = pygame.font.SysFont("Comic Sans MS", int(0.09 * self.width))
        self.select_column_text = self.font.render("Select column", 1, (255, 255, 0))
        self.select_school_text = self.font.render("Select school", 1, (255, 255, 0))

    def reset(self):
        self.column_selected = False

    def update(self, select, switch):
        if switch:
            self.switch = True
        elif select:
            self.select = True
        elif self.switch:
            if not self.column_selected:
                self.column_id = (self.column_id + 1) % len(self.schools)
                self.row_id = 0
            else:
                self.row_id = (self.row_id + 1) % (len(self.schools[self.column_id]) + 1)
            self.switch = False
        elif self.select:
            if not self.column_selected:
                self.column_selected = True
                self.select = False
            else:
                self.select = False
                if self.row_id == len(self.schools[self.column_id]):
                    self.column_selected = False
                    self.select = False
                    self.row_id = 0
                else:
                    school = self.schools[self.column_id][self.row_id]
                    self.reset()
                    self.game.start_game(school)

    def render(self):
        self.blit(self.background_images[self.column_id], self.background_images[self.column_id].get_rect())

        ###################################### FEU ###############################
        fire = self.fire_images[(pygame.time.get_ticks() / 150) % len(self.fire_files)]
        rect = fire.get_rect()
        draw_pos = fire.get_rect().move(int(self.width * 0.07), int(0.15 * self.height))
        self.blit(fire, draw_pos)

        ################################### Étoiles ##############################
        if ((pygame.time.get_ticks()) / 300) % 2 == 0:
            self.blit(self.star_image, self.star_image.get_rect().move(int(self.width * 0.07), int(self.height * 0.04)))

        if ((pygame.time.get_ticks()) / 300) % 2 == 1:
            self.blit(self.star_image, self.star_image.get_rect().move(int(self.width * 0.84), int(self.height * 0.04)))

        #################################### Titre ################################
        if not self.column_selected:
            self.blit(self.select_column_text, self.select_column_text.get_rect().move(int(self.width * 0.22), int(self.height * 0.02)))
        else:
            self.blit(self.select_school_text, self.select_school_text.get_rect().move(int(self.width * 0.22), int(self.height * 0.02)))

        #################################### Fleches #############################
        if self.column_selected:
            self.blit(self.arrowv_image, self.arrowv_image.get_rect().move(int(self.width * 0.74), int(self.height * 0.86)))
        else:
            self.blit(self.arrowh_image, self.arrowh_image.get_rect().move(int(self.width * 0.74), int(self.height * 0.885)))

        ############################### Selection colonne #########################
        if not self.column_selected:
            pygame.draw.rect(self,
                             (255, 255, 0),
                             pygame.Rect((0.075 * self.width + 0.213 * self.width * self.column_id,
                                          0.224 * self.height),
                                         (0.213 * self.width,
                                          self.height * 0.0925 * len(self.schools[self.column_id]))),
                             10)
        ############################### Selection ecole ###########################
        else:
            if self.row_id == len(self.schools[self.column_id]):
                self.blit(self.back2_image, self.back2_image.get_rect().move(int(self.width * 0.4), int(self.height * 0.82)))
            else:
                pygame.draw.rect(self,
                                 (255, 255, 0),
                                 pygame.Rect((0.075 * self.width + 0.213 * self.width * self.column_id,
                                              0.224 * self.height + 0.0925 * self.height * self.row_id),
                                             (0.213 * self.width,
                                              0.0925 * self.height)),
                                 10)
                self.blit(self.back1_image, self.back1_image.get_rect().move(int(self.width * 0.4), int(self.height * 0.82)))


        return self

    def _load_images(self):
        self._load_background()
        self._load_fire()
        self._load_star()
        self._load_back()
        self._load_arrows()

    def _load_arrows(self):
        self.arrowh_image = pygame.image.load(self.arrowh_file).convert_alpha()
        self.arrowv_image = pygame.image.load(self.arrowv_file).convert_alpha()
        height1 = self.arrowh_image.get_height()
        width1 = self.arrowh_image.get_width()
        height2 = int(self.height * 0.07)
        width2 = int((width1 / float(height1)) * height2)
        self.arrowh_image = pygame.transform.smoothscale(self.arrowh_image, (width2, height2))
        self.arrowv_image = pygame.transform.smoothscale(self.arrowv_image, (height2, width2))

    def _load_fire(self):
        for f in self.fire_files:
            image = pygame.image.load(f)
            rect = image.get_rect()
            image = pygame.transform.scale(image, (int(self.width * 0.85), int((rect.height / float(rect.width)) * self.width * 0.85 * 0.80)))
            self.fire_images.append(image)

    def _load_background(self):
        for bf in self.background_files:
            image = pygame.image.load(bf)
            rect = image.get_rect()
            image = pygame.transform.smoothscale(image, (self.width, int((rect.height / float(rect.width)) * self.width)))
            self.background_images.append(image)

    def _load_star(self):
        self.star_image = pygame.image.load(self.star_file).convert_alpha()
        height1 = self.star_image.get_height()
        width1 = self.star_image.get_width()

        height2 = int(self.height * 0.10)
        width2 = int((width1 / float(height1)) * height2)

        self.star_image = pygame.transform.smoothscale(self.star_image, (width2, height2))

    def _load_back(self):
        self.back1_image = pygame.image.load(self.back1_file).convert_alpha()
        height1 = self.back1_image.get_height()
        width1 = self.back1_image.get_width()

        height2 = int(self.height * 0.12)
        width2 = int((width1 / float(height1)) * height2)

        self.back1_image = pygame.transform.smoothscale(self.back1_image, (width2, height2))

        self.back2_image = pygame.image.load(self.back2_file).convert_alpha()
        height1 = self.back2_image.get_height()
        width1 = self.back2_image.get_width()

        height2 = int(self.height * 0.12)
        width2 = int((width1 / float(height1)) * height2)

        self.back2_image = pygame.transform.smoothscale(self.back2_image, (width2, height2))