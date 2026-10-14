#Christine Gilbert
#10/11/2026
#draw a house and a star in the sky
#import turtle
import turtle
#make the screen and turtle name and set all the colors
screen = turtle.Screen()
t = turtle.Turtle()
screen.title("Christine Gilbert")
screen.bgcolor("blue")
t.color("gold")
t.pencolor("white")
t.fillcolor("firebrick")
t.pensize(7)
t.speed(1)
# lines drawn = 4 walls + 3 roof + 5 stars
#make the house
t.begin_fill()
for side in range(4):
    t.forward(200)
    t.left(90)
t.end_fill()

t.penup()
t.goto(0,200)
t.pendown()

sides = 0
t.fillcolor("tan")
t.begin_fill()
while sides < 3:
    t.forward(200)
    t.left(120)
    sides = sides + 1
t.end_fill()

t.penup()
t.goto(300,300)
t.pendown()
t.fillcolor("gold")
t.begin_fill()
for point in range(5):
    t.forward(80)
    t.left(144)
t.end_fill()
