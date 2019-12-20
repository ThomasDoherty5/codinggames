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
speedUpRate = 0.04
downJump = 80
jumpTime = 2*framerate
specialEffectsRarity = 1
coinScore = 4
powerTime = 10

highscore = 0

# For storing the speeds of objects
# Will store as vectors
speedDict = {}

# For writing text
pen = Turtle()
pen.hideturtle()
pen.penup()

# Window
wn = Screen()
wn.bgcolor('#2288CC')
wn.title("Runner Game")
wn.setup(height = 500, width = 800)
wn.tracer(0)
wn.listen()
wn.onkeypress(bye, 'Escape')

# For purposes of changing the speed later
sp = speed

colors = [
'#FF0000', '#FF4000', '#FF8000', '#FFC000', '#FFFF00',
'#C0FF00', '#80FF00', '#40FF00', '#00FF00', '#00FF40', '#00FF80', '#00FFC0', '#00FFFF',
'#00C0FF', '#0040FF', '#0000FF', '#4000FF', '#8000FF', '#C000FF', '#FF00FF',
'#FF00C0', '#FF0080', '#FF0040'
]

abilitiesDict = {
'iJ':'#802010', 'dC':'#701370'
}

# For everything on-screen
class Obj():

	# x and y are STARTING coords
	def __init__(self, color, x, y, length, grav, t):
		self.t = Turtle()
		self.t.penup()
		self.t.color(color)
		self.t.goto(x, y)
		self.t.shape('square')
		self.t.shapesize(stretch_len = length);
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
			if int(obj.t.xcor()//1) in range(int((self.t.xcor() - 50)//1), int((self.t.xcor()+51)/1)):
				if int(obj.t.ycor()//1) in range(-440, int(self.t.ycor()//1)):
					self.t.sety(obj.t.ycor()+20)
					speedDict[self][1] = 0
					return None
		self.t.sety(pl.t.ycor() - downJump)

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
coin = Obj('#FFCC22', 500, randint(-3, 3)*100, 1, False, None); coin.t.shape('circle')

# Top bar
bar = Obj('#FFFFFF', 0, 195, 50, False, None)
bar.t.shapesize(stretch_wid = 0.5, stretch_len = 50)

# Player
pl = Obj('#00FF00', 0, 20, 1, True, 'pl')

coinPower = None
jumpDelay = True

def jump():
	global jumpTime
	if jumpTime >= framerate/2 or jumpDelay == False:
		speedDict[pl] = [speedDict[pl][0], jHeight]
	elif jumpDelay == True:
		pass;

def jump_down():
	pl.down()

dis = 0

# Main game (not counting death)
def main():

	global sp
	global jumpTime
	global highscore
	global dis; dis = 0
	global coinScore
	powerEligibility = True
	pTime = 0 #Time since last gotten power
	sp = speed

	score = 0
	elapsed = 0

	speedDict[pl] = [0, 0]

	# Power the coin has
	coinPower = None;

	# Player power
	playerPower = None

	#Is there a jump delay?
	jumpDelay = True

	# Starting off the game
	for obj in speedDict:
		obj.t.goto(obj.x, obj.y)

	# Countdown until the beginning
	pen.goto(5, 225)
	for i in range(0, 30):
		pen.write((str(round((3 - (i/10)), 1)) + ' until start'), align = 'center', font = ('Times', 20, 'normal'))
		sleep(0.1)
		pen.clear()

	# Real 'main loop' in main()
	while True:
		# Refresh the screen
		wn.update()

		pen.clear()
		pen.write("Score: " + str(score) + "     High Score: " + str(highscore) + "     Distance: " + str(int(dis//1)),
			align = 'center', font = ('Times', 20, 'normal'))

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
						obj.t.sety(obj.t.ycor() + choice([-20, 20]))

		#Random special effects generator
		if powerEligibility:
			if randint(1, specialEffectsRarity*framerate) == 5:
				if coinPower is None:
					p = choice(list(abilitiesDict.keys())); coinPower = p; coin.t.color(abilitiesDict[p])

		#Special effects (runs every loop iteration)
		#Deleted old code because it was structured badly
		if coinPower is not None: #Powers on line 55
			# No more powers for you
			powerEligibility = False

			if pl.collided(coin):
				playerPower = coinPower
				coinPower = None
				coin.t.color('#FFCC22')

				#Lightening the background slightly
				wn.bgcolor('#55AADD')

				# Time with power
				pTime = 0

		# Powers!
		if playerPower is not None:
			if playerPower == 'iJ':
				jumpDelay = False
			elif playerPower == 'dC' and pTime == 0:
				coinScore *= 2

			if pTime > framerate*powerTime:
				wn.bgcolor('#2288CC')
				coinPower = None
				playerPower = None
				powerEligibility = True

				#Ending the powers
				coinScore *= 1/2
				jumpDelay = True

		#Jumping
		wn.listen()
		wn.onkeypress(jump, 'Up')
		wn.onkeypress(jump_down, 'Down')

		#Moving back to the right, and increasing speed
		for obj in speedDict:
			obj.upd()
			if obj.t.xcor() < -440:
				if obj == pl:
					return score
				else:
					obj.change_layer(randint(-3, 3))
					if obj == coin:
						obj.t.sety(randint(-3, 3)*100)
					else:
						obj.t.color(choice(colors))
					obj.t.goto(440, obj.y)

		# Not letting people escape up
		if pl.t.ycor() > 180:
			speedDict[pl][1] = -30
			pl.t.sety(pl.t.ycor() - 5)

		#Scoring points with the coin
		if coin.collided(pl):
			score += coinScore
			coin.t.setx(600)
			coin.t.sety(choice([-3, -2, -1, 0, 1, 2, 3])*50)

		# The player staying on top of objects
		for obj in speedDict:
			if obj != pl:
				if pl.collided(obj):

					# If it's colliding from the horizontal
					if pl.angle(obj) < atan(1/4) and pl.angle(obj) > atan(-1/4):
						if obj.t.xcor() > pl.t.xcor():
							return score;
					else:
						speedDict[pl][1] *= bounce
						if obj.t.ycor() < pl.t.ycor():
							pl.t.sety(obj.t.ycor() + 20)
						else:
							pl.t.sety(obj.t.ycor() - 20)

		# This brings up the 'death' animation
		if pl.t.ycor() < -260:
			return score;

		# Score checking
		if score > highscore:
			highscore = score

		# Delays
		pTime += 1
		sp *= (1 + speedUpRate/framerate)
		dis += sp/(framerate*20);
		elapsed += 1
		if jumpTime < framerate/2:
			jumpTime += 1
		if elapsed%(framerate*scoreRate) == 0:
			score += 1
		sleep(1/framerate)

def death(sc):
	coinPower = None; playerPower = None; wn.bgcolor('#2288CC')
	global dis
	for obj in speedDict:
		obj.t.goto(1000, 0)

	wn.update()

	pen.goto(0, 0)
	pen.write('You died!    Score: ' + str(sc) + '     Distance: ' + str(int(dis//1)), align = 'center', font = ('Times', 30, 'bold'))
	sleep(2)
	pen.clear()

# This is in a try-except clause to get rid of the massive 'error' occurring in earlier versions:
'''
Traceback (most recent call last):
  File "runnergame.py", line 251, in <module>
    sc = main()
  File "runnergame.py", line 154, in main
    pen.clear()
  File "/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/turtle.py", line 2642, in clear
    self._clear()
  File "/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/turtle.py", line 2620, in _clear
    self.screen._delete(item)
  File "/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/turtle.py", line 557, in _delete
    self.cv.delete(item)
  File "<string>", line 1, in delete
  File "/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/tkinter/__init__.py", line 2818, in delete
    self.tk.call((self._w, 'delete') + args)
_tkinter.TclError: invalid command name ".!canvas"
'''
debugMode = False;

if not debugMode:
	try:
		while True:
			sc = main()
			death(sc)
	except:
		pass;
else:
	while True:
		sc = main()
		death(sc)
