from turtle import Turtle
from csv_helper import CsvHelper

class Writer(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.csv_helper = CsvHelper()

    def write_answer(self, answer):
        coordinates = self.csv_helper.get_x_y(answer)
        self.goto(coordinates)
        self.write(arg=answer, align="left")