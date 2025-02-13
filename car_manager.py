from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]

class CarManager:

    def __init__(self):
        self.all_cars = []
        self.STARTING_MOVE_DISTANCE = 5
        self.MOVE_INCREMENT = 10

    def generate_car(self):
        new_car = Turtle("square")
        new_car.penup()
        new_car.shapesize(stretch_len=2, stretch_wid=1)
        new_car.color(random.choice(COLORS))
        new_car.goto(280, random.randint(-250, 250))
        self.all_cars.append(new_car)

    def move(self):
        for car in self.all_cars:
            car.goto(car.xcor() - self.STARTING_MOVE_DISTANCE, car.ycor())

    def increase_speed(self):
        self.STARTING_MOVE_DISTANCE += self.MOVE_INCREMENT