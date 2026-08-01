import pygame
import sys
from random import randint as r
from AAAAAAAAAATest import list_segmentation as ls
def factors_of_a_number(num : int):
    if not isinstance(num,int):
        raise TypeError(f"Expected int, got {type(num).__name__} instead.")
    fac = [1]
    for i in range(2,num,1):
        if num%i == 0:
            fac.append(i)
        else:
            pass
    fac.append(num)
    return fac
def is_coprime(a,b):
    fa = factors_of_a_number(int(a))
    fb = factors_of_a_number(int(b))
    if len(fa) <= 1 or len(fb) <= 1:
        return False
    try:
        for i in fa[1:]:
            for j in fb[1:]:
                if i == j:
                    return False
        return True
    except IndexError as e:
        raise Exception(f"There is not enough elements in the list : {e}")
def color_generator():
    return (r(0,255),r(0,255),r(0,255))
def list_from_to_generation(o,n,i=1):
    if o > n:
        i = -i
    return list(range(o,n+1,i))
def coordinate_pairing_merger(x_l,y_l):
    new_coords = []
    try:
        for i in range(len(x_l)):
            new_coords.append((x_l[i],y_l[i]))
        return new_coords
    except IndexError:
        return new_coords
def loc_draws(locs,screen,ball_r,color = color_generator()):
    for x,y in ls(locs):
        pygame.draw.circle(screen,color,(x,y),ball_r)
        #print(locs)
scale = 6
w,h = r(200,300),r(150,250)
while not is_coprime(w,h):
    break
    w,h = r(200,300),r(150,250)
WIDTH, HEIGHT =  78 * scale, 43 * scale
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Light Bounce Simulation")
speed = 5 * scale
clock = pygame.time.Clock()
bg_color = (0,0,0)
light_color = (255,255,255)
ball_radius = 3
ball_x,ball_y = ball_radius,HEIGHT - ball_radius
ball_dx,ball_dy = speed,-speed
DEFAULT_FRAMES = 60
frames = DEFAULT_FRAMES
incr = 5
locs = []
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        pygame.quit()
        sys.exit()
    if keys[pygame.K_UP] or keys[pygame.K_RIGHT]:
        frames += 5
        print("Frames :",frames)
    if keys[pygame.K_DOWN] or keys[pygame.K_LEFT]:
        frames -= 5
        print("Frames :",frames)
    if keys[pygame.K_0]:
        frames = 0
        print("Frames :",frames)
    if keys[pygame.K_1]:
        frames = DEFAULT_FRAMES
        print("Frames :",frames)
    if keys[pygame.K_2]:
        frames = 2 * DEFAULT_FRAMES
        print("Frames :",frames)
    if keys[pygame.K_3]:
        frames = 3 * DEFAULT_FRAMES
        print("Frames :",frames)
    if keys[pygame.K_4]:
        frames = 4 * DEFAULT_FRAMES
        print("Frames :",frames)
    if keys[pygame.K_5]:
        frames = 5 * DEFAULT_FRAMES
        print("Frames :",frames)
    if keys[pygame.K_6]:
        frames = 6 * DEFAULT_FRAMES
        print("Frames :",frames)
    if keys[pygame.K_7]:
        frames = 7 * DEFAULT_FRAMES
        print("Frames :",frames)
    if keys[pygame.K_8]:
        frames = 8 * DEFAULT_FRAMES
        print("Frames :",frames)
    if keys[pygame.K_9]:
        frames = 9 * DEFAULT_FRAMES
        print("Frames :",frames)
    ball_x += ball_dx
    ball_y += ball_dy
    if ball_x - ball_radius <= 0 or ball_x + ball_radius >= WIDTH:
        ball_dx *= -1
    if ball_y - ball_radius <= 0 or ball_y + ball_radius >= HEIGHT:
        ball_dy *= -1
    locs.append((ball_x,ball_y))
    screen.fill(bg_color)
    loc_draws(locs,screen,ball_radius,light_color)
    for i in range(1,len(locs)):
        x,y = locs[i]
        lx,ly = locs[i-1]
        x_l = list_from_to_generation(lx,x)
        y_l = list_from_to_generation(ly,y)
        coords = coordinate_pairing_merger(x_l,y_l)
        loc_draws(coords,screen,ball_radius,light_color)
    pygame.draw.circle(screen,light_color,(ball_x,ball_y),ball_radius)
    pygame.display.flip()
    clock.tick(frames)