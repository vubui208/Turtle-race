import turtle as t
import random as r
import time as v

# Setup screen
s = t.Screen()
s.setup(500, 800)
s.bgcolor("black")
s.tracer(0)
t.setworldcoordinates(-250, -400, 250, 400)

# Score display turtles
t_score = t.Turtle()
t_high = t.Turtle()
t_score.hideturtle()
t_high.hideturtle()
t_score.penup()
t_high.penup()
t_score.pencolor("cyan")
t_high.pencolor("cyan")
t_score.goto(-250, 370)
t_high.goto(-250, 330)

# Game info turtles
t0 = t.Turtle()
t0.hideturtle()
t0.penup()
t0.pencolor("green")
t7 = t.Turtle()
t8 = t.Turtle()
t7.hideturtle()
t8.hideturtle()
t7.penup()
t8.penup()
t7.pencolor("cyan")
t8.pencolor("cyan")

# Player turtle
t1 = t.Turtle()
t1.shape("turtle")
t1.fillcolor("blue")
t1.penup()
t1.goto(0, -390)
t1.setheading(90)

# Obstacle base turtle
t2 = t.Turtle()
t2.shape("square")
t2.fillcolor("red")
t2.penup()
t2.hideturtle()

# Clone obstacles
t3 = t2.clone()
t4 = t2.clone()
t5 = t2.clone()
t6 = t2.clone()
for obs in [t3, t4, t5, t6]:
    obs.penup()
    obs.hideturtle()

# Globals
score = 0
highest_score = 0
what = 0
colors = ("yellow", "red", "green")
lights_pos = (100,300, -20)

# Traffic light turtle
traffic_light_turtle = t.Turtle()
traffic_light_turtle.hideturtle()
traffic_light_turtle.penup()
traffic_light_turtle.speed(0)

# Functions
def show_traffic_light(i):
    traffic_light_turtle.clear()
    traffic_light_turtle.goto(lights_pos[i % 3]-150, 100)
    traffic_light_turtle.fillcolor(colors[i % 3])
    traffic_light_turtle.pencolor(colors[i % 3])
    traffic_light_turtle.pendown()
    traffic_light_turtle.begin_fill()
    traffic_light_turtle.circle(30)
    traffic_light_turtle.end_fill()
    traffic_light_turtle.penup()
    s.update()
    v.sleep(1)

def countdown():
    for i in range(5, 0, -1):
        show_traffic_light(5 - i)
        t0.write(i, align="center", font=("Arial", 30, "normal"))
        s.update()
        v.sleep(1)
        t0.clear()
    show_traffic_light(3)
    t0.write("GO", align="center", font=("Arial", 30, "normal"))
    s.update()
    v.sleep(1)
    t0.clear()
    traffic_light_turtle.clear()

def move_obstacle(obs):
    if obs.ycor() > -400:
        obs.sety(obs.ycor() - r.uniform(0.01, 1))
    else:
        obs.hideturtle()
        obs.goto(r.randint(-220, 220), 400)
        obs.showturtle()

def collision(player, obs):
    global what
    if abs(player.xcor() - obs.xcor()) < 25 and abs(player.ycor() - obs.ycor()) < 25:
        what = 1

def update_score_display():
    t_score.clear()
    t_score.write(f"SCORE: {score}", font=("Arial", 15, "normal"))
    t_high.clear()
    t_high.write(f"HIGHEST SCORE: {highest_score}", font=("Arial", 15, "normal"))

def reset_obstacle(obs):
    obs.goto(r.randint(-220, 220), 400)
    obs.showturtle()

def increase_score(obs):
    global score, highest_score
    if obs.ycor() <= -400:
        reset_obstacle(obs)
        score += 1
        if score > highest_score:
            highest_score = score
        update_score_display()

def game_over():
    t1.hideturtle()
    for obs in [t2, t3, t4, t5, t6]:
        obs.hideturtle()
    t0.goto(-175, 0)
    t0.write("GAME OVER", font=("Arial", 40, "normal"))
    t7.goto(-40, -100)
    t7.write(f"SCORE: {score}", font=("Arial", 15, "normal"))
    t8.goto(-90, -150)
    t8.write(f"HIGHEST SCORE: {highest_score}", font=("Arial", 15, "normal"))
    t0.sety(-300)
    t0.write("PRESS SPACE TO TRY AGAIN", font=("Arial", 20, "normal"))
    s.update()

def reset_game():
    global what, score
    what = 0
    score = 0
    t7.clear()
    t8.clear()
    t0.clear()
    update_score_display()
    t1.goto(0, -390)
    t0.goto(0, 0)
    t1.showturtle()
    for obs in [t2, t3, t4, t5, t6]:
        reset_obstacle(obs)

def handle_space():
    global what
    if what == 1:
        what = 0

# Movement
s.onkeypress(lambda: t1.sety(t1.ycor() + 20 if t1.ycor() < 390 else 390), "Up")
s.onkeypress(lambda: t1.sety(t1.ycor() - 20 if t1.ycor() > -390 else -390), "Down")
s.onkeypress(lambda: t1.setx(t1.xcor() + 20 if t1.xcor() < 240 else 240), "Right")
s.onkeypress(lambda: t1.setx(t1.xcor() - 20 if t1.xcor() > -240 else -240), "Left")
s.onkeypress(handle_space, "space")
s.listen()

# Game loop
while True:
    if what == 0:
        reset_game()
        countdown()  # ensure countdown runs before game loop
        while what == 0:
            for obs in [t2, t3, t4, t5, t6]:
                move_obstacle(obs)
                increase_score(obs)
                collision(t1, obs)
            update_score_display()
            s.update()
    else:
        game_over()

t.done()
