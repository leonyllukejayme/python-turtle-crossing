from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    
    def __init__(self):
        self.all_cars = []
        self.car_speed = 0.1

    def create_car(self):
        random_chance = random.randint(1,8)
        if random_chance == 1:
            new_car = Turtle('square')
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.shapesize(stretch_len=2,stretch_wid=1)
            random_y = random.randint(-230,230)
            new_car.goto(320,random_y)
            self.all_cars.append(new_car)

        
    def move(self):
        for car in self.all_cars:
            car.backward(STARTING_MOVE_DISTANCE)

    def inc_speed(self):
        if self.car_speed >= 0.05:
            self.car_speed -= 0.01
