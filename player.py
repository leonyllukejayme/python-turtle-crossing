from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 20
FINISH_LINE_Y = 280


class Player(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.setheading(90)
        self.reset()

    def move(self):
        self.new_y = self.ycor() + MOVE_DISTANCE
        if self.ycor() < FINISH_LINE_Y:
            self.goto(self.xcor(),self.new_y)

    def reset(self):
        self.goto(STARTING_POSITION)
