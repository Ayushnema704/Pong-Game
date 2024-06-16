#Simple Pong Game in python using turle

#Game Window Setup
#turtle - module for using basic graphics and making games

import turtle  

wn=turtle.Screen()      
wn.title("Pong Game By Ayush Nema")             
wn.bgcolor("black")
wn.setup(width=1280,height=720)
wn.tracer(0)         #used to set delay in animation

#Score

score_a=0
score_b=0

#Paddle A

paddle_a = turtle.Turtle()
paddle_a.speed(0)     #speed of animation not paddle
paddle_a.shape("square")
paddle_a.shapesize(stretch_wid=7,stretch_len=1)
paddle_a.color("white")
paddle_a.penup()
paddle_a.goto(-600,0)



#Function
def paddle_a_up():
    y=paddle_a.ycor()
    y +=20
    if (y < 290) : 
       y=paddle_a.sety(y)
    
    
def paddle_a_down():
    y=paddle_a.ycor()
    y -=20
    if (y > -290): 
       y=paddle_a.sety(y)

#key Bindings
wn.listen()
wn.onkeypress(paddle_a_up,"w")
wn.onkeypress(paddle_a_down,"s")



#Paddle B

paddle_b = turtle.Turtle()
paddle_b.speed(0)     #speed of animation not paddle
paddle_b.shape("square")
paddle_b.shapesize(stretch_wid=7,stretch_len=1)
paddle_b.color("white")
paddle_b.penup()
paddle_b.goto(600,0)



#Function
def paddle_b_up():
    y=paddle_b.ycor()
    y +=20
    if(y<290):
     y=paddle_b.sety(y)
    
def paddle_b_down():
    y=paddle_b.ycor()
    y -=20
    if(y>-290):
     y=paddle_b.sety(y)
    

#key Bindings
wn.listen()
wn.onkeypress(paddle_b_up,"Up")
wn.onkeypress(paddle_b_down,"Down")

#Ball

ball = turtle.Turtle()
ball.speed(0)     #speed of animation not paddle
ball.shape("circle")
ball.shapesize(stretch_len=1.25,stretch_wid=1.25)
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx=0.25     #moving pixels of ball
ball.dy=0.25

#Pen
pen=turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,310)
pen.write("Player A : 0  Player B : 0", align="center" , font=("Courier","24","normal"))



# Main Game Loop
while True:
    wn.update()         #Every time when the loop runs , it updates the screen

    #move the ball
    
    ball.setx(ball.xcor()+ ball.dx)
    ball.sety(ball.ycor()+ ball.dy)

    #Setting The Borders

    #Ball

    
    # Upward border   s
    
    if ball.ycor() > 310:
       ball.sety(310)
       ball.dy *= -1

    #Downward Border

    if ball.ycor() < -310:
       ball.sety(-310)
       ball.dy *= -1

  
    #Right Border

    if ball.xcor() > 630:
       ball.goto(0,0)
       ball.dx *= -1
       score_a +=1
       pen.clear()
       pen.write("Player A : {}  Player B : {}". format(score_a,score_b), align="center" , font=("Courier","24","normal"))


    #Left Border

    if ball.xcor() < -630:
       ball.goto(0,0)
       ball.dx *= -1
       score_b +=1
       pen.clear()
       pen.write("Player A : {}  Player B : {}". format(score_a,score_b), align="center" , font=("Courier","24","normal"))

    #Ball and Paddle Collisions

    if ball.xcor() > 590 and ball.xcor() < 600 and ( ball.ycor() < paddle_b.ycor() + 70 ) and (ball.ycor() > paddle_b.ycor() -70):
        ball.setx(590)
        ball.dx *= -1 

    if ball.xcor() > -620 and ball.xcor() < -600 and ( ball.ycor() < paddle_a.ycor() + 70) and (ball.ycor() > paddle_a.ycor() - 70):
        ball.setx(-600)
        ball.dx *= -1 
        

