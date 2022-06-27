# Simple Pong in Python 3 for Beginners
# Tutorial by @TokyoEdTech
# Written by TheTrueOryx

import turtle

#Defining the window
wn = turtle.Screen() #Screen Object
wn.title("Pong by TheTrueOryx") #Title
wn.bgcolor("black") #Background Color 
wn.setup(width=800, height=600) #Size of window
wn.tracer(0) #Update frequency - set to zero so that it can be updated during gameplay

#Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0) #Speed of animation
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5,stretch_len=1)
paddle_a.penup() #Do not draw a line as the object moves
paddle_a.goto(-350,0) #inital location from center

#Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0) #Speed of animation
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
paddle_b.penup() #Do not draw a line as the object moves
paddle_b.goto(350,0) #inital location from center

#Ball
ball = turtle.Turtle()
ball.speed(0) #Speed of animation
ball.shape("square")
ball.color("white")
ball.penup() #Do not draw a line as the object moves
ball.goto(0,0) #inital location from center

#Movement Function
def paddle_a_up():
    y = paddle_a.ycor() #Use .ycor() to get paddle_a's y coordinate
    y += 20
    paddle_a.sety(y) #Set paddle_a's y coordinate to the new value

def paddle_a_down():
    y = paddle_a.ycor() #Use .ycor() to get paddle_a's y coordinate
    y -= 20
    paddle_a.sety(y) #Set paddle_a's y coordinate to the new value

def paddle_b_up():
    y = paddle_b.ycor() #Use .ycor() to get paddle_b's y coordinate
    y += 20
    paddle_b.sety(y) #Set paddle_b's y coordinate to the new value

def paddle_b_down():
    y = paddle_b.ycor() #Use .ycor() to get paddle_b's y coordinate
    y -= 20
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
