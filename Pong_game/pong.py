import turtle 
import os

wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width = 800, height = 600)
wn.tracer(0)

#score
score_1 = 0
score_2 = 0

#paddle a
paddle_a =  turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)


#paddle_b
paddle_b =  turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

#ball
ball =  turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = 0.5
ball.dy = -0.5

#pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player 1: 0   Player 2: 0", align = "center", font = ("Courier", 24, "normal"))
pen.goto(0, -290)
pen.write("Player 1 w = up, s = down     Player 2 up key = up, down key = down", align = "center", font = ("Courier", 10, "normal"))
pen.goto(0, 260)

#functions
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)
def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

#keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)
def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

#keyboard binding
wn.listen()
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

#Main group loop
while True:
        wn.update()

        #Move the ball
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)

        #border checking
        if ball.ycor() > 290:
            ball.sety(290)
            ball.dy *= -1

        if ball.ycor() < -290:
            ball.sety(-290)
            ball.dy *= -1

        if ball.xcor() > 390:
            ball.goto(0, 0)
            ball.dx *= -1
            score_1 += 1
            pen.clear()
            pen.write("Player 1: {}   Player 2: {}".format(score_1, score_2), align = "center", font = ("Courier", 24, "normal"))

        if ball.xcor() < -390:
            ball.goto(0, 0)
            ball.dx *= -1
            score_2 += 1
            pen.clear()
            pen.write("Player 1: {}   Player 2: {}".format(score_1, score_2), align = "center", font = ("Courier", 24, "normal"))

        #collision with paddles
        if ball.xcor() > 340 and ball.xcor() < 350 and ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() -50:
            ball.setx(340)
            ball.dx *= -1

        if ball.xcor() < -340 and ball.xcor() > -350 and ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() -50:
            ball.setx(-340)
            ball.dx *= -1


        