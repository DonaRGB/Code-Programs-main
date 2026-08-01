import pygame as pg
import sys
pg.init()
ratio = 3/2
WIDTH,HEIGHT = ratio * 600, ratio * 400
DEFAULT_FRAMES = 60
DEFAULT_BALL_SPEED = 4
DEFAULT_PADDLE_SPEED = 7
screen = pg.display.set_mode((WIDTH,HEIGHT))
pg.display.set_caption("Ball Paddle Game")
paddle_color = (255,126,12)
background_color = (12,16,20)
ball_color = (255,1,100)
paddle_width,paddle_height = ratio * 100, ratio * 10
paddle_x = WIDTH // 2 - paddle_width // 2
paddle_y = HEIGHT - 30 * ratio
paddle_speed = 7 * ratio
ball_speed = 4
ball_r = 10 * ratio
ball_x,ball_y = WIDTH//2,HEIGHT//2
ball_dx,ball_dy = ball_speed * ratio,-1 * ball_speed * ratio
ball_dxc,ball_dyc = 4 * ratio,-4 * ratio
clock = pg.time.Clock()
frames = 60
pause = 1
score = 0
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
    keys = pg.key.get_pressed()
    if (keys[pg.K_LEFT] or keys[pg.K_a]) and paddle_x > 0:
        paddle_x -= paddle_speed
    if (keys[pg.K_RIGHT] or keys[pg.K_d]) and paddle_x < WIDTH - paddle_width:
        paddle_x += paddle_speed
    if keys[pg.K_SPACE]:
        pause = 1 - pause
    #ball_dx = ball_dxc * pause
    #ball_dy = ball_dyc * pause
    ball_x += ball_dx
    ball_y += ball_dy
    if ball_x - ball_r <= 0 or ball_x + ball_r >= WIDTH:
        ball_dx *= -1
    if ball_y - ball_r <= 0:
        ball_dy *= -1
    if (paddle_y <= ball_y + ball_r <= paddle_y + paddle_height and paddle_x <= ball_x <= paddle_x + paddle_width):
        ball_dy *= -1
        score += 1
    if ball_y > HEIGHT:
        print("Score :",score)
        print("Game Over")
        pg.quit()
        sys.exit()
    screen.fill(background_color)
    pg.draw.rect(screen,paddle_color,(paddle_x,paddle_y,paddle_width,paddle_height))
    pg.draw.circle(screen,ball_color,(ball_x,ball_y),ball_r)
    pg.display.flip()
    clock.tick(frames)