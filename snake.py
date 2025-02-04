from turtle import Turtle


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        x_modifier = 0

    def create_snake(self):
        x_modifier = 0
        for position in range(3):
            tim = Turtle("square")
            tim.shapesize(0.7, 0.7)
            tim.penup()
            tim.color("white")
            tim.goto(x_modifier, 0)
            x_modifier -= 15
            self.segments.append(tim)

    def extend(self):
        new_seg = Turtle("square")
        new_seg.shapesize(0.7, 0.7)
        new_seg.penup()
        new_seg.color("white")
        new_seg.goto(self.segments[-1].xcor(), self.segments[-1].ycor())
        self.segments.append(new_seg)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def move(self):
        for new_seg in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[new_seg - 1].xcor()
            new_y = self.segments[new_seg - 1].ycor()
            self.segments[new_seg].goto(new_x, new_y)
        if self.head.xcor() > 290:
            self.head.setx(-290)
        elif self.head.xcor() < -290:
            self.head.setx(290)
        if self.head.ycor() > 290:
            self.head.sety(-290)
        elif self.head.ycor() < -290:
            self.head.sety(290)

        self.head.forward(15)

    def up(self):
        if self.head.heading() != 270:
            self.segments[0].setheading(90)

    def left(self):
        if self.head.heading() != 0:
            self.segments[0].setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.segments[0].setheading(0)

    def down(self):
        if self.head.heading() != 90:
            self.segments[0].setheading(270)
