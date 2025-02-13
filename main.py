import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
loop_count = 1
level = 6

player = Player()
cars = CarManager()
score = Scoreboard()

screen.listen()
screen.onkeypress(player.go_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    if loop_count % (level - 1) == 0:
        cars.generate_car()

    cars.move()

    loop_count += 1

    for car in cars.all_cars:
        if player.distance(car) < 20:
            game_is_on = False
            score.game_over()

    if player.is_at_finish():
        score.level += 1
        player.increase_level()
        cars.increase_speed()
        level -= 1
        score.update_score()

screen.exitonclick()