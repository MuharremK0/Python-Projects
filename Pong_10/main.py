from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen=Screen()
screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.title("Pong")
screen.tracer(0)

#Paddle objects
paddle1=Paddle(350,0)
paddle2=Paddle(-350,0)
ball=Ball()
scoreboard=Scoreboard()

#Paddle controller
screen.listen()
screen.onkey(paddle1.go_up,"Up")
screen.onkey(paddle1.go_down,"Down")
screen.onkey(paddle2.go_up,"w")
screen.onkey(paddle2.go_down,"s")

game_is_on=True
while(game_is_on):
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    
    if (ball.ycor() > 280 or ball.ycor() < -280):
         ball.bounce_y()
    
    if(ball.distance(paddle1) < 50 and ball.xcor() > 320
       or ball.distance(paddle2) < 50 and ball.xcor() < -320):
         ball.bounce_x()

    #detect r paddle misses
    if(ball.xcor() > 380):
        ball.reset_position()
        scoreboard.l_point()
    
    #detect l paddle misses
    if(ball.xcor() < -380):
        ball.reset_position()
        scoreboard.r_point()
screen.exitonclick()