import random
from turtle import Turtle, Screen


screen = Screen()
turtle_one = Turtle()
turtle_two = Turtle()
turtle_three = Turtle()
turtle_four = Turtle()

choice = screen.textinput(title="Place your bets!", prompt="Which turtle will you place your bet on?")
colours = ["red", "blue", "green", "yellow"]
y_startingpoints = [-100,-150,-200,-250]
turtles=[]
for i in range (0,4):
    turtle = Turtle(shape="turtle")
    turtle.penup()
    turtle.color(colours[i])
    turtle.goto(x=-200, y = y_startingpoints[i])
    turtle.pendown()
    turtles.append(turtle)

race = True
while(race):
    for turtle in turtles:
        if (turtle.xcor() >= 200):
            race = False
            win = turtle.pencolor()
            if (win == choice):
                print("you won!")
            else:
                print("you lost...")

        turtle.forward(random.randint(0,10))

screen.exitonclick()
