import pygame
import sys

# General setup
pygame.init()
clock = pygame.time.Clock()

# Setting up main window
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width,screen_height))

# Game objects
ball = pygame.Rect(screen_width/2 - 15, screen_height/2 - 15, 30, 30)
paddle1 = pygame.Rect(screen_width - 20, screen_height/2, 10, 100)
paddle2 = pygame.Rect(10, screen_height/2, 10, 100)

# Game variables
ball_speed = [2, 2]
paddle_speed = 2

def draw_objects():
    screen.fill(pygame.Color('black'))
    pygame.draw.rect(screen, pygame.Color('white'), paddle1)
    pygame.draw.rect(screen, pygame.Color('white'), paddle2)
    pygame.draw.ellipse(screen, pygame.Color('white'), ball)
    pygame.draw.aaline(screen, pygame.Color('white'), (screen_width / 2, 0),(screen_width / 2, screen_height))

def check_ball_collision():
    global ball_speed
    if ball.left < 0 or ball.right > screen_width:
        ball_speed[0] *= -1
    if ball.top < 0 or ball.bottom > screen_height:
        ball_speed[1] *= -1

    if ball.colliderect(paddle1) or ball.colliderect(paddle2):
        ball_speed[0] *= -1.1  # Increase speed by 10%
        ball_speed[1] *= -1.1  # Increase speed by 10%

def check_paddle_collision():
    if paddle1.top < 0:
        paddle1.top = 0
    if paddle1.bottom > screen_height:
        paddle1.bottom = screen_height
    if paddle2.top < 0:
        paddle2.top = 0
    if paddle2.bottom > screen_height:
        paddle2.bottom = screen_height

def game_loop():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Ball movement
        ball.x += ball_speed[0]
        ball.y += ball_speed[1]

        # Player paddle movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            paddle1.y -= paddle_speed
        if keys[pygame.K_DOWN]:
            paddle1.y += paddle_speed

        # AI paddle movement
        if paddle2.centery < ball.centery:
            paddle2.y += paddle_speed
        elif paddle2.centery > ball.centery:
            paddle2.y -= paddle_speed

        check_ball_collision()
        check_paddle_collision()

        draw_objects()

        pygame.display.flip()
        clock.tick(60)

game_loop()
