import math
import random
import turtle 
import time 
from turtle import Turtle, Screen
from random import randint

screen = Screen()
t = Turtle('turtle')
t.speed(-1)
t.width(5)


colors = ['red', 'green', 'blue', 'purple', 'yellow', 'orange', 'black']

def penup():
	t.penup()

def pendown():
	t.pendown()

def dragging(x, y):
	t.ondrag(None)
	t.setheading(t.towards(x, y))
	t.goto(x,y)                         														   #  only draw if the mouse is clicked 
	t.ondrag(dragging)
	 # if you continue it will continue to call this function

def clickright(x, y):
	t.clear()

def placecircle(x, y):
	t.begin_fill()
	t.circle(20)
	t.end_fill()

def colorswap():
	t.color(random.choice(colors))

def eraser():
	t.color('White')

def main():
	turtle.listen()

	t.ondrag(dragging)

	turtle.onscreenclick(clickright, 3)
	turtle.onscreenclick(placecircle, 2)
	turtle.onkey(colorswap, 'Left')
	turtle.onkey(penup, "Up")
	turtle.onkey(pendown, 'Down')
	turtle.onkey(eraser, 'e')
	


	screen.mainloop()

main()

 
#right click is clear
# middle click is insert circle
# left click is draw
# up is pen up
# down is pen down
# left is change color
# e is eraser
