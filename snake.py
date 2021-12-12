from turtle import Turtle
MOVEDISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    """Create a snake to begin the game"""
    def __init__(self):
        self.segments = []
        self.num_segments = 3
        self.x = [0, -20, -40]
        for i in range(self.num_segments):
            segment = Turtle("square")
            segment.color("white")
            segment.penup()
            segment.setx(self.x[i])
            self.segments.append(segment)
        self.head = self.segments[0]
        self.tail = self.segments[1:]


    def move(self):
        for segment in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[segment-1].xcor()
            new_y = self.segments[segment-1].ycor()
            self.segments[segment].goto(new_x, new_y)
        self.segments[0].forward(MOVEDISTANCE)


    def up(self):
        if self.head.heading() != DOWN:
            self.head.seth(UP)


    def down(self):
        if self.head.heading() != UP:
            self.head.seth(DOWN)


    def left(self):
        if self.head.heading() != RIGHT:
            self.head.seth(LEFT)


    def right(self):
        if self.head.heading() != LEFT:
            self.head.seth(RIGHT)


    def new_segment(self):
        segment = Turtle("square")
        segment.color("white")
        segment.penup()
        self.segments.append(segment)
        self.move()
        self.tail = self.segments[1:]
