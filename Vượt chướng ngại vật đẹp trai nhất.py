import turtle as t
import random as r
import time as v
s=t.Screen()
t7 = t.Turtle()
t8 = t.Turtle()
t0 = t.Turtle()
t1 = t.Turtle()
t2 = t.Turtle()
t.tracer(1)
t.setup(500,800)
t.bgcolor("black")
t.setworldcoordinates(-250,-400,250,400)
tx=t.Turtle()
tx.hideturtle()
tz=t.Turtle()
tz.hideturtle()
tz.penup()
t0.hideturtle()
t1.shape("turtle")
t2.shape("square")
t2.hideturtle()
t1.fillcolor("blue")
t2.fillcolor("red")
t1.penup()
t1.goto(0,-390)
t1.left(90)
t.hideturtle()
t.penup()
t.goto(-250,370)
t.pencolor("cyan")
tz.pencolor("cyan")
#RÙA IN ĐIỂM
t.write("SCORE :0",font=("arial",15,"normal"))
tz.goto(-250,330)
tz.write("HIGHEST SCORE :0",font=("arial",15,"normal"))
colors = ("yellow", "red", "green")
toa_do = (25, 70, -20)
t7.penup()
t8.penup()
t0.home()
t8.pencolor("cyan")
t7.pencolor("cyan")
t0.pencolor("green")
t7.hideturtle()
t8.hideturtle()

#TẠO CHƯỚNG NGẠI VẬT
t2.penup()
#t2.goto(r.randint(-220,220),400)
#t2.showturtle()
t3=t2.clone()
t3.hideturtle()
t3.penup()
#t3.goto(r.randint(-220,220),400)
#t3.showturtle()
t4=t2.clone()
t4.penup()
t4.hideturtle()
#t4.goto(r.randint(-220,220),400)
#t4.showturtle()
t5=t2.clone()
t5.penup()
t5.hideturtle()
#t5.goto(r.randint(-220,220),400)
#t5.showturtle()
t6=t2.clone()
t6.penup()
t6.hideturtle()

t.tracer(3)
score = 0
#TẠO ĐÈN GIAO THÔNG
def dengiaothong(i):
    tx.speed(0)
    tx.fillcolor(colors[i % 3])
    tx.pencolor(colors[i % 3])
    tx.penup()
    tx.goto(toa_do[i % 3], 300)
    tx.pendown()
    tx.begin_fill()
    tx.circle(30)
    tx.end_fill()
    v.sleep(1)
    tx.clear()
#ĐẾM NGƯỢC THỜI GIAN
def countdown():
    for i in range(5, 0, -1):
        t0.write(i, move=False, align="center", font=("Arial", 30, "normal"))
        v.sleep(1)
        t0.clear()
    t0.write("GO", move=False, align="center", font=("Arial", 30, "normal"))
    v.sleep(1)
    t0.clear()
def chuongngaivat(tenconrua):
        global score
        if tenconrua.ycor() > -400:
            tenconrua.sety(tenconrua.ycor() - r.uniform(0.01, 1))
        elif tenconrua.ycor() <= -400:
          tenconrua.hideturtle()
          tenconrua.goto(r.randint(-220, 220), 400)
          tenconrua.showturtle()
def vacham(nguoichoi, vatcan):
    global what
    if nguoichoi.xcor() < vatcan.xcor() + 25 and nguoichoi.ycor() < vatcan.ycor() + 25 and nguoichoi.xcor() > vatcan.xcor() - 25 and nguoichoi.ycor() > vatcan.ycor() - 25:
        what = 1
        return what
def dilen():
    if t1.ycor() < 390:
        t1.sety(t1.ycor() + 20)
def dixuong():
    if (t1.ycor() > -390):
        t1.sety(t1.ycor() - 20)
def quaphai():
    if t1.xcor() < 240:
        t1.setx(t1.xcor() + 20)
def quatrai():
    if (t1.xcor() > -240):
        t1.setx(t1.xcor() - 20)
def thuaroi():
    global higest_score
    t1.hideturtle()
    t2.hideturtle()
    t3.hideturtle()
    t4.hideturtle()
    t5.hideturtle()
    t6.hideturtle()
    if higest_score < score:
       higest_score = score
    t.clear()
    tz.clear()
    t0.penup()
    t0.goto(-175, 0)
    t0.write("GAME OVER", font=("airal", 40, "normal"))
    t7.goto(-40, -100)
    t7.write("SCORE: " + str(score), font=("arial", 15, "normal"))
    t8.goto(-90, -150)
    t8.write("HIGHEST SCORE :" + str(higest_score), font=("arial", 15, "normal"))
    t0.sety(-300)
    t0.write("PRESS SPACE TO TRY AGAIN", font=("airal", 20, "normal"))
    s.update()
def choilai():
    global what
    what = 0
    return what

def xoagame():
    t0.clear()
    t.clear()
    tz.clear()
def gobacktoyourshit(chuongngaivat):
    chuongngaivat.penup()
    chuongngaivat.goto(r.randint(-220,220),400)
def tinhdiem(chuongngaivat):
    global score
    global higest_score

    if higest_score < score:
        higest_score = score
    if chuongngaivat.ycor() <= -400:
       chuongngaivat.goto(r.randint(-220,220),400)
       score = score + 1
       t.clear()
       t.write("SCORE: " + str(score), font=("arial", 15, "normal"))

s.onkeypress(dilen,"Up")
s.onkeypress(dixuong,"Down")
s.onkeypress(quaphai,"Right")
s.onkeypress(quatrai,"Left")
s.onkeypress(choilai,"space")
s.listen()
what = 0
higest_score = 0
while True:
    if what == 0:
       t7.clear()
       t8.clear()
       if higest_score < score:
          higest_score = score
       score = 0
       xoagame()
       t1.showturtle()
       t2.showturtle()
       t3.showturtle()
       t4.showturtle()
       t5.showturtle()
       t6.showturtle()
       gobacktoyourshit(t2)
       gobacktoyourshit(t3)
       gobacktoyourshit(t4)
       gobacktoyourshit(t5)
       gobacktoyourshit(t6)
       t.goto(-250, 370)
       t.clear()
       t.write("SCORE: " + str(score), font=("arial", 15, "normal"))
       tz.goto(-250, 330)
       tz.clear()
       tz.write("HIGHEST SCORE :" + str(higest_score), font=("arial", 15, "normal"))
       t1.goto(0,-390)
       s.tracer(0)
       t0.home()
       countdown()
       while what == 0:
           s.update()
           chuongngaivat(t2)
           chuongngaivat(t3)
           chuongngaivat(t4)
           chuongngaivat(t5)
           chuongngaivat(t6)
           tinhdiem(t2)
           tinhdiem(t3)
           tinhdiem(t4)
           tinhdiem(t5)
           tinhdiem(t6)
           vacham(t1, t2)
           vacham(t1, t3)
           vacham(t1, t4)
           vacham(t1, t5)
           vacham(t1, t6)
           if higest_score < score:
               higest_score = score
           tz.clear()
           tz.write("HIGHEST SCORE :" + str(higest_score), font=("arial", 15, "normal"))
           s.update()
    if what == 1:
        thuaroi()


t.done()





