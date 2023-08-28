from turtle import Turtle

STARTING_POSITION=(0,-200)
MOVE_DISTANCE=10
FINISH_LINE_Y=200

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("white")
        self.penup()
        self.go_to_start()
        self.setheading(90)


    def up(self):
        self.goto(self.xcor(),self.ycor()+MOVE_DISTANCE)

    def down(self):
        self.goto(self.xcor(),self.ycor()-MOVE_DISTANCE)
    
    def is_at_finish_line(self):
       return self.ycor() > FINISH_LINE_Y

    def go_to_start(self):
        self.goto(STARTING_POSITION)