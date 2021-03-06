# Simple Pong in Python 3 for Beginners
# Tutorial by @TokyoEdTech
# Written by TheTrueOryx

import turtle
import winsound

#Constants
SCNWID = 800
SCNHGT = 600
PADDLELOC = SCNWID/2*0.875
PADDLESPD = 20
BALLSPD = 0.5

#Variables
score_a = 0
score_b = 0

#Defining the window
wn = turtle.Screen() #Screen Object
wn.title("Pong by TheTrueOryx") #Title
wn.bgcolor("black") #Background Color 
wn.setup(width=SCNWID, height=SCNHGT) #Size of window
wn.tracer(0) #Update frequency - set to zero so that it can be updated during gameplay

#Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0) #Speed of animation
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5,stretch_len=1)
paddle_a.penup() #Do not draw a line as the object moves
paddle_a.goto(-PADDLELOC,0) #inital location from center

#Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0) #Speed of animation
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
paddle_b.penup() #Do not draw a line as the object moves
paddle_b.goto(PADDLELOC,0) #inital location from center

#Ball
ball = turtle.Turtle()
ball.speed(0) #Speed of animation
ball.shape("square")
ball.color("white")
ball.penup() #Do not draw a line as the object moves
ball.goto(0,0) #inital location from center
ball.dx = BALLSPD
ball.dy = BALLSPD

# Pen (Score)
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,SCNHGT/2*12/15)
pen.write("Player A: {}   Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

#Movement Function
def paddle_a_up():
    y = paddle_a.ycor() #Use .ycor() to get paddle_a's y coordinate
    y += PADDLESPD
    paddle_a.sety(y) #Set paddle_a's y coordinate to the new value

def paddle_a_down():
    y = paddle_a.ycor() #Use .ycor() to get paddle_a's y coordinate
    y -= PADDLESPD
    paddle_a.sety(y) #Set paddle_a's y coordinate to the new value

def paddle_b_up():
    y = paddle_b.ycor() #Use .ycor() to get paddle_b's y coordinate
    y += PADDLESPD
    paddle_b.sety(y) #Set paddle_b's y coordinate to the new value

def paddle_b_down():
    y = paddle_b.ycor() #Use .ycor() to get paddle_b's y coordinate
    y -= PADDLESPD
    paddle_b.sety(y) #Set paddle_b's y coordinate to the new value

#Keyboard binding
wn.listen() #Listen for input
wn.onkeypress(paddle_a_up,"w") #When "w" is pressed, do paddle_a_up    
wn.onkeypress(paddle_a_down,"s") #When "s" is pressed, do paddle_a_down 
wn.onkeypress(paddle_b_up,"Up") #When "Up" is pressed, do paddle_b_up    
wn.onkeypress(paddle_b_down,"Down") #When "Down" is pressed, do paddle_b_down 

#Main game loop
while True:
    wn.update()

    #Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #Border checking
    if ball.ycor() > SCNHGT/2-10:
        ball.sety(SCNHGT/2-10)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if ball.ycor() < -SCNHGT/2+10:
        ball.sety(-SCNHGT/2+10)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if ball.xcor() > SCNWID/2-10:
        ball.goto(0,0)
        ball.dx *= -1
        score_a += 1
        pen.clear() #Clear the screen
        pen.write("Player A: {}   Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal")) #write updated score

    if ball.xcor() < -SCNWID/2+10:
        ball.goto(0,0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}   Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    #Paddle and ball collisions
    if (ball.xcor() > PADDLELOC-10 and ball.xcor() < PADDLELOC) and (ball.ycor() < paddle_b.ycor()+50 and ball.ycor() > paddle_b.ycor()-50):
        ball.setx(PADDLELOC-10)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if (ball.xcor() < -PADDLELOC+10 and ball.xcor() > -PADDLELOC) and (ball.ycor() < paddle_a.ycor()+50 and ball.ycor() > paddle_a.ycor()-50):
        ball.setx(-PADDLELOC+10)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
