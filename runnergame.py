# Infinite runner game prototype

from turtle import *
from time import *

# For calculating angles
from math import *

# Random generation
from random import *

# Constants
grv = 800
speed = 300
framerate = 60
jHeight = 400
bounce = -0.6
scoreRate = 5
speedUpRate = 0.1

# For storing the speeds of objects
# Will store as vectors
speedDict = {}

# For writing text
pen = Turtle()
pen.hideturtle()
pen.penup()

wn = Screen()
wn.bgcolor('#2288CC')
wn.title("Runner Game")
wn.setup(height = 500, width = 800)
wn.tracer(0)
wn.listen()
wn.onkeypress(bye, 'Escape')

sp = speed

class Obj():

	# x and y are STARTING coords
	def __init__(self, color, x, y, length, grav, t):
		self.t = Turtle()
		self.t.penup()
		self.t.color(color)
		self.t.goto(x, y)
		self.t.shape('square'); self.t.shapesize(stretch_len = length);
		self.length = length
		self.x = x; self.y = y
		self.gr = grav; self.ty = t;
		if self.ty == 'obs':
			speedDict[self] = [-sp, 0]
		else:
			speedDict[self] = [0, 0]

	def change_layer(self, layer_num):
		self.y = layer_num*40

	def down(self):
		for obj in speedDict:
			if obj.t.xcor() in range(int((self.t.xcor() - 50)//1), int((self.t.xcor()+51)/1)):
				if obj.t.ycor() in range(-440, int(self.t.ycor()//1)):
					self.t.sety(obj.t.ycor()+20)
					speedDict[self][1] = 0
					return None
		pl.t.sety(pl.t.ycor() - 30)

	# If two entities have collided
	def collided(self, other):
		if abs(other.t.xcor() - self.t.xcor()) > other.length*10:
			return False
		elif abs(other.t.ycor() - self.t.ycor()) > 20:
			return False
		return True

	# For calculating the angle between two objects
	def angle(self, other):

		# NOTE - atan is arctangent.
		try:
			return atan((other.t.ycor() - self.t.ycor())/((other.t.xcor())-(self.t.xcor())))
		except ZeroDivisionError:
			return pi/2

	def upd(self):
		if self != pl and self != bar:
			speedDict[self][0] = -sp

# Obstacles
obsOne = Obj('#FF0000', -270, 100, 4, False, 'obs')
obsTwo = Obj('#FF8000', 370, -150, 5, False, 'obs')
obsThree = Obj('#FFFF00', -430, -50, 4, False, 'obs')
obsFour = Obj('#00A000', 50, 0, 5, False, 'obs')
obsFive = Obj('#0000FF', -110, -100, 4, False, 'obs')
obsSix = Obj('#800080', 210, 150, 5, False, 'obs')

# Top bar
bar = Obj('#FFFFFF', 0, 195, 50, False, None)
bar.t.shapesize(stretch_wid = 0.5, stretch_len = 50)

pl = Obj('#00FF00', 0, 20, 1, True, 'pl')

jumpTime = 2*framerate

def jump():
	global jumpTime
	if jumpTime >= framerate/2:
		speedDict[pl] = [speedDict[pl][0], jHeight]
		jumpTime = 0
	else:
		pass;

def jump_down():
	pl.down()

def main():

	global sp
	sp = speed
	global jumpTime

	score = 0
	elapsed = 0

	# Starting off the game
	for obj in speedDict:
		obj.t.goto(obj.x, obj.y)

	# Countdown until the beginning
	pen.goto(5, 225)
	for i in range(0, 30):
		pen.write((str(round((3 - (i/10)), 1)) + ' until start'), align = 'center', font = ('Times', 20, 'normal'))
		sleep(0.1)
		pen.clear()

	while True:
		wn.update()

		pen.clear()
		pen.write(score, align = 'center', font = ('Times', 20, 'normal'))

		for obj in speedDict:
			# Moving everything
			obj.t.goto(obj.t.xcor() + (speedDict[obj][0]/framerate), obj.t.ycor() + (speedDict[obj][1]/framerate))
			# Gravity for player
			if obj.gr == True:
				speedDict[obj] = [speedDict[obj][0], speedDict[obj][1] - (grv/framerate)]
			# Making sure nothing has collided
			for obj2 in speedDict:
				if obj != obj2 and obj != pl and obj2 != pl:
					if obj.collided(obj2):
						obj.t.sety(obj.t.ycor() + choice(-20, 20))

		#Jumping
		wn.listen()
		wn.onkeypress(jump, 'Up')
		wn.onkeypress(jump_down, 'Down')

		#Moving back to the right, and increasing speed
		for obj in speedDict:
			obj.upd()
			if obj.t.xcor() < -440:
				if obj == pl:
					return None
				else:
					obj.change_layer(randint(-3, 3))
					obj.t.goto(440, obj.y)

		# Not letting people escape up
		if pl.t.ycor() > 180:
			speedDict[pl][1] = -30
			pl.t.sety(pl.t.ycor() - 5)

		# The player staying on top of objects
		for obj in speedDict:
			if obj != pl:
				if pl.collided(obj):

					# If it's colliding from the horizontal
					if pl.angle(obj) < atan(1/4) and pl.angle(obj) > atan(-1/4):
						if obj.t.xcor() > pl.t.xcor():
							return None;
					else:
						speedDict[pl][1] *= bounce
						if obj.t.ycor() < pl.t.ycor():
							pl.t.sety(obj.t.ycor() + 20)
						else:
							pl.t.sety(obj.t.ycor() - 20)

		# This brings up the 'death' animation
		if pl.t.ycor() < -260:
			return None;

		# Delays
		sp *= (1 + speedUpRate/framerate)
		elapsed += 1
		if jumpTime < framerate/2:
			jumpTime += 1
		if elapsed%(framerate*scoreRate) == 0:
			score += 1
		sleep(1/framerate)

def death():
	for obj in speedDict:
		obj.t.goto(1000, 0)

	wn.update()

	pen.goto(0, 0)
	pen.write('You died', align = 'center', font = ('Times', 30, 'bold'))
	sleep(2)
	pen.clear()

while True:
	main()
	death()