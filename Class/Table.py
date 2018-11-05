import pygame, sys, time
from pygame.locals import *
from random import randint

pygame.init()

WINDOW_WIDTH = 1024
WINDOW_HEIGHT = 600

clock = pygame.time.Clock()

player1_win = False
player2_win = False


### Paddle Stuff ###
PADDLE_SPEED = 10

UP1 = False
DOWN1 = False
NO_MOVEMENT1 = True

UP2 = False
DOWN2 = False
NO_MOVEMENT2 = True


### Ball Stuff ###
UPLEFT = 0
DOWNLEFT = 1
UPRIGHT = 2
DOWNRIGHT = 3


### Music ###
# pygame.mixer.music.load("../Music/endofline.ogg")
# sound_effect = pygame.mixer.Sound("../Music/beep.wav")


### colors ###
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


### Game Font ###
basic_font = pygame.font.SysFont("Helvetica", 120)
game_over_font_big = pygame.font.SysFont("Helvetica", 72)
game_over_font_small = pygame.font.SysFont("Helvetica", 50)


### Creating the main surface ###
main_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), 0, 32)
surface_rect = main_surface.get_rect()
