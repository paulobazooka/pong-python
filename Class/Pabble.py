from Class.Table import *


class Paddle(pygame.sprite.Sprite):

    # Inicia a barra do jogador com alguns parâmentros
    def __init__(self, player_number):
        pygame.sprite.Sprite.__init__(self)

        self.player_number = player_number
        self.image = pygame.Surface([10, 100])
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.speed = 8

        # Estabelecendo a posição das barras dos dois jogadores
        if self.player_number == 1:
            self.rect.centerx = main_surface.get_rect().left
            self.rect.centerx += 50
        elif self.player_number == 2:
            self.rect.centerx = main_surface.get_rect().right
            self.rect.centerx -= 50
        self.rect.centery = main_surface.get_rect().centery

    # Mover a barra para cima e para baixo
    def move(self, UP, DOWN, NO_MOVEMENT):
        if UP and (self.rect.y > 5):
            self.rect.y -= self.speed
        elif DOWN and (self.rect.bottom < WINDOW_HEIGHT - 5):
            self.rect.y += self.speed
        elif NO_MOVEMENT:
            pass
