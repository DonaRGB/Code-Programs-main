import pygame as pg
import sys
pg.init()
ratio = 3/2
WIDTH,HEIGHT = ratio * 600, ratio * 400
screen = pg.display.set_mode((WIDTH,HEIGHT))
pg.display.set_caption("Ball Paddle Game")
p = (255,255,255)
b = (0,0,0)
paddle_width,paddle_height = ratio * 100, ratio * 10
paddle_x = WIDTH // 2 - paddle_width // 2
paddle_y = HEIGHT - 30 * ratio
paddle_speed = 7 * ratio
ball_r = 10 * ratio
ball_x,ball_y = WIDTH//2,HEIGHT//2
ball_dx,ball_dy = 4 * ratio,-4 * ratio
clock = pg.time.Clock()
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
    keys = pg.key.get_pressed()
    if keys[pg.K_LEFT] and paddle_x > 0:
        paddle_x -= paddle_speed
    if keys[pg.K_RIGHT] and paddle_x < WIDTH - paddle_width:
        paddle_x += paddle_speed
    ball_x += ball_dx
    ball_y += ball_dy
    if ball_x - ball_r <= 0 or ball_x + ball_r >= WIDTH:
        ball_dx *= -1
    if ball_y - ball_r <= 0:
        ball_dy *= -1
    if (paddle_y <= ball_y + ball_r <= paddle_y + paddle_height and paddle_x <= ball_x <= paddle_x + paddle_width):
        ball_dy *= -1
    if ball_y > HEIGHT:
        print("Game Over")
        pg.quit()
        sys.exit()
    screen.fill(b)
    pg.draw.rect(screen,p,(paddle_x,paddle_y,paddle_width,paddle_height))
    pg.draw.circle(screen,p,(ball_x,ball_y),ball_r)
    pg.display.flip()
    clock.tick(60)