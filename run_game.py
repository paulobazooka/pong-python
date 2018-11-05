from Class.Table import *
from Class.Pabble import Paddle
from Class.Ball import Ball


paddle1 = Paddle(1)
paddle2 = Paddle(2)

ball = Ball()

all_sprites = pygame.sprite.RenderPlain(paddle1, paddle2, ball)

player1_score = 0
player2_score = 0


def paddle_hit():
    if pygame.sprite.collide_rect(ball, paddle2):
        if ball.direction == UPRIGHT:
            ball.direction = UPLEFT
        elif ball.direction == DOWNRIGHT:
            ball.direction = DOWNLEFT
        ball.speed += 1
        # sound_effect.play()
    elif pygame.sprite.collide_rect(ball, paddle1):
        if ball.direction == UPLEFT:
            ball.direction = UPRIGHT
        elif ball.direction == DOWNLEFT:
            ball.direction = DOWNRIGHT
        ball.speed += 1
        # sound_effect.play()


counter = 0

while True:

    clock.tick(60)

    if ball.rect.x > WINDOW_WIDTH:
        ball.rect.centerx = surface_rect.centerx
        ball.rect.centery = surface_rect.centery
        ball.direction = randint(0, 1)
        ball.speed = 4
    elif ball.rect.x < 0:
        ball.rect.centerx = surface_rect.centerx
        ball.rect.centery = surface_rect.centery
        ball.direction = randint(2, 3)
        ball.speed = 4

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()

            if event.key == ord('w'):
                UP1 = True
                DOWN1 = False
                NO_MOVEMENT1 = False
            elif event.key == ord('s'):
                UP1 = False
                DOWN1 = True
                NO_MOVEMENT1 = False

            elif event.key == K_UP:
                UP2 = True
                DOWN2 = False
                NO_MOVEMENT2 = False
            elif event.key == K_DOWN:
                UP2 = False
                DOWN2 = True
                NO_MOVEMENT2 = False

        elif event.type == KEYUP:
            if event.key == ord('w') or event.key == ord('s'):
                NO_MOVEMENT1 = True
                DOWN1 = False
                UP1 = False
            elif event.key == K_DOWN or event.key == K_UP:
                NO_MOVEMENT2 = True
                DOWN2 = False
                UP2 = False

    score_board = basic_font.render(str(player1_score) + "           " + str(player2_score), True, WHITE, BLACK)
    score_board_rect = score_board.get_rect()
    score_board_rect.centerx = surface_rect.centerx
    score_board_rect.y = 10

    main_surface.fill(BLACK)

    main_surface.blit(score_board, score_board_rect)

    all_sprites.draw(main_surface)

    paddle1.move(UP1, DOWN1, NO_MOVEMENT1)
    paddle2.move(UP2, DOWN2, NO_MOVEMENT2)
    ball.move()
    ball.change_direction()

    paddle_hit()

    if ball.rect.x > WINDOW_WIDTH:
        player1_score += 1
    elif ball.rect.x < 0:
        player2_score += 1

    pygame.display.update()

    if counter == 0:
        time.sleep(1.5)
        # pygame.mixer.music.play(-1, 0.5)

    if player1_score == 5:
        player1_win = True
        break
    elif player2_score == 5:
        player2_win = True
        break

    counter += 1

while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()

    main_surface.fill(BLACK)

    if player1_win == True:
        game_over = game_over_font_big.render("GAME OVER", True, WHITE, BLACK)
        game_over1 = game_over_font_small.render("Player 1 Wins", True, WHITE, BLACK)
    elif player2_win == True:
        game_over = game_over_font_big.render("GAME OVER", True, WHITE, BLACK)
        game_over1 = game_over_font_small.render("Player 2 Wins", True, WHITE, BLACK)

    game_over_rect = game_over.get_rect()
    game_over_rect.centerx = surface_rect.centerx
    game_over_rect.centery = surface_rect.centery - 50
    game_over1_rect = game_over1.get_rect()
    game_over1_rect.centerx = game_over_rect.centerx
    game_over1_rect.centery = game_over_rect.centery + 75

    main_surface.blit(game_over, game_over_rect)
    main_surface.blit(game_over1, game_over1_rect)

    pygame.display.update()
