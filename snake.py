from turtle import Turtle

S_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_1 = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

Box = []


class Snake:

    def __init__(self):
        self.Box = []
        self.create_game()
        self.head = self.Box[0]

    def create_game(self):
        for Position in S_POSITION:
            self.add_Box(Position)

    def add_Box(self, Position):
        Box2 = Turtle("square")
        Box2.color("white")
        Box2.penup()
        Box2.goto(Position)
        self.Box.append(Box2)

    def extend(self):
        self.add_Box(self.Box[-1].position())

    def move(self):
        for B in range(len(self.Box) - 1, 0, -1):
            x = self.Box[B - 1].xcor()
            y = self.Box[B - 1].ycor()
            self.Box[B].goto(x, y)
        self.head.forward(MOVE_1)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
