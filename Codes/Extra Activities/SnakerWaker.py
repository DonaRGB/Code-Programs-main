import turtle
import time
import random
screen = turtle.Screen()
screen.title("Snake Game")
bg_color = "black"
screen.bgcolor(bg_color)
scale_factor = 0.75
DIMENSIONS = 1000
WIDTH,HEIGHT = DIMENSIONS * scale_factor,DIMENSIONS * scale_factor
screen.setup(width = WIDTH,height = HEIGHT)
screen.tracer(0)
size = int(15 * scale_factor)
h = turtle.Turtle()
h_shape = "square"
h_color = "lime"
h.shape(h_shape)
h.color(h_color)
h.penup()
h.goto(0,0)
h.direction = "stop"
segs = []
f = turtle.Turtle()
food_shape = "circle"
food_color = "red"
f.shape(food_shape)
f.color(food_color)
f.penup()
f.goto(0,int(100*scale_factor))
score = 0
def go_up():
    if h.direction != "down":
        h.direction = "up"
def go_down():
    if h.direction != "up":
        h.direction = "down"
def go_left():
    if h.direction != "right":
        h.direction = "left"
def go_right():
    if h.direction != "left":
        h.direction = "right"
def move():
    if h.direction == "up":
        y = h.ycor()
        h.sety(y+20*scale_factor)
    elif h.direction == "down":
        y = h.ycor()
        h.sety(y-20*scale_factor)
    elif h.direction == "left":
        x = h.xcor()
        h.setx(x-20*scale_factor)
    elif h.direction == "right":
        x = h.xcor()
        h.setx(x+20*scale_factor)
screen.listen()
screen.onkey(go_up,"Up")
screen.onkey(go_down,"Down")
screen.onkey(go_left,"Left")
screen.onkey(go_right,"Right")
cols = int(WIDTH//2) - size
cels_size = 20
cels = (int(HEIGHT//2) - 1) // cels_size
while True:
    screen.update()
    if h.xcor() > cols or h.xcor() < -cols or h.ycor() > cols or h.ycor() < -cols:
        print("Game Over! Final Score :",score)
        break
    if h.distance(f) < cels_size:
        x = random.randint(-cels,cels) * cels_size
        y = random.randint(-cels,cels) * cels_size
        f.goto(x,y)
        new_seg = turtle.Turtle()
        new_seg.shape(h_shape)
        new_seg.color("green")
        new_seg.penup()
        segs.append(new_seg)
        score += 1
    for i in range(len(segs)-1,0,-1):
        x = segs[i-1].xcor()
        y = segs[i-1].ycor()
        segs[i].goto(x,y)
    if len(segs) > 0:
        x = h.xcor()
        y = h.ycor()
        segs[0].goto(x,y)