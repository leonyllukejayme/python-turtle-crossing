import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title('Turtle Crossing Game')
screen.cv._rootwindow.resizable(False,False)
screen.tracer(0)

player = Player()

car = CarManager()

scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move,'space')

game_is_on = True
while game_is_on:
    time.sleep(car.car_speed)
    screen.update()
    car.create_car()
    car.move()

    # Detect Collosion with cars
    for c in car.all_cars:
        if c.distance(player) < 30:
            game_is_on = False
            scoreboard.game_over()
    
    # Turtle reach the other side
    if player.ycor() >= 280:
        player.reset()
        car.inc_speed()
        scoreboard.increase_level()


screen.mainloop()