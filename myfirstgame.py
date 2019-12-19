#this imports a turtle
import turtle 

#lets use the Macos system
import os

# Makes a window
window = turtle.Screen()

#makes the name of the window
window.title("My First Game")
window.bgcolor("#000000")
window.setup(width=800, height=600)

#window does not update by it's self
window.tracer(0)

#the ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("#FFFFFF")
ball.penup()
ball.goto(0, 0)
ball.dx = 2
ball.dy = 2

#score
score_1 = 0
score_2 = 0

#the way the ball is moving
drectionx = 1
drectiony = 1

#the bat 1 (left)
bat_1 = turtle.Turtle()
bat_1.speed(0)
bat_1.shape("square")
bat_1.color("#FFFFFF")
bat_1.shapesize(stretch_wid=5, stretch_len=1)
bat_1.penup()
bat_1.goto(-350, 0)

#the bat 2 (right)
bat_2 = turtle.Turtle()
bat_2.speed(0)
bat_2.shape("square")
bat_2.color("#FFFFFF")
bat_2.shapesize(stretch_wid=5, stretch_len=1)
bat_2.penup()
bat_2.goto(350, 0)

#Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("#FFFFFF")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("player 1's points: 0 	player 2's points: 0", align="center", font=("Courtier", 24, "normal"))

#function
def bat_1_up():
	y = bat_1.ycor()
	y += 30
	bat_1.sety(y)
def bat_1_down():
	y = bat_1.ycor()
	y -= 30
	bat_1.sety(y)
def bat_2_up():
	y = bat_2.ycor()
	y += 30
	bat_2.sety(y)
def bat_2_down():
	y = bat_2.ycor()
	y -= 30
	bat_2.sety(y)
def write_score():
	pen.write("player 1's points: {} 	player 2's points: {}".format(score_1, score_2), align="center", font=("Courtier", 24, "normal"))

#keyborad binding
window.listen()
window.onkeypress(bat_1_up, "w")
window.onkeypress(bat_1_down, "s")
window.onkeypress(bat_2_up, "Up")
window.onkeypress(bat_2_down, "Down")
window.onkeypress(turtle.bye,"Escape")

#main game loop
while True:
	window.update()

	#move the ball
	ball.setx(ball.xcor() + ball.dx)
	ball.sety(ball.ycor() + ball.dy)


	#border check/bounce
	if ball.ycor() > 290:
		ball.sety(290)
		ball.dy *= -1
		os.system("afplay pong_bounce.wav&")
		drectiony *= -1

	if ball.ycor() < -290:
		ball.sety(-290)
		ball.dy *= -1
		os.system("afplay pong_bounce.wav&")
		drectiony *= -1

	if ball.xcor() > 390:
		ball.goto(0, 0)
		ball.dx *= -1
		score_1 += 1
		pen.clear()
		write_score()
		drectionx *= -1
		drectiony *= -1

	if ball.xcor() < -390:
		ball.goto(0, 0)
		ball.dx *= -1
		score_2 += 1
		pen.clear()
		write_score()
		drectionx *= -1
		drectiony *= -1

	#bat and ball collisions
	if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < bat_2.ycor() + 40 and ball.ycor() > bat_2.ycor() - 40):
		ball.setx(340)
		ball.dx *= -1
		os.system("afplay pong_bounce.wav&")
		drectionx *= -1

	if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < bat_1.ycor() + 40 and ball.ycor() > bat_1.ycor() - 40):
		ball.setx(-340)
		ball.dx *= -1
		os.system("afplay pong_bounce.wav&")
		drectionx *= -1

	if (drectionx < 0):
		ball.dx -= 0.001
	if (drectiony < 0):		
		ball.dy -= 0.001
	if (drectionx > 0):
		ball.dx += 0.001
	if (drectiony > 0):
		ball.dy += 0.001
	if (score_1 > 9):
		pen.clear
		pen.goto(0, 10)
		pen.write("Player 1 Wins The Game!", align="center", font=("Courtier", 24, "normal"))
		ball.dx = 0
		ball.dy = 0
	if (score_2 > 9):
		pen.clear
		pen.goto(0, 10)
		pen.write("Player 2 Wins The Game!", align="center", font=("Courtier", 24, "normal"))
		ball.dx = 0
		ball.dy = 0
# Keeps it open (the end of the program)
window.mainloop()
