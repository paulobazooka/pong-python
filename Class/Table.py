import pygame, sys, time
from pygame.locals import *
from random import randint

pygame.init()

WINDOW_WIDTH = 1024
WINDOW_HEIGHT = 600

# Frame por segundo
clock = pygame.time.Clock()

player1_win = False
player2_win = False


# Paddle velocidade
PADDLE_SPEED = 10

UP1 = False
DOWN1 = False
NO_MOVEMENT1 = True

UP2 = False
DOWN2 = False
NO_MOVEMENT2 = True


# posição da bola
UPLEFT = 0
DOWNLEFT = 1
UPRIGHT = 2
DOWNRIGHT = 3


# cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


# fonte do jogo
basic_font = pygame.font.SysFont("Helvetica", 120)
game_over_font_big = pygame.font.SysFont("Helvetica", 72)
game_over_font_small = pygame.font.SysFont("Helvetica", 50)
label_ex_small = pygame.font.SysFont("Helvetica", 25)


# criando a tela principal
main_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), 0, 32)
surface_rect = main_surface.get_rect()
