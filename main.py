import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player=Player()
Car_Manager=CarManager()
score_board=Scoreboard()
screen.listen()
screen.onkey(player.up,'Up')
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    Car_Manager.create_cars()
    Car_Manager.move_cars()
    

    for car in Car_Manager.all_cars:
        if  car.distance(player)<20:
            score_board.game_over()
            game_is_on=False

    
    if player.finish():
        player.go_to_start()
        Car_Manager.speed_cars()
        score_board.update_score()

screen.exitonclick()