from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self) -> None:
        self.all_cars=[]
    def create_cars(self):
        random_num=random.randint(1,6)
        if random_num==1 :
            new_car=Turtle('square')
            new_car.shapesize(1,2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y=random.randint(-250,250)
            new_car.goto(300,random_y)
            self.all_cars.append(new_car)
    def move_cars(self):
        for car in self.all_cars:
            car.backward(STARTING_MOVE_DISTANCE)
    def speed_cars(self):
        for car in self.all_cars:
            car.backward(STARTING_MOVE_DISTANCE+5)
