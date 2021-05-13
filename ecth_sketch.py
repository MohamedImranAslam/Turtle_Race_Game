from turtle import Turtle,Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width = 500,height = 400)
user_bet = screen.textinput(title="Make your bet",prompt="Which turtle will win the race? Enter the color:" )
colors = ["red","blue","yellow","green","orange","black"]
y_axis = [-70,-40,-10,20,50,80]
all_turtles = []

for turtle_index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x = -230, y = y_axis[turtle_index])
    all_turtles.append(new_turtle)
print(all_turtles)
if user_bet:
    is_race_on = True
while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"you've won. The {winning_color} is the winner")
            else:
                print(f"you've Lost. The {winning_color} is the winner")
        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)

screen.exitonclick()