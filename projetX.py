#!/usr/bin/env python
#coding: utf8

import pygame

from player import Player
from obstacles.obstaclemanager import ObstacleManager
from collisionstrategies.collision_strategy_factory import CollisionStrategyFactory
from gameboard import GameBoard
from menus.scoreboard import ScoreBoard
from menus.topmenu import TopMenu
from menus.mainmenu import MainMenu
from scoremanager import ScoreManager


WINDOW_WIDTH = 720#1080
WINDOW_HEIGHT = 600#900
GAME_SIZE = int(WINDOW_WIDTH * 0.70)
FPS = 60
LEFT_KEY = pygame.K_LEFT
RIGHT_KEY = pygame.K_RIGHT
MODE = 0 #pygame.FULLSCREEN


DEBUG = True
DB_FILE = "scoreboard.sqlite"

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)


class Game:
    controls_reversed = False
    score = 0
    time_passed = 0
    done = False
    screen = None
    obstacle_manager = None
    gameboard = None
    scoreboard = None
    topmenu = None
    game_started = False

    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.score_manager = ScoreManager(DB_FILE)

    def start(self):
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), MODE)
        self.gameboard = GameBoard((GAME_SIZE, GAME_SIZE), self)
        self.scoreboard = ScoreBoard((WINDOW_WIDTH - GAME_SIZE, WINDOW_HEIGHT), self.score_manager)
        self.topmenu = TopMenu((GAME_SIZE, WINDOW_HEIGHT - GAME_SIZE))
        self.mainmenu = MainMenu((WINDOW_WIDTH, WINDOW_HEIGHT), self)

        while not self.done:
            key = pygame.key.get_pressed()
            left, right = self._get_movement(key)

            if key[pygame.K_ESCAPE]:
                self.done = True

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.done = True

            if self.game_started:
                self._tick(left, right)
            else:
                self._main_menu_tick(left, right)

            pygame.display.flip()

            self.time_passed = self.clock.tick(FPS)

        pygame.quit()

    def reverse_controls(self, reversed):
        self.controls_reversed = reversed

    def _get_movement(self, key):
        left = key[LEFT_KEY] == 1
        right = key[RIGHT_KEY] == 1

        if self.controls_reversed:
            left = not left
            right = not right

        return left, right

    def _main_menu_tick(self, select, switch):
        self.mainmenu.update(select, switch)

        self.screen.blit(self.mainmenu.render(), (0, 0))

    def _tick(self, left, right):
        direction = 0
        if not (left and right):
            if left:
                direction = -1
            elif right:
                direction = 1

        self.score_manager.increment_score(1)
        self.gameboard.set_player_direction(direction)
        self.gameboard.tick(self.time_passed)

        self.screen.blit(self.gameboard.render(), (0, WINDOW_HEIGHT - GAME_SIZE))
        self.screen.blit(self.scoreboard.render(), (GAME_SIZE, 0))
        self.screen.blit(self.topmenu.render(), (0, 0))

    def start_game(self, school):
        self.game_started = True
        self.gameboard.reset()
        print school

    def stop_game(self):
        self.game_started = False
        self.controls_reversed = False

    def drink(self):
        self.scoreboard.remove_life()
        print self.scoreboard.is_game_over()

if __name__ == "__main__":
    game = Game()
    game.start()
