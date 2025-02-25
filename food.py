import random
from turtle import Turtle


class Food(Turtle):
    '''Controls food position'''

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("purple")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        '''Changes food position'''
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
