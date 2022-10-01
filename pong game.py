#pong game

import pygame
import sys
import random

pygame.init()

#colors
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

#screen
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Pong")
screen.fill(black)

#paddle
paddle = pygame.Rect(10,250,10,100)
paddle2 = pygame.Rect(780,250,10,100)
paddle_speed = 0
paddle2_speed = 0

#ball
ball = pygame.Rect(400,300,10,10)
ball_speed_x = 5
ball_speed_y = 5

#score
score = 0
score2 = 0

#font
font = pygame.font.Font(None, 74)

#clock
clock = pygame.time.Clock()

#game loop
while True:
    #event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                paddle_speed -= 5
            if event.key == pygame.K_DOWN:
                paddle_speed += 5
            if event.key == pygame.K_w:
                paddle2_speed -= 5
            if event.key == pygame.K_s:
                paddle2_speed += 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                paddle_speed += 5
            if event.key == pygame.K_DOWN:
                paddle_speed -= 5
            if event.key == pygame.K_w:
                paddle2_speed += 5
            if event.key == pygame.K_s:
                paddle2_speed -= 5

    #paddle movement
    paddle.y += paddle_speed
    paddle2.y += paddle2_speed

    #ball movement
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    #ball collision
    if ball.top <= 0 or ball.bottom >= 600:
        ball_speed_y *= -1
    if ball.left <= 0:
        ball_speed_x *= -1
        score += 1
    if ball.right >= 800:
        ball_speed_x *= -1
        score2 += 1
    if paddle.colliderect(ball):
        ball_speed_x *= -1
    if paddle2.colliderect(ball):
        ball_speed_x *= -1

    #paddle collision
    if paddle.top <= 0:
        paddle.top = 0
    if paddle.bottom >= 600:
        paddle.bottom = 600
    if paddle2.top <= 0:
        paddle2.top = 0
    if paddle2.bottom >= 600:
        paddle2.bottom = 600

    #score
    score_text = font.render(str(score), True, white)
    score_text2 = font.render(str(score2), True, white)

    #draw
    screen.fill(black)
    pygame.draw.rect(screen, white, paddle)
    pygame.draw.rect(screen, white, paddle2)
    pygame.draw.ellipse(screen, white, ball)
    screen.blit(score_text, (350,50))
    screen.blit(score_text2, (450,50))
    pygame.display.flip()

    #clock
    clock.tick(60)


